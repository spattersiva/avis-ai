import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from huggingface_hub import login
import os

hf_token=os.environ.get("HF_TOKEN")
if hf_token:
    login(token=hf_token)
else:
    print("Huggice face token not found")

@st.cache_resource
def load_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "kandinsky-community/kandinsky-2-1-mini"
,  # much smaller than sd-turbo
        torch_dtype=torch.float32
    ).to("cpu")
    pipe.enable_attention_slicing()
    return pipe

st.title("🎨 AI Logo Generator")
pipe = load_model()

business = st.text_input("Enter business name:")
if st.button("Generate"):
    if business:
        prompt = f"Modern logo design for '{business}', vector, clean, white background"
        st.info("Generating...")
        image = pipe(prompt, num_inference_steps=10, guidance_scale=6).images[0]
        st.image(image, caption=f"Logo for {business}")
    else:
        st.warning("Please enter a name.")


