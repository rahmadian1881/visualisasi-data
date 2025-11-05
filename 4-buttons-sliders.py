import streamlit as st

st.title("**Anggota Kelompok:**")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")


st.title('Creating a Button')

# Defining a Button
button = st.button('Click Here')
if button:
    st.write("You have Clicked the Button")
else:
    st.write("You have not Clicked the Button")

st.title("Creating Radio Buttons")

# Defining Radio Button
gender = st.radio(
    "Select Gender", 
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write("You have selected Male.")
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

st.title("Creating Checkboxes")
st.write("Seleect your Hobies: ")
# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

st.title('Creating Dropdown')
# Creating Dropdown
hobby = st.selectbox('Choose your Hobby: ',
('Books', 'Movies', 'Sports'))

st.title('Multi-Select')
# Defining Multi-Select with Pre-Selection
hobbies = st.multiselect(
    'What are your hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'], 
    ['Reading', 'Playing'])

st.title("Download Button")
# Creating Download Button
down_btn = st.download_button(
    label="Download Image",
    data=open("assets/img1.jpg", "rb"),
    file_name="img2.jpg",
    mime="image2/jpeg"
)

import time
st.title("Progress Bar")
# Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage + 1)
st.write("Download Complete")

st.title("Spinner")
# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')