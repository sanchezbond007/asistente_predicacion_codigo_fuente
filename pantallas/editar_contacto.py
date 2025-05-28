from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os
import sys

# Asegura acceso a la raíz del proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from utils.traducciones import traducir as t  # ✅ IMPORTACIÓN CORRECTA

class PantallaEditarContacto(Screen):
    def __init__(self, idioma="es", volver_callback=None, contacto=None, **kwargs):
        super().__init__(**kwargs)
        self.idioma = idioma
        self.volver_callback = volver_callback
        self.contacto = contacto or {"nombre": "", "telefono": ""}

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text=t(self.idioma, "titulo"), font_size=24))

        # Campo para editar nombre
        layout.add_widget(Label(text=t(self.idioma, "nombre")))
        self.input_nombre = TextInput(text=self.contacto["nombre"])
        layout.add_widget(self.input_nombre)

        # Campo para editar teléfono
        layout.add_widget(Label(text=t(self.idioma, "telefono")))
        self.input_telefono = TextInput(text=self.contacto["telefono"])
        layout.add_widget(self.input_telefono)

        # Botón guardar
        btn_guardar = Button(text="💾 " + t(self.idioma, "guardar"), size_hint_y=None, height=50)
        btn_guardar.bind(on_press=self.guardar_contacto)
        layout.add_widget(btn_guardar)

        # Botón volver
        btn_volver = Button(text="← " + t(self.idioma, "volver"), size_hint_y=None, height=50)
        btn_volver.bind(on_press=self.volver)
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def guardar_contacto(self, instance):
        nombre = self.input_nombre.text
        telefono = self.input_telefono.text
        print(f"📌 Guardado: {nombre} - {telefono}")
        # Aquí puedes implementar guardado real si deseas

    def volver(self, instance):
        if self.volver_callback:
            self.volver_callback()