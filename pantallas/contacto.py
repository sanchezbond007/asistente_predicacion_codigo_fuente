from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import os
import sys

# Asegura acceso a la raíz del proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from utils.traducciones import traducir as t

class PantallaContacto(Screen):  # ✅ ESTA CLASE DEBE ESTAR PRESENTE
    def __init__(self, idioma="es", volver_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.idioma = idioma
        self.volver_callback = volver_callback

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text=t(self.idioma, "titulo"), font_size=24))

        layout.add_widget(Label(
            text="info@ejemplo.com\nTel: +1 234 567 890",
            font_size=16
        ))

        btn_volver = Button(text="← " + t(self.idioma, "volver"), size_hint=(1, 0.15))
        btn_volver.bind(on_press=self.volver)
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def volver(self, instance):
        if self.volver_callback:
            self.volver_callback()