import os

import streamlit as st
from PIL import Image

import style

# start with `streamlit run main.py`

st.title("Pytorch Style Transfer")

img = st.sidebar.selectbox("Select image", tuple(os.listdir("images/content-images")))
style_name = st.sidebar.selectbox("Select image", tuple([x.split('.')[0].replace('-', '_') for x in os.listdir("images/style-images")]))

model = "saved_models/" + style_name + '.pth'
input_image = "images/content-images/" + img
output_image = "images/output-images/" + style_name + "_" + img

style.load_model(model)

st.write("### Source image:")
image = Image.open(input_image)
st.image(image, width=400)

clicked = st.button("Stylize")
if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)
    st.write("### Output image:")
    image = Image.open(output_image)
    st.image(image, width=400)