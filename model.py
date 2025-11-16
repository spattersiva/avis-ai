from diffusers import StableDiffusionPipeline
import torch
from deep_translator import GoogleTranslator
from huggingface_hub import login
import os
# Load lightweight model
hf=os.environ.get("HF")
model_id = "lambdalabs/sd-tiny"
login(hf)

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", low_cpu_mem_usage=True,torch_dtype=torch.float32)
pipe.to("cpu")


def generate_image(text):
    prompt =GoogleTranslator(source='auto',target='en').translate(text)
    image = pipe(prompt).images[0]
    image_path="static/output.png"
    image.save(image_path)
    return image_path