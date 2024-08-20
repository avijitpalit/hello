import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/SG161222/RealVisXL_V4.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Check for successful status code
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        print("Response:", response.text)
        return None

    # Check if the response content is in JSON format (usually indicates an error)
    if response.headers.get("content-type") == "application/json":
        print("Error:", response.json())
        return None

    return response.content

image_bytes = query({
    "inputs": "a pretty bride"
})

if image_bytes:
    try:
        image = Image.open(io.BytesIO(image_bytes))
        image.show()
    except Image.UnidentifiedImageError as e:
        print("Could not identify image file:", e)
else:
    print("No image returned by the API.")
