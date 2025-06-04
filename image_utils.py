from PIL import Image, ImageEnhance, ImageFilter


def crop_image(path, crop_box=(100, 100, 400, 400)):
    img = Image.open(path)
    cropped = img.crop(crop_box)
    output_path = "assets/output.jpg"
    cropped.save(output_path)
    return output_path


def apply_filter(path, filter_type="BLUR"):
    img = Image.open(path)
    if filter_type == "BLUR":
        img = img.filter(ImageFilter.BLUR)
    elif filter_type == "CONTOUR":
        img = img.filter(ImageFilter.CONTOUR)
    elif filter_type == "DETAIL":
        img = img.filter(ImageFilter.DETAIL)
    else:
        raise ValueError("Filtro sconosciuto")
    output_path = "assets/output.jpg"
    img.save(output_path)
    return output_path


def apply_preset(path, preset_name="contrast"):
    img = Image.open(path)
    if preset_name == "contrast":
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.8)
    elif preset_name == "brightness":
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.5)
    else:
        raise ValueError("Preset sconosciuto")
    output_path = "assets/output.jpg"
    img.save(output_path)
    return output_path
