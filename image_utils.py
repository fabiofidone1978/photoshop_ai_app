from PIL import Image, ImageFilter


def apply_filter(path, filter_type="BLUR"):
    img = Image.open(path)
    if filter_type == "BLUR":
        img = img.filter(ImageFilter.BLUR)
    elif filter_type == "CONTOUR":
        img = img.filter(ImageFilter.CONTOUR)
    img.save("assets/output.jpg")


def resize_image(path, size=(512, 512)):
    img = Image.open(path)
    img = img.resize(size)
    img.save("assets/resized.jpg")
