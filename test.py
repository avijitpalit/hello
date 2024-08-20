import requests
import io
from PIL import Image
import random
import schedule
import time
import json

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

with open('prompt.json', 'r') as jsonfile:
  prompts = json.load(jsonfile)

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def generate():
  try:
    random_element = random.choice(prompts)
    prompt = random_element['prompt'].strip()

    image_bytes = query({
      "inputs": prompt,
      "parameters": {
        "width": 1920,
        "height": 1080,
        # "randomize_seed": True
      }
    })
    image = Image.open(io.BytesIO(image_bytes))
    image.save(f"wallpaper/flux_{random.random()}.png", format="PNG")
  except Exception as e:
    print(f"Error: {e}")

generate()
""" schedule.every(5).minutes.do(generate)
while True:
    schedule.run_pending()
    time.sleep(1) """