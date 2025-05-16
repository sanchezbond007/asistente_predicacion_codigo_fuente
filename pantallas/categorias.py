# pantallas/categorias.py

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class PantallaCategorias(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout principal
        layout = BoxLayout(
            orientation='vertical',
            spacing=10,
            padding=20
        )

        # Título
        layout.add_widget(Label(
            text="Selecciona una categoría",
            font_size=60,
            size_hint_y=None,
            height=90
        ))

        # Botones de categorías
        categorias = [
            ("Doctrina", "categorias_doctrina"),
            ("Esperanza", "categorias_esperanza"),
            ("Conducta", "categorias_conducta"),
            ("Debates",   "debate")
        ]
        for texto, destino in categorias:
            btn = Button(
                text=texto,
                font_size=60,
                size_hint_y=None,
                height=90
            )
            btn.bind(on_release=lambda inst, d=destino: setattr(self.manager, 'current', d))
            layout.add_widget(btn)

        # --- AQUÍ AGREGAMOS EL BOTÓN VOLVER ---
        btn_volver = Button(
            text="Volver",
            font_size=60,
            size_hint_y=None,
            height=90
        )
        # Cuando lo pulses, volvemos al menú principal
        btn_volver.bind(on_release=lambda *_: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_volver)

        self.add_widget(layout)