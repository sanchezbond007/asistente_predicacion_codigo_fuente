import os, sys
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from utils.traducciones import traducir


class PantallaCrearUsuario(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=30)

        self.lbl_nombre = Label(text=traducir("nombre"))
        self.txt_nombre = TextInput(multiline=False)

        self.lbl_email = Label(text=traducir("email"))
        self.txt_email = TextInput(multiline=False)

        self.btn_guardar = Button(text=traducir("guardar_usuario"))
        self.btn_guardar.bind(on_release=self.guardar_usuario)

        self.btn_volver = Button(text=traducir("volver_menu"))
        self.btn_volver.bind(on_release=lambda *_: setattr(self.manager, 'current', 'menu'))

        layout.add_widget(self.lbl_nombre)
        layout.add_widget(self.txt_nombre)
        layout.add_widget(self.lbl_email)
        layout.add_widget(self.txt_email)
        layout.add_widget(self.btn_guardar)
        layout.add_widget(self.btn_volver)

        self.add_widget(layout)

    def guardar_usuario(self, *args):
        nombre = self.txt_nombre.text.strip()
        email = self.txt_email.text.strip()
        print(f"Guardado: {nombre} - {email}")
        # Aquí puedes agregar lógica para almacenar los datos si deseas