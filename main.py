import requests
import json as js
from icecream import ic
import streamlit as st


col1, col2 = st.columns(2)

with col1:
    st.title("IMDB API")
    name = st.text_input("Movie Name")
    if st.button("Submit"):
        name_split = name.split()
        length = len(name_split)

        dynamic_vars = {}
        count = 0
        for i in range(length):
            dynamic_vars[f"var_{i}"] = name_split[i]
            count += 1

        template = ""

        for k, v in enumerate(name_split):
            template = template + f"{name_split[k]}+"

        template = template[:-1]

        key = '329578fe'
        url = f"https://www.omdbapi.com/?apikey=329578fe&t={template}"
        response = requests.get(url)
        data = response.json()

        st.image(data['Poster'])

        with col2:
            st.write("Title: " + data["Title"])
            st.write("Year: " + data["Year"])
            st.write("Rated: " + data["Rated"])
            st.write("Released: " + data["Released"])
            st.write("Runtime: " + data["Runtime"])
            st.write("Genre: " + data["Genre"])
            st.write("Director: " + data["Director"])
            st.write("Writer: " + data["Writer"])
            st.write("Actors: " + data["Actors"])
            st.write("Plot: " + data["Plot"])
            st.write("Language: " + data["Language"])
            st.write("Country: " + data["Country"])
            st.write("Awards: " + data["Awards"])


