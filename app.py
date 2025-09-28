import streamlit as st
import pandas as pd
import os
import pickle
import requests

def fetch_posters(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YjFiNGM0MjUzZTdlY2IxZjRiMWQ3OGMxNzk0MDhiZSIsIm5iZiI6MTc1MjkwMTMzNC44NDksInN1YiI6IjY4N2IyNmQ2ZmQ5NDU1MzFlZThhNDE5YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RJWWyVWSOI5SFW79hYZd1xbNMXijgYR9rKqL67XW99U"
    }
    response = requests.get(url,headers=headers)
    data = response.json()
    return "http://image.tmdb.org/t/p/w780" + data['poster_path']

st.title('Movie Recommender System')
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)
selected_movie_name = st.selectbox('Select the movie',movies['title'].values,None)

# recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] # calculating the index from the dataframe
    distances = similarity[movie_index] # distances for that particualr index from the similarity matrx
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6] # getting the distances of only 5 movies that are most similar
    # enumerate will result in id + similarity score --- the 0 will result in the id
    
    recommended_movies = []
    movies_posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        poster = fetch_posters(movies.iloc[i[0]].movie_id)
        movies_posters.append(poster)
    return recommended_movies,movies_posters

# for recommended movies list we have to pass the selected movie name to a function recommend it will get the most similar movies from the similarity matrix and shows it to the user
if st.button('Recommend'):
    recommended_movies, posters = recommend(selected_movie_name)
    st.write(selected_movie_name)

    # Create 5 columns
    cols = st.columns(5)

    # Loop through the recommended movies and display their titles and posters
    for i in range(5):
        with cols[i]:
            st.text(recommended_movies[i])
            st.image(posters[i])


