from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from image_utils import apply_filter, resize_image
from generate import generate_image_from_prompt

# triggers

class EditorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_path = None

    def on_select_image(self, path=None):
        """Load the selected image and show it in the preview."""
        if path:
            self.image_path = path
            self.ids.preview.source = path

    def on_apply_filter(self):
        """Apply a simple filter to the loaded image."""
        if self.image_path:
            apply_filter(self.image_path)
            self.ids.preview.source = "assets/output.jpg"

    def on_generate_image(self, prompt):
        """Generate a new image from the provided prompt."""
        if not prompt:
            return
        result = generate_image_from_prompt(prompt)
        self.ids.preview.source = result


class PhotoshopAIApp(App):
    def build(self):
        Builder.load_file("editor.kv")
        return EditorLayout()


if __name__ == '__main__':
    PhotoshopAIApp().run()
