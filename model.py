import streamlit as st
import torch
from diffusers import KandinskyV22Pipeline

@st.cache_resource
def load_pipe():
    pipe = KandinskyV22Pipeline.from_pretrained(
        "kandinsky-community/kandinsky-2-2-decoder",
        torch_dtype=torch.float32
    )
    pipe.to("cpu")
    return pipe

def generate_image(prompt):
    pipe = load_pipe()
    img = pipe(prompt=prompt).images[0]

    path = "static/output.png"
    img.save(path)
    return path
