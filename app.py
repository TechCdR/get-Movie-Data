import requests
import streamlit as st



def get_movie_data(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey=5d98bf8c"
    response = requests.get(url)
    data = response.json()
    return {
        "Title": data["Title"],
        "Year": data["Year"],
        "Poster": data["Poster"],
        "Plot": data["Plot"],
        "Actors": data["Actors"],
        "imdbRating": data["imdbRating"],
    }

st.header("Tech Coder :boy:   get Movie Data 🎥 ML Project")

left, right = st.columns([1, 2])

title = st.text_input("Enter Movie Name :")


if st.button("Search"):
    movie_data = get_movie_data(title)


    with left:
        st.image(movie_data["Poster"])
    
    with right:
        st.write("\n\n")
        st.write(f"Movie Name =>   {movie_data['Title']}")
        st.write(f"release Year =>  {movie_data['Year']}")
        st.write(f"description =>  {movie_data['Plot']}")
        st.write(f"Actors =>  {movie_data['Actors']}")
        st.write("Movie Rating =>  ", movie_data["imdbRating"])


# costom style
with open("style/style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
