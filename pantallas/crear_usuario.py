# pantallas/crear_usuario.py

import os
import sys
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from utils.traducciones import traducir as t

class PantallaCrearUsuario(Screen):
    def __init__(self, volver_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.volver_callback = volver_callback

    def on_pre_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.nombre_input = TextInput(hint_text=t("nombre"), multiline=False)
        self.email_input = TextInput(hint_text=t("email"), multiline=False)

        layout.add_widget(Label(text=t("crear_usuario"), font_size='20sp'))
        layout.add_widget(self.nombre_input)
        layout.add_widget(self.email_input)

        btn_guardar = Button(text=t("guardar_usuario"))
        btn_guardar.bind(on_press=self.guardar_usuario)

        btn_volver = Button(text=t("volver_menu"))
        btn_volver.bind(on_press=lambda *a: self.volver_callback() if self.volver_callback else None)

        layout.add_widget(btn_guardar)
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def guardar_usuario(self, *args):
        nombre = self.nombre_input.text
        email = self.email_input.text
        print(f"Usuario guardado: {nombre}, {email}")