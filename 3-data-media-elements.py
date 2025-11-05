import streamlit as st

st.title("**Anggota Kelompok:**")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")


st.title("Displaying an Images")
# Displaying Image by specifying path
st.image("assets/img1.jpg")
# Image Courtesy byunplash
st.write("Image Courtesy: unplash.com")

# Image Coutesy
st.title("Displaying Multiple Images")
# Listing out animal images
animal_images = [
    'assets/img1.jpg',
    'assets/img2.jpg',
    'assets/img3.jpg',
    'assets/img4.jpg',
    'assets/img5.jpg'
]
# Displaying Multiple images with width 150
st.image(animal_images, width=150)
# Image Courtesy
st.write("Image Courtesy: unplash")


import base64
# Function to set Image as Background
def add_local_background_image_(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: unplash")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
st.write("Background Image")
# Calling Image in function
add_local_background_image_("assets/img.jpg")

from PIL import Image

original_image = Image.open("assets/img2.jpg")
# Display Original Image
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600 * 400
resized_image = original_image.resize((600, 400))
# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)