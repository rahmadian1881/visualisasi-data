import streamlit as st
import pandas as pd
import numpy as np

st.title("Map Chart")
st.write("Kelompok: 1")
st.markdown("""
    - Tria Maulida Sari (0110222300)
    - Rahma Dian Nurhikma - (0110222082)
    - Alma Nur Fajriah - (0110222222)
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]

)

st.map(df)
