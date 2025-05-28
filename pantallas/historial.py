from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import os
import sys

# Asegura que el proyecto vea la carpeta raíz correctamente
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from utils.traducciones import traducir as t  # ✅ CORRECTO

class PantallaHistorial(Screen):
    def __init__(self, idioma="es", volver_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.idioma = idioma
        self.volver_callback = volver_callback

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text=t(self.idioma, "titulo"), font_size=20))

        # Aquí podrías agregar más contenido del historial si lo deseas

        btn_volver = Button(text="← Volver", size_hint=(1, 0.2))
        btn_volver.bind(on_press=self.volver)
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def volver(self, instance):
        if self.volver_callback:
            self.volver_callback()