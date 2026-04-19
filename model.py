import torch
from diffusers import StableDiffusionPipeline
import streamlit as st

# Load model once (important for Streamlit)
@st.cache_resource
def load_model():
    return StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe=load_model()

pipe.enable_attention_slicing()
pipe.enable_sequential_cpu_offload()

pipe = load_model()
def generate_image(prompt):
    image = pipe(
        prompt,
        num_inference_steps=15
    ).images[0]

    image_path = "generated.png"
    image.save(image_path)
    return image_path
