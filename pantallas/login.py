from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
import os
import sys

# Fondo blanco
Window.clearcolor = (1, 1, 1, 1)

# Asegura acceso a la raíz del proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from utils.traducciones import traducir as t

class PantallaLogin(Screen):
    def __init__(self, idioma_callback=None, continuar_callback=None, idioma='en', **kwargs):
        self.idioma = idioma
        self.idioma_callback = idioma_callback
        self.continuar_callback = continuar_callback
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=40)
        self.layout.add_widget(Widget(size_hint_y=2))  # Espaciador superior

        self.titulo = Label(
            text='',
            font_size=60,
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=120,
            halign='center',
            valign='middle'
        )
        self.titulo.bind(size=self.titulo.setter('text_size'))
        self.layout.add_widget(self.titulo)

        self.lbl_select = Label(
            text='',
            font_size=60,
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=80
        )
        self.layout.add_widget(self.lbl_select)

        # Botones de idioma
        botones_idioma = BoxLayout(size_hint_y=None, height=80, spacing=30)
        botones_idioma.add_widget(Button(
            text="Español",
            font_size=60,
            on_press=lambda x: self.cambiar_idioma("es")
        ))
        botones_idioma.add_widget(Button(
            text="English",
            font_size=60,
            on_press=lambda x: self.cambiar_idioma("en")
        ))
        self.layout.add_widget(botones_idioma)

        # Botones principales
        self.btn_login = Button(text='', font_size=60, size_hint_y=None, height=90,
                                on_press=lambda x: self.continuar_callback() if self.continuar_callback else None)
        self.btn_crear = Button(text='', font_size=60, size_hint_y=None, height=90)
        self.btn_actualizar = Button(text='', font_size=60, size_hint_y=None, height=90)

        self.layout.add_widget(self.btn_login)
        self.layout.add_widget(self.btn_crear)
        self.layout.add_widget(self.btn_actualizar)

        self.layout.add_widget(Widget(size_hint_y=3))  # Espaciador inferior

        self.add_widget(self.layout)
        self.actualizar_textos()

    def cambiar_idioma(self, nuevo_idioma):
        self.idioma = nuevo_idioma
        if self.idioma_callback:
            self.idioma_callback(nuevo_idioma)
        self.actualizar_textos()

    def actualizar_textos(self):
        self.titulo.text = t(self.idioma, "titulo")
        self.lbl_select.text = t(self.idioma, "seleccionar_idioma")
        self.btn_login.text = t(self.idioma, "login")
        self.btn_crear.text = t(self.idioma, "crear_usuario")
        self.btn_actualizar.text = t(self.idioma, "actualizar")