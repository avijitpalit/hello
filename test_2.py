from huggingface_hub import InferenceClient
import random, time, json, schedule, wallpaper, os

# client = InferenceClient(model="black-forest-labs/FLUX.1-dev", token="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")
client = InferenceClient(model="John6666/epicrealism-xl-v8kiss-sdxl", token="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")
with open('prompts.json', 'r') as jsonfile:
    prompts = json.load(jsonfile)

def generate():
    try:
        print("Generating...")
        random_element = random.choice(prompts)
        prompt = f"{random_element['prompt'].strip()} --seed {random.randint(1, 99)}"
        #prompt = "Create a detailed, evocative description of a stunning bride on her wedding day. Include physical attributes, emotions, and the overall ambiance. --ar 16:9 --v 6.0 --style raw"
        image = client.text_to_image(
                "b&w, instagram photo, portrait photo of 26 y.o blonde woman, perfect detailed eyes, natural skin, hard shadows, film grain"
            )
        print(image)
        wallpaper_path = f"wallpaper/flux_{random.random()}.png"
        image.save(wallpaper_path, format="PNG")
        print("Image saved")
        # wallpaper.set(os.path.abspath(wallpaper_path))
        # print("Wallpaper changed")
    except Exception as e:
        print(f"ERROR: {e}")

generate()

""" schedule.every(5).minutes.do(generate)
while True:
    schedule.run_pending()
    time.sleep(1) """

