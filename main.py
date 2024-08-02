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
        # GET MOVIE DATA
        key1 = '329578fe'
        url1 = f"https://www.omdbapi.com/?apikey=329578fe&t={template}"
        response1 = requests.get(url1)
        data1 = response1.json()

        # GET STREAMING DATA
        url2 = f"https://streaming-availability.p.rapidapi.com/shows/search/title"
        querystring = {"country": "us", "title": f"{name}", "series_granularity": "show", "show_type": "movie", "output_language": "en"}
        headers = {
            "x-rapidapi-key": "1b6ce2494dmshf74f9c461b4cdbbp1d3b11jsndd6ab0d8575c",
            "x-rapidapi-host": "streaming-availability.p.rapidapi.com"
        }

        response2 = requests.get(url2, headers=headers, params=querystring)
        data2 = response2.json()

        st.image(data1['Poster'])

        with col2:
            st.write("Title: " + data1["Title"])
            st.write("Year: " + data1["Year"])
            st.write("Rated: " + data1["Rated"])
            st.write("Released: " + data1["Released"])
            st.write("Runtime: " + data1["Runtime"])
            st.write("Genre: " + data1["Genre"])
            st.write("Director: " + data1["Director"])
            st.write("Writer: " + data1["Writer"])
            st.write("Actors: " + data1["Actors"])
            st.write("Plot: " + data1["Plot"])
            st.write("Language: " + data1["Language"])
            st.write("Country: " + data1["Country"])
            st.write("Awards: " + data1["Awards"])

            services = []
            for v in data2[0]["streamingOptions"]["us"]:
                if 'name' in v["service"]:
                    services.append(v["service"]["name"])
                else:
                    continue

            services = str(set(services))
            services = services.replace("'", "")
            services = services.replace("{", "")
            services = services.replace("}", "")

            st.write("Streaming On: ", services)
