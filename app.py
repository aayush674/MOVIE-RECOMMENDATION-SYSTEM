import streamlit as st
import pickle
import requests
st.title("Movie Recommender System")

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=9165ecf0be5f3cbe1566a53674a7ab06&language=en-US'.format((movie_id)))
    data=response.json()
    return "https://image.tmdb.org/t/p/original"+data['poster_path']
def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_lists = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_lists:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies=pickle.load(open('movies.pkl','rb'))
movies_list=movies['title'].values
similarity=pickle.load(open('sim.pkl','rb'))
selected_movie=st.selectbox(
    'Movies',movies_list
)
if st.button('Recommend'):
    names,posters=recommend(selected_movie)

    col1,col2=st.columns(2)
    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])

    col1, col2 = st.columns(2)
    with col1:
        st.image(posters[2])
        st.text(names[2])
    with col2:
        st.image(posters[3])
        st.text(names[3])

    col1, col2 = st.columns(2)
    with col1:
        st.image(posters[4])
        st.text(names[4])
    with col2:
        st.image(posters[5])
        st.text(names[5])

    col1, col2 = st.columns(2)
    with col1:
        st.image(posters[6])
        st.text(names[6])
    with col2:
        st.image(posters[7])
        st.text(names[7])

    col1, col2 = st.columns(2)
    with col1:
        st.image(posters[8])
        st.text(names[8])
    with col2:
        st.image(posters[9])
        st.text(names[9])

