import streamlit as st
import pandas as pd
import os
import pickle
import requests

# --------- parameters ---------
FILE_URL  = "https://www.dropbox.com/scl/fi/qe5ypv60xu1awlznky65j/similarity.pkl?rlkey=02i13m2udeur3fp0r17lhjsh8&e=1&dl=1"
LOCAL_PKL = "similarity.pkl"

# --------- download similarity.pkl if absent ---------
if not os.path.exists(LOCAL_PKL):
    with st.spinner("Downloading similarity matrix from Dropbox…"):
        try:
            response = requests.get(FILE_URL)
            response.raise_for_status()  # Raise error if download fails
            with open(LOCAL_PKL, "wb") as f:
                f.write(response.content)
        except Exception as e:
            st.error(f"Download failed: {e}")
            st.stop()

# --------- load data ---------
try:
    with open(LOCAL_PKL, "rb") as f:
        similarity = pickle.load(f)
except Exception as e:
    st.error(f"Couldn't load similarity matrix: {e}")
    st.stop()

movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

# --------- TMDB token ---------
TMDB_TOKEN = st.secrets.get("TMDB_TOKEN", "YOUR_TOKEN_HERE")

def fetch_poster(movie_id: int) -> str:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_TOKEN}"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return "https://via.placeholder.com/300x450?text=No+Poster"
    path = resp.json().get("poster_path")
    return f"https://image.tmdb.org/t/p/w780{path}" if path \
           else "https://via.placeholder.com/300x450?text=No+Poster"

def recommend(movie_title: str):
    idx = movies[movies["title"] == movie_title].index[0]
    distances = similarity[idx]
    top5 = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:6]
    titles = [movies.iloc[i].title for i, _ in top5]
    posters = [fetch_poster(movies.iloc[i].movie_id) for i, _ in top5]
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
