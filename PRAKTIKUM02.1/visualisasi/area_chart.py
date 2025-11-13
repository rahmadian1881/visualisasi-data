import streamlit as st
import pandas as pd
import numpy as np

st.title("Area Chart")
st.write("Kelompok: 1")
st.markdown("""
    - Tria Maulida Sari (0110222300)
    - Nama (NIM)
    - Nama (NIM)
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]

)

st.area_chart(df)
