from PIL import Image
import zipfile
import json
import os


def export_to_pdf(path, output="assets/export.pdf"):
    img = Image.open(path).convert("RGB")
    img.save(output, "PDF", resolution=100.0)


def export_project_zip(image_path, metadata, output="assets/project_export.zip"):
    with zipfile.ZipFile(output, 'w') as zipf:
        zipf.write(image_path, arcname=os.path.basename(image_path))
        zipf.writestr("metadata.json", json.dumps(metadata, indent=2))


def save_preset(params, output="assets/preset.json"):
    with open(output, "w") as f:
        json.dump(params, f)


def load_preset(input_path="assets/preset.json"):
    with open(input_path, "r") as f:
        return json.load(f)


def save_project(image_path, settings, output="assets/project.aepj"):
    with open(output, "w") as f:
        json.dump({
            "image": image_path,
            "settings": settings
        }, f)


def load_project(project_path="assets/project.aepj"):
    with open(project_path, "r") as f:
        return json.load(f)
