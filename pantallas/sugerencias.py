import os
import sys
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.storage.jsonstore import JsonStore

# Asegura que el proyecto vea la carpeta raíz
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from utils.temas_handler import obtener_sugerencias, obtener_detalle_tema

class PantallaSugerencias(Screen):
    def __init__(self, volver_callback=None, idioma='es', **kwargs):
        super().__init__(**kwargs)
        self.volver_callback = volver_callback
        self.idioma = idioma
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.add_widget(self.layout)
        self.mostrar_sugerencias()

    def mostrar_sugerencias(self):
        self.layout.clear_widgets()
        titulo = Label(text='Sugerencias Bíblicas' if self.idioma == 'es' else 'Bible Suggestions', font_size='20sp', size_hint=(1, 0.1))
        self.layout.add_widget(titulo)

        temas = obtener_sugerencias(idioma=self.idioma)
        for tema in temas:
            btn = Button(text=tema['titulo'], size_hint=(1, None), height=50)
            btn.bind(on_release=lambda btn, t=tema: self.mostrar_detalle(t))
            self.layout.add_widget(btn)

        if self.volver_callback:
            btn_volver = Button(text='Volver' if self.idioma == 'es' else 'Back', size_hint=(1, 0.1))
            btn_volver.bind(on_release=lambda instance: self.volver_callback())
            self.layout.add_widget(btn_volver)

    def mostrar_detalle(self, tema):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text=tema['titulo'], font_size='18sp', size_hint=(1, 0.1)))
        self.layout.add_widget(Label(text=tema['respuesta'], font_size='16sp', size_hint=(1, 0.7)))

        btn_volver = Button(text='Volver' if self.idioma == 'es' else 'Back', size_hint=(1, 0.1))
        btn_volver.bind(on_release=lambda instance: self.mostrar_sugerencias())
        self.layout.add_widget(btn_volver)