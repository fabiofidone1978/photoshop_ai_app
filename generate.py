import os
import requests


def generate_image_from_prompt(prompt):
    url = "https://api.stability.ai/v2beta/stable-image/generate"
    api_key = os.environ.get("STABILITY_API_KEY")
    if not api_key:
        raise RuntimeError("STABILITY_API_KEY environment variable not set")
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {
        "prompt": prompt,
        "style": "anime"
    }
    r = requests.post(url, headers=headers, json=data)
    r.raise_for_status()
    os.makedirs("assets", exist_ok=True)
    with open("assets/generated.jpg", "wb") as f:
        f.write(r.content)
    return "assets/generated.jpg"
