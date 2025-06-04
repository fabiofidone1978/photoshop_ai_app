import os
from PIL import Image, ImageFilter


ASSETS_DIR = "assets"


def ensure_assets_dir():
    os.makedirs(ASSETS_DIR, exist_ok=True)


def apply_filter(path, filter_type="BLUR"):
    ensure_assets_dir()
    img = Image.open(path)
    if filter_type == "BLUR":
        img = img.filter(ImageFilter.BLUR)
    elif filter_type == "CONTOUR":
        img = img.filter(ImageFilter.CONTOUR)
    img.save(os.path.join(ASSETS_DIR, "output.jpg"))


def resize_image(path, size=(512, 512)):
    ensure_assets_dir()
    img = Image.open(path)
    img = img.resize(size)
    img.save(os.path.join(ASSETS_DIR, "resized.jpg"))
