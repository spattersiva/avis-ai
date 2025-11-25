import streamlit as st
import requests
from PIL import Image
import io

API_URL = "https://api-inference.huggingface.co/models/kandinsky-community/kandinsky-2-1"
headers = {"Authorization": f"Bearer YOUR_HF_TOKEN"}

def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    image_bytes = response.content
    return Image.open(io.BytesIO(image_bytes))

@st.cache_resource
def app():
    st.title("Kandinsky Text to Image")

    prompt = st.text_input("Enter prompt")
    if st.button("Generate"):
        with st.spinner("Generating..."):
            img = generate_image(prompt)
            st.image(img)

app()


