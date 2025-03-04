import streamlit as st
import pandas as pd
import duckdb


st.write("""
# SQL SRS
Spaced Repetition System SQL practice
""")

option = st.selectbox(
    "What would you like to review?",
    ("Joins", "Group By", "Window functions"),
    index=None,
    placeholder="Select a theme"
)

st.write("You selected:", option)


data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["S", "Q", "L"])

with tab1:
    st.dataframe(df)
    query = st.text_area(label="entrez votre query")
    result = duckdb.sql(query).df()
    st.write(f"Vous avez entré la query suivant: {query}")
    st.dataframe(result)

with tab2:
    st.header("oui")

with tab3:
    st.header("non")