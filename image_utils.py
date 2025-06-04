import os
from PIL import Image, ImageFilter
import os


ASSETS_DIR = "assets"


def ensure_assets_dir():
    os.makedirs(ASSETS_DIR, exist_ok=True)


def apply_filter(path, filter_type="BLUR"):

    img = Image.open(path)
    if filter_type == "BLUR":
        img = img.filter(ImageFilter.BLUR)
    elif filter_type == "CONTOUR":
        img = img.filter(ImageFilter.CONTOUR)

    os.makedirs("assets", exist_ok=True)
    img.save("assets/output.jpg")



def resize_image(path, size=(512, 512)):

    img = Image.open(path)
    img = img.resize(size)

    os.makedirs("assets", exist_ok=True)
    img.save("assets/resized.jpg")

