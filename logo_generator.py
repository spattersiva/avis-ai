from diffusers import StableDiffusionPipeline
import torch

# Load the Stable Diffusion model only once
pipe = StableDiffusionPipeline.from_pretrained(
    "kandinsky-community/kandinsky-2-1-mini" ,
    torch_dtype=torch.float32).to('cpu')

def generate_logo(business_name, description=""):
    prompt = f"Professional minimalist logo design for a company named '{business_name}'. {description}. Vector, clean, modern, white background"
    image = pipe(prompt, num_inference_steps=20, guidance_scale=7.5).images[0]
    return image
