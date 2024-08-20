from gradio_client import Client
import gradio_client.exceptions
import shutil
import os
import wallpaper
import json
import sys
import random
import time
import threading
import schedule

def generate():
	with open('prompt.json', 'r') as jsonfile:
		prompts = json.load(jsonfile)

	random_element = random.choice(prompts)
	prompt = random_element['prompt'].strip()
	neg_prompt = random_element['neg_prompt'].strip()

	try:
		client = Client("black-forest-labs/FLUX.1-dev")
		result = client.predict(
				prompt=prompt,
				seed=0,
				randomize_seed=True,
				width=1920,
				height=1080,
				guidance_scale=3.5,
				num_inference_steps=28,
				api_name="/infer"
		)

		print(result)

		# sourceImg1 = result[0][0]['image']
		# sourceImg2 = result[0][1]['image']
		# print(sourceImg)
		sourceImg = result[0]
		destImg = f'wallpaper/wallpaper_{random.random()}.png'
		wallpaper.convert_webp_to_png(sourceImg, destImg)

		# shutil.copy(sourceImg, os.getcwd() + "/wallpaper/")
		# shutil.copy(sourceImg2, os.getcwd() + "/wallpaper/")
		# print("Image copied")

		# Set wallpaper
		wallpaper.set(os.path.abspath(destImg))
	except Exception as e:
		print(f"Error: {e}")

generate()

schedule.every(10).minutes.do(generate)
while True:
    schedule.run_pending()
    time.sleep(1)

