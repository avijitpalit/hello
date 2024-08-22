import time
from huggingface_hub import InferenceClient
import random
import json
import schedule

client = InferenceClient(model="black-forest-labs/FLUX.1-dev", token="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")
with open('prompt.json', 'r') as jsonfile:
    prompts = json.load(jsonfile)

def generate():
    try:
        print("Generating...")
        random_element = random.choice(prompts)
        prompt = f"{random_element['prompt'].strip()} --seed {random.randint(1, 99)}"
        #prompt = "Create a detailed, evocative description of a stunning bride on her wedding day. Include physical attributes, emotions, and the overall ambiance. --ar 16:9 --v 6.0 --style raw"
        image = client.text_to_image(
                prompt,
                width=1920,
                height=1072
            )
        print(image)
        image.save(f"wallpaper/flux_{random.random()}.png", format="PNG")
        print("Image saved")
    except Exception as e:
        print(f"ERROR: {e}")

generate()
schedule.every(10).minutes.do(generate)
while True:
    schedule.run_pending()
    time.sleep(1)

