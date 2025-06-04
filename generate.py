import requests
import os


def generate_image_from_prompt(prompt):
    url = "https://api.stability.ai/v2beta/stable-image/generate"
    headers = {
        "Authorization": "sk-CBsbVK5KVZYWwygFzyXdKWKdy0w1k0J7IJrfb7BjjxUDcNmm"}
    data = {
        "prompt": prompt,
        "style": "anime"
    }
    r = requests.post(url, headers=headers, json=data)
    os.makedirs("assets", exist_ok=True)
    with open("assets/generated.jpg", "wb") as f:
        f.write(r.content)
    return "assets/generated.jpg"
