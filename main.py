from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from image_utils import apply_filter, resize_image
from generate import generate_image_from_prompt
# triggers

class EditorLayout(BoxLayout):
    def on_select_image(self, path):
        # Mostra immagine e abilita modifiche
        pass

    def on_apply_filter(self):
        # Applica filtro selezionato
        pass

    def on_generate_image(self, prompt):
        result = generate_image_from_prompt(prompt)
        # Mostra immagine generata
        pass


class PhotoshopAIApp(App):
    def build(self):
        return EditorLayout()


if __name__ == '__main__':
    PhotoshopAIApp().run()
