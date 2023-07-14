# import pickle
import pandas as pd
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=2e7cffa5c80d314b8bd2c787c53ac848&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

st.set_page_config(layout="wide", page_title="FilmNXT", page_icon="logo/logo-color-circle.png")


container_css = """
    <style>
        [data-testid="block-container"]{
            background-repeat: no-repeat;
            background-size: auto;
        }
    </style>
"""

st.markdown(container_css, unsafe_allow_html=True)
st.image("logo/logo-no-background.png",width=800)
st.markdown("<p style='font-size: 18px;'>What would you like to watch next?</p>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .main {
        background-color: #000;
    }
    h1 {
        color: red;
    }
    p {
        color: white;
    }
    img{
        width: 200px; 
        height: 300px; 
        
    }
    
    /* Button */
    .css-7ym5gk{
        background-color: red;
    }
    /* Header*/
    .e13qjvis2{
        background-color: rgb(49, 51, 63);
    }
    
    /* Text Below Movies */
    .css-183lzff{
        color: #fff;
    }
    
    /* Footer*/
    .e1g8pov61{
        color: #000;
     }

    </style>
    """,unsafe_allow_html=True
)


st.header('Find Similar Movies')

movies = pd.read_pickle('movie_list.pkl')
similarity = pd.read_pickle('similarity.pkl')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown.",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        html_code = f'<a href="https://www.google.com/search?q={recommended_movie_names[0]}%20Movie" target="_blank">'\
                    f'<img src="{recommended_movie_posters[0]}"></a>'
        st.markdown(html_code, unsafe_allow_html=True)
        st.write(recommended_movie_names[0])

    with col2:
        html_code = f'<a href="https://www.google.com/search?q={recommended_movie_names[1]}%20Movie" target="_blank">'\
                    f'<img src="{recommended_movie_posters[1]}"></a>'
        st.markdown(html_code, unsafe_allow_html=True)
        st.write(recommended_movie_names[1])

    with col3:
        html_code = f'<a href="https://www.google.com/search?q={recommended_movie_names[2]}%20Movie" target="_blank">'\
                    f'<img src="{recommended_movie_posters[2]}"></a>'
        st.markdown(html_code, unsafe_allow_html=True)
        st.write(recommended_movie_names[2])

    with col4:
        html_code = f'<a href="https://www.google.com/search?q={recommended_movie_names[3]}%20Movie" target="_blank">'\
                    f'<img src="{recommended_movie_posters[3]}"></a>'
        st.markdown(html_code, unsafe_allow_html=True)
        st.write(recommended_movie_names[3])

    with col5:
        html_code = f'<a href="https://www.google.com/search?q={recommended_movie_names[4]}%20Movie" target="_blank">'\
                    f'<img src="{recommended_movie_posters[4]}"></a>'
        st.markdown(html_code, unsafe_allow_html=True)
        st.write(recommended_movie_names[4])


st.header('How it Works?')
st.write("FilmNXT application uses Content Based Recommendation System. <br>You will be asked to choose a movie that"
         " you have already watched, and other movies similar to that will be suggested. <br>The Suggestions are "
         "curated based on genre, cast, production company, director and other factors. <br>This creates an "
         "extensive mapping of the movies with the other factors that are taken into consideration, making this the"
         " best movie recommender",unsafe_allow_html=True)

