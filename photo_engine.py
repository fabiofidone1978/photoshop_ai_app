from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import numpy as np


def apply_rgb_curves(img, r_curve, g_curve, b_curve):
    r, g, b = img.split()
    r = r.point(r_curve)
    g = g.point(g_curve)
    b = b.point(b_curve)
    return Image.merge("RGB", (r, g, b))


def adjust_hsl(img, h_shift=0, s_mult=1.0, l_mult=1.0):
    img = img.convert("HSV")
    h, s, v = img.split()
    h = h.point(lambda p: (p + h_shift) % 255)
    s = s.point(lambda p: min(255, int(p * s_mult)))
    v = v.point(lambda p: min(255, int(p * l_mult)))
    return Image.merge("HSV", (h, s, v)).convert("RGB")


def dehaze(img):
    return img.filter(ImageFilter.DETAIL)


def reduce_noise(img):
    return img.filter(ImageFilter.MedianFilter(size=3))


def crop_image(img, left, top, right, bottom):
    return img.crop((left, top, right, bottom))


def process_image(path, brightness=1.0, contrast=1.0, saturation=1.0, sharpness=1.0, clarity=1.0):
    img = Image.open(path)
    img = ImageEnhance.Brightness(img).enhance(brightness)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Color(img).enhance(saturation)
    img = ImageEnhance.Sharpness(img).enhance(sharpness)
    img = dehaze(img)
    img = reduce_noise(img)
    output_path = "assets/edited.jpg"
    img.save(output_path)
    return output_path
