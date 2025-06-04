from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import platform
from editor import EditorLayout


class PhotoshopAIApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Light"
        self.title = "Photoshop AI"
        if platform in ["win", "linux", "macosx"]:
            Window.size = (1024, 720)
        return EditorLayout()

    def toggle_theme(self):
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )


if __name__ == "__main__":
    PhotoshopAIApp().run()
