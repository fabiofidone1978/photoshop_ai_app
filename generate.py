from PIL import Image, ImageDraw, ImageFont
import os


def generate_image_from_prompt(prompt: str) -> str:
    """
    Genera un'immagine simulata (mock) da un prompt.
    """
    if not os.path.exists("assets"):
        os.makedirs("assets")

    img = Image.new("RGB", (512, 512), color="lightblue")
    draw = ImageDraw.Draw(img)

    # Font predefinito (non richiede installazione)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    # Scrive il prompt centrato
    draw.text((20, 230), f"AI Prompt:\n{prompt}", fill="black", font=font)

    output_path = "assets/generated.jpg"
    img.save(output_path, "JPEG")

    return output_path
