from diffusers import StableDiffusionPipeline
import torch

# Specify device: use 'cuda' if available for faster inference
device = "cuda" if torch.cuda.is_available() else "cpu"

# Model ID for the Stable Diffusion model
model_id = "CompVis/stable-diffusion-v1-4"

# Initialize the pipeline (you need to set your Hugging Face token)
pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token="YOUR_HF_AUTH_TOKEN")
pipe = pipe.to(device)

prompt = "A surreal landscape with floating islands and futuristic architecture at sunset"
result = pipe(prompt, num_inference_steps=50, guidance_scale=7.5)

# Save the generated image
image = result.images[0]
image.save("generated_landscape.png")
print("Image generated and saved as 'generated_landscape.png'")
