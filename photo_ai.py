import os
import requests
from PIL import Image, ImageEnhance, ImageOps
from pathlib import Path
from utils import upload_to_aruba


REPLICATE_API_URL = "https://api.replicate.com/v1/predictions"
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
HEADERS = {
    "Authorization": f"Token {REPLICATE_API_TOKEN}",
    "Content-Type": "application/json"
}


def _call_replicate_model(model: str, input_data: dict) -> str:
    response = requests.post(
        REPLICATE_API_URL,
        json={
            "version": model,
            "input": input_data
        },
        headers=HEADERS
    )
    response.raise_for_status()
    prediction = response.json()
    return prediction["urls"]["get"]


def style_transfer(image_path: str, style: str = "wave") -> str:
    url = upload_to_aruba(image_path)
    output = _call_replicate_model(
        "9e6a365b264d44495c7299e8c8231f794e2e6c8f52c56b2ce7dc2160bfe90f3e",
        {"image": url, "style": style}
    )
    return output


def super_resolution(image_path: str, scale: int = 2) -> str:
    url = upload_to_aruba(image_path)
    output = _call_replicate_model(
        "4c14f9385509f2d20bce5786f6c229aee299bdfbaa6a5aee0c71cd1b5a0f146b",
        {"image": url, "scale": scale}
    )
    return output


def object_removal(image_path: str) -> str:
    url = upload_to_aruba(image_path)
    output = _call_replicate_model(
        "24e27152f27c4042a6db46a7879db8c0ba4724ec35f54ec379611e46c6f17d61",
        {"image": url}
    )
    return output


def noise_reduction(image_path: str) -> str:
    url = upload_to_aruba(image_path)
    output = _call_replicate_model(
        "9a5a84860ba3feacb3a8b7f8a40b65a39d3df94c49df883f6cd1cb30c3df9873",
        {"image": url}
    )
    return output


def adjust_rgb_curves(image_path: str, red=1.0, green=1.0, blue=1.0) -> str:
    img = Image.open(image_path).convert("RGB")
    r, g, b = img.split()

    r = r.point(lambda i: min(255, int(i * red)))
    g = g.point(lambda i: min(255, int(i * green)))
    b = b.point(lambda i: min(255, int(i * blue)))

    new_img = Image.merge("RGB", (r, g, b))
    output_path = str(Path(image_path).with_name(
        "rgb_" + Path(image_path).name))
    new_img.save(output_path)
    return output_path


def adjust_hsl(image_path: str, hue=0, saturation=1.0, lightness=1.0) -> str:
    img = Image.open(image_path).convert("RGB")
    img = ImageEnhance.Color(img).enhance(saturation)
    img = ImageEnhance.Brightness(img).enhance(lightness)
    output_path = str(Path(image_path).with_name(
        "hsl_" + Path(image_path).name))
    img.save(output_path)
    return output_path


def crop_image(image_path: str, left, top, right, bottom) -> str:
    img = Image.open(image_path)
    cropped = img.crop((left, top, right, bottom))
    output_path = str(Path(image_path).with_name(
        "cropped_" + Path(image_path).name))
    cropped.save(output_path)
    return output_path


def apply_preset(image_path: str, preset_name: str) -> str:
    img = Image.open(image_path)
    if preset_name == "bw":
        img = ImageOps.grayscale(img)
    elif preset_name == "warm":
        img = ImageEnhance.Color(img).enhance(1.5)
    output_path = str(Path(image_path).with_name(
        f"{preset_name}_" + Path(image_path).name))
    img.save(output_path)
    return output_path


def export_pdf(image_path: str) -> str:
    img = Image.open(image_path)
    output_path = str(Path(image_path).with_suffix(".pdf"))
    img.save(output_path, "PDF")
    return output_path


def export_zip(image_paths: list, output_zip: str) -> str:
    import zipfile
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for path in image_paths:
            zipf.write(path, arcname=Path(path).name)
    return output_zip


def export_psd(image_path: str) -> str:
    # Simulazione base: esporta come TIFF (più compatibile offline)
    output_path = str(Path(image_path).with_suffix(".tiff"))
    Image.open(image_path).save(output_path)
    return output_path


def save_project(image_path: str, meta: dict) -> str:
    project_dir = Path(image_path).with_suffix(".project")
    project_dir.mkdir(exist_ok=True)
    img_output = project_dir / Path(image_path).name
    meta_output = project_dir / "meta.json"

    Image.open(image_path).save(img_output)
    with open(meta_output, "w") as f:
        import json
        json.dump(meta, f, indent=2)
    return str(project_dir)


def load_project(project_path: str) -> tuple:
    from PIL import Image
    import json
    img_file = next(Path(project_path).glob("*.png"))
    meta_file = Path(project_path) / "meta.json"
    with open(meta_file, "r") as f:
        meta = json.load(f)
    return str(img_file), meta


def dehaze(image_path: str) -> str:
    img = Image.open(image_path).convert("RGB")
    enhancer = ImageEnhance.Contrast(img)
    enhanced = enhancer.enhance(1.3)
    output_path = str(Path(image_path).with_name(
        "dehazed_" + Path(image_path).name))
    enhanced.save(output_path)
    return output_path
