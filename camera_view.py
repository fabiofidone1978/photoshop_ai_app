import os
from PIL import Image


def take_photo():
    """
    Simula uno scatto foto (mock compatibile desktop).
    Su Android dovrai usare AKCamera direttamente in UI.
    """
    output_path = "assets/capture.jpg"

    if not os.path.exists("assets"):
        os.makedirs("assets")

    # Simula uno scatto salvando una semplice immagine
    img = Image.new("RGB", (512, 512), color="gray")
    img.save(output_path, "JPEG")

    return output_path
