import requests


def remove_background(image_path, output_path="assets/nobg.png"):
    # Usa remove.bg API (devi avere una chiave API)
    with open(image_path, 'rb') as img_file:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': img_file},
            data={'size': 'auto'},
            headers={'X-Api-Key': 'INSERISCI_LA_TUA_API_KEY'}
        )
    if response.status_code == requests.codes.ok:
        with open(output_path, 'wb') as out:
            out.write(response.content)
        return output_path
    else:
        print("Errore remove.bg:", response.status_code, response.text)
        return ""


def beautify_face(image_path, output_path="assets/beautify.jpg"):
    # Placeholder per futura integrazione (es. Face++ o API proprie)
    print("Funzione beautify_face in sviluppo.")
    return image_path
