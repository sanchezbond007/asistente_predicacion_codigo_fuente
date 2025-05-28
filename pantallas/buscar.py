# pantallas/buscar.py

import os
import sys
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from utils.traducciones import traducir as t

class PantallaBuscar(Screen):
    def __init__(self, volver_callback=None, **kwargs):
        self.volver_callback = volver_callback
        super().__init__(**kwargs)

    def on_pre_enter(self):
        self.clear_widgets()

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text=t("buscar"), font_size='20sp'))

        self.busqueda_input = TextInput(hint_text=t("buscar"), multiline=False)
        layout.add_widget(self.busqueda_input)

        btn_buscar = Button(text=t("buscar"))
        btn_buscar.bind(on_press=self.realizar_busqueda)
        layout.add_widget(btn_buscar)

        btn_volver = Button(text=t("volver"))
        btn_volver.bind(on_press=lambda *a: self.volver_callback() if self.volver_callback else None)
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def realizar_busqueda(self, *args):
        texto = self.busqueda_input.text
        print(f"Buscar: {texto}")