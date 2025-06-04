from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.snackbar import Snackbar
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.core.image import Image as CoreImage
from kivy.graphics.texture import Texture
from PIL import Image as PILImage
from io import BytesIO


class EditorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_path = None
        self.current_texture = None

    def load_image(self):
        content = FileChooserIconView(on_submit=self._on_image_selected)
        self._popup = Popup(title="Seleziona immagine",
                            content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def _on_image_selected(self, chooser, selection, *_):
        if selection:
            self.image_path = selection[0]
            self.ids.preview.source = self.image_path
            Snackbar(text="📂 Immagine caricata").open()
            self._popup.dismiss()

    def save_image(self):
        if not self.image_path:
            Snackbar(text="❗ Nessuna immagine da salvare").open()
            return
        chooser = FileChooserIconView(on_submit=self._on_save_selected)
        self._popup = Popup(title="Salva immagine",
                            content=chooser, size_hint=(0.9, 0.9))
        self._popup.open()

    def _on_save_selected(self, chooser, selection, *_):
        if selection:
            save_path = selection[0]
            img = PILImage.open(self.image_path)
            img.save(save_path)
            Snackbar(text="✅ Immagine salvata").open()
            self._popup.dismiss()

    def crop_image(self):
        Snackbar(text="✂️ Funzione di ritaglio non ancora implementata").open()

    def apply_filter(self):
        Snackbar(text="🎨 Applicazione filtro non ancora implementata").open()

    def apply_preset(self):
        Snackbar(text="🧩 Applicazione preset non ancora implementata").open()

    def generate_ai(self):
        prompt = self.ids.prompt_input.text
        if not prompt:
            Snackbar(text="❗ Inserisci un prompt").open()
            return
        Snackbar(text=f"🧠 Generazione AI da prompt: {prompt}").open()
