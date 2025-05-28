from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import os, sys

# Asegura acceso a la raíz del proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from utils.traducciones import traducir as t  # ✅ IMPORTACIÓN CORRECTA

class PantallaListaContactos(Screen):
    def __init__(self, idioma="es", volver_callback=None, editar_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.idioma = idioma
        self.volver_callback = volver_callback
        self.editar_callback = editar_callback

        layout_principal = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Título
        layout_principal.add_widget(Label(text=t(self.idioma, "titulo"), font_size=24))

        # Scroll con lista de contactos (ficticios como ejemplo)
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        contactos = [
            {"nombre": "Juan Pérez", "telefono": "123-456-7890"},
            {"nombre": "Ana López", "telefono": "321-654-0987"},
        ]

        for contacto in contactos:
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            box.add_widget(Label(text=f"{contacto['nombre']} - {contacto['telefono']}", size_hint_x=0.8))
            btn_editar = Button(text="✎", size_hint_x=0.2)
            btn_editar.bind(on_press=lambda x, c=contacto: self.editar(c))
            box.add_widget(btn_editar)
            grid.add_widget(box)

        scroll.add_widget(grid)
        layout_principal.add_widget(scroll)

        # Botón volver
        btn_volver = Button(text="← " + t(self.idioma, "volver"), size_hint=(1, 0.15))
        btn_volver.bind(on_press=self.volver)
        layout_principal.add_widget(btn_volver)

        self.add_widget(layout_principal)

    def volver(self, instance):
        if self.volver_callback:
            self.volver_callback()

    def editar(self, contacto):
        if self.editar_callback:
            self.editar_callback(contacto)