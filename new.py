# app.py
import streamlit as st
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

@st.cache_resource
def load_pipeline_cpu(model_id: str = "runwayml/stable-diffusion-v1-5"):
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32,
        safety_checker=None,  # optional
    )
    pipe.to("cpu")
    pipe.enable_attention_slicing()
    return pipe

st.title("CPU Text-to-Image (Stable Diffusion)")

prompt = st.text_area(
    "Prompt",
    "a futuristic Chennai skyline at sunset, cinematic, highly detailed",
)
negative_prompt = st.text_input(
    "Negative prompt",
    "low quality, blurry, distorted, watermark",
)

col1, col2, col3 = st.columns(3)
with col1:
    steps = st.slider("Steps", 5, 30, 15)  # fewer steps = faster on CPU [web:84]
with col2:
    cfg = st.slider("Guidance scale", 1.0, 15.0, 7.5)
with col3:
    size = st.selectbox("Size", ["256x256", "384x384", "512x512"], index=1)

width, height = map(int, size.split("x"))
seed = st.number_input("Seed (optional, -1 for random)", value=123, step=1)

if st.button("Generate"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        st.info("Loading model (first run) and generating image on CPU...")
        pipe = load_pipeline_cpu()
        generator = torch.Generator(device="cpu")
        if seed >= 0:
            generator.manual_seed(int(seed))

        with torch.no_grad():
            image = pipe(
                prompt=prompt,
                negative_prompt=negative_prompt or None,
                height=height,
                width=width,
                num_inference_steps=int(steps),
                guidance_scale=float(cfg),
                generator=generator,
            ).images[0]

        st.image(image, caption="Generated image", use_column_width=True)

        # Optionally allow download
        img_filename = "generated.png"
        image.save(img_filename)
        with open(img_filename, "rb") as f:
            st.download_button("Download image", f, file_name=img_filename, mime="image/png")
