from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import os
import sys

# Asegura que vea la carpeta raíz
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from utils.temas_handler2 import cargar_temas_profundos  # Este es tu archivo separado

class PantallaTemasProfundos(Screen):
    def __init__(self, volver_callback=None, idioma='es', **kwargs):
        super().__init__(**kwargs)
        self.volver_callback = volver_callback
        self.idioma = idioma
        self.build()

    def build(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical')
        scroll = ScrollView()
        inner_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        inner_layout.bind(minimum_height=inner_layout.setter('height'))

        temas = cargar_temas_profundos()

        for tema in temas:
            titulo = tema.get('titulo', {}).get(self.idioma, '')
            btn = Button(text=titulo, size_hint_y=None, height=60)
            btn.bind(on_release=lambda btn, t=tema: self.mostrar_tema(t))
            inner_layout.add_widget(btn)

        scroll.add_widget(inner_layout)
        layout.add_widget(scroll)

        btn_volver = Button(text='⬅ Volver', size_hint_y=None, height=50)
        btn_volver.bind(on_release=lambda _: self.volver_callback())
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def mostrar_tema(self, tema):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text=tema['titulo'][self.idioma], font_size=20, size_hint_y=None, height=50))
        layout.add_widget(Label(text=tema['contenido'][self.idioma], size_hint_y=None, height=300))

        btn_volver = Button(text='⬅ Volver a temas profundos', size_hint_y=None, height=50)
        btn_volver.bind(on_release=lambda _: self.build())
        layout.add_widget(btn_volver)

        self.add_widget(layout)