import torch
from diffusers import StableDiffusionPipeline

# Load model once (important for Streamlit)
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cpu")

def generate_image(prompt):
    image = pipe(
        prompt,
        num_inference_steps=25
    ).images[0]

    image_path = "generated.png"
    image.save(image_path)
    return image_path
