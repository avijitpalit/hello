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
  try:
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content
  except Exception as e:
    print(f"Error: {e}")

def generate():
  try:
    random_element = random.choice(prompts)
    prompt = random_element['prompt'].strip()

    image_bytes = query({
      "inputs": prompt,
      "parameters": {
        "width": 1920,
        "height": 1080,
        "seed": 0,
        "randomize_seed": True
      }
    })
    image = Image.open(io.BytesIO(image_bytes))
    image.save(f"wallpaper/flux_{random.random()}.png", format="PNG")
  except Exception as e:
    print(f"Error: {e}")

def generate_2():
  image_bytes = query({
    "inputs": "Cinematic photograph of a house in the light of day in front of a nature background --ar 16:9 --v 6.0 --style raw",
    "parameters": {
      "width": 1024,
      "height": 1024
    }
  })
  print(image_bytes)
  image = Image.open(io.BytesIO(image_bytes))
  image.show()

generate_2()
""" schedule.every(5).minutes.do(generate)
while True:
    schedule.run_pending()
    time.sleep(1) """