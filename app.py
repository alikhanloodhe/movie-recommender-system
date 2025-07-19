import streamlit as st
import pandas as pd
import os
import pickle
import requests

# --------- parameters ---------
FILE_ID   = "1cmeXnYWta9mFAXQGav3mLxMWg4LFBugu"
FILE_URL  = f"https://drive.google.com/uc?export=download&id={FILE_ID}"
LOCAL_PKL = "similarity.pkl"

# --------- download similarity.pkl if absent ---------
if not os.path.exists(LOCAL_PKL):
    with st.spinner("Downloading similarity matrix…"):
        r = requests.get(FILE_URL, stream=True)
        if r.status_code == 200:
            with open(LOCAL_PKL, "wb") as f:
                for chunk in r.iter_content(1024 * 1024):  # 1 MB chunks
                    if chunk:
                        f.write(chunk)
        else:
            st.error(f"Download failed (HTTP {r.status_code})."); st.stop()

# --------- load data ---------
try:
    similarity = pickle.load(open(LOCAL_PKL, "rb"))
except Exception as e:
    st.error(f"Couldn’t load similarity matrix: {e}"); st.stop()

movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies       = pd.DataFrame(movies_dict)

# --------- TMDB token ---------
TMDB_TOKEN = st.secrets.get("TMDB_TOKEN", "YOUR_TOKEN_HERE")

def fetch_poster(movie_id: int) -> str:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {"accept": "application/json",
               "Authorization": f"Bearer {TMDB_TOKEN}"}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return "https://via.placeholder.com/300x450?text=No+Poster"
    path = resp.json().get("poster_path")
    return f"https://image.tmdb.org/t/p/w780{path}" if path \
           else "https://via.placeholder.com/300x450?text=No+Poster"

def recommend(movie_title: str):
    idx        = movies[movies["title"] == movie_title].index[0]
    distances  = similarity[idx]
    top5       = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:6]
    titles     = [movies.iloc[i].title        for i, _ in top5]
    posters    = [fetch_poster(movies.iloc[i].movie_id) for i, _ in top5]
    return titles, posters

# --------- UI ---------
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a movie", movies["title"].values, index=None)

if st.button("Recommend") and selected_movie:
    titles, posters = recommend(selected_movie)
    cols = st.columns(5)
    for col, t, p in zip(cols, titles, posters):
        with col:
            st.image(p)
            st.caption(t)
elif st.button("Recommend"):
    st.warning("Please choose a movie first.")
