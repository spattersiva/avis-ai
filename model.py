from diffusers import DiffusionPipeline
import torch
from deep_translator import GoogleTranslator
import os

# Lightweight, fast CPU model
MODEL_ID = "kandinsky-community/kandinsky-2-2-decoder"

# Load model
pipe = DiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float32
).to("cpu")


def generate_image(text):
    # Translate prompt to English
    prompt = GoogleTranslator(source="auto", target="en").translate(text)

    # Generate image
    out = pipe(
        prompt=prompt,
        num_inference_steps=20   # good quality + fast
    )

    image = out.images[0]

    # Save output
    image_path = "static/output.png"
    image.save(image_path)
    return image_path
