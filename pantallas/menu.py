from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import os, sys

# Asegura que el proyecto vea la carpeta raíz correctamente
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from utils.traducciones import traducir as t  # ✅ correcto

class PantallaMenu(Screen):
    def __init__(self, idioma="es", navegar_callback=None, volver_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.idioma = idioma
        self.navegar_callback = navegar_callback
        self.volver_callback = volver_callback

        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # Título principal
        layout.add_widget(Label(text=t(self.idioma, "titulo"), font_size=28, size_hint_y=None, height=50))

        # Botones de navegación
        botones = [
            ("login", "sugerencias"),
            ("crear_usuario", "temas_profundos"),
            ("actualizar", "buscar"),
        ]

        for clave, destino in botones:
            btn = Button(text=t(self.idioma, clave), size_hint_y=None, height=50)
            btn.bind(on_press=lambda instance, d=destino: self.navegar(d))
            layout.add_widget(btn)

        # Botón volver
        btn_volver = Button(text="← " + t(self.idioma, "volver"), size_hint_y=None, height=50)
        btn_volver.bind(on_press=self.volver)
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def navegar(self, destino):
        if self.navegar_callback:
            self.navegar_callback(destino)

    def volver(self, instance):
        if self.volver_callback:
            self.volver_callback()