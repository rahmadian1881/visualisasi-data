import streamlit as st

st.title("**Anggota Kelompok:**")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")

st.title("Text Box")
# Creating text box
name = st.text_input("Enter your name")
st.write("Your name is: ", name)

# Creating Text Area
input_text = st.text_area("Enter your Review")
# Printing entered text
st.write("""You entered: \n""", input_text)

# Create number input
st.number_input("Enter your number")
num = st.number_input("Enter your number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. value is 10")
st.write("Default Value is 5, \n Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

st.title("Time")
# Defining Time Function
st.time_input("Select Your Time")

st.title("Date")
# Defining Date Function
st.date_input("Select Date")

import datetime
st.title("Date")
# Defining Time Function
st.date_input("Select Date", value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1970, 1, 1),
    max_value=datetime.date(2022, 12, 31))

st.title("Select Color")
# defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)

import pandas as pd
st.title("CSV Data")
data_file = st.file_uploader("Upload CSV file", type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type,
        "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submitted = my_form.form_submit_button(label='Submit')

st.write(a)
