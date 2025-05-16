from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class PantallaMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)

        layout.add_widget(Label(
            text="===== Asistente de Predicación =====",
            font_size=60,
            size_hint_y=None,
            height=90
        ))

        opciones = [
            ("1. Ver sugerencias",       "sugerencias"),
            ("2. Buscar tema",           "buscar"),
            ("3. Ver por categoría",     "categorias"),
            ("4. Programar recordatorio","recordatorio"),
            ("5. Editar datos del contacto","editar_contacto"),
            ("6. Enviar resumen digital","contacto"),  # abre la pantalla de contacto
            ("7. Salir",                 "login"),
        ]

        for texto, destino in opciones:
            btn = Button(text=texto, font_size=60, height=90)
            btn.bind(on_press=lambda inst, dest=destino: self.cambiar_pantalla(dest))
            layout.add_widget(btn)

        # Botón Volver adicional
        btn_volver = Button(
            text="Volver",
            font_size=60,
            height=90,
            on_press=lambda *_: setattr(self.manager, "current", "login")
        )
        layout.add_widget(btn_volver)

        self.add_widget(layout)

    def cambiar_pantalla(self, nombre_pantalla):
        self.manager.current = nombre_pantalla