from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
import random
from temas_handler import cargar_todos_los_temas

class PantallaSugerencias(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout_principal = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.scroll = ScrollView(size_hint=(1, 1))
        self.box = BoxLayout(orientation="vertical", spacing=10, size_hint_y=None)
        self.box.bind(minimum_height=self.box.setter('height'))
        self.scroll.add_widget(self.box)

        self.layout_principal.add_widget(self.scroll)

        boton_volver = Button(text="Volver", size_hint=(1, None), height=90, font_size=60)
        boton_volver.bind(on_press=lambda x: self.manager.current == "menu")
        self.layout_principal.add_widget(boton_volver)

        self.add_widget(self.layout_principal)
        self.mostrar_sugerencias()

    def mostrar_sugerencias(self):
        temas = cargar_todos_los_temas()
        if not temas:
            self.box.add_widget(Label(text="(No hay temas disponibles)", font_size=40, size_hint_y=None, height=100))
            return

        sugerencias = random.sample(temas, min(10, len(temas)))
        for tema in sugerencias:
            btn = Button(text=tema.get("titulo", "(Sin título)"), size_hint_y=None, height=100, font_size=40)
            self.box.add_widget(btn)