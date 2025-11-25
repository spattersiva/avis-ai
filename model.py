import streamlit as st
import requests
from PIL import Image
import io

API_URL = "https://api-inference.huggingface.co/models/kandinsky-community/kandinsky-2-1"
headers = {"Authorization": f"Bearer YOUR_HF_TOKEN"}

@st.cache_data
def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.conent


st.title("AVIS AI  Text to Image")
prompt = st.text_input("Enter prompt")
    
if st.button("Generate"):
        with st.spinner("Generating..."):
            image_bytes = generate_image(prompt)
            img=Image.open(io.BytesIO(image_bytes))
            st.image(img)





