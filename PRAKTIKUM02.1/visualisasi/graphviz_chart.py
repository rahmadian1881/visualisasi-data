import streamlit as st
import graphviz as gv

st.title("Map Chart")
st.write("Kelompok: 1")
st.markdown("""
    - Tria Maulida Sari (0110222300)
    - Rahma Dian Nurhikma - (0110222082)
    - Alma Nur Fajriah - (0110222222)
""")

st.graphviz_chart("""
digraph {
    "Training Data" -> "ML Algorithm"
    "ML Algorithm" -> "Model"
    "Model" -> "Result Forecasting"
    "New Data" -> "Model"}
""")

