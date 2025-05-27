import streamlit as st
import pickle as pkl
import pandas as pd
import requests

TMDB_API_KEY = '467d1b63934a99d98f93704c485f608c'

def fetch_poster(movie_title):
    response = requests.get(
        f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
    )
    data = response.json()
    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return full_path
    return None

similarity=pkl.load(open('similarity.pkl', 'rb'))
def recommend(movie):
    movie_index=movies_list[movies_list['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_posters=[]
    for i in movie_list:
        movie_title=movies_list.iloc[i[0]].title
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_title))
    return recommended_movies, recommended_posters
movies_list=pkl.load(open('movies.pkl', 'rb'))
movies_titles=movies_list['title'].values

st.title('Movie Recommender System')
selected_movie_name=st.selectbox(
    'Which movie made your day? We’ve got 5 more for you 💡',
    movies_titles
)
if st.button('Recommend'):
    names, posters=recommend(selected_movie_name)
    for i in range(len(names)):
        st.markdown(f"{names[i]}")
        if posters[i]:
            st.image(posters[i])
        else:
            st.text("Poster not available 😢")
