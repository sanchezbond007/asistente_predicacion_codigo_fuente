from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import plyer

class PantallaResumenDigital(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.add_widget(layout)

        layout.add_widget(Label(
            text="Resumen Digital",
            font_size=60,
            size_hint_y=None,
            height=100
        ))

        # Aquí podrías cargar un resumen en texto o lista de links
        self.lbl_contenido = Label(
            text="Aquí aparecerá el resumen de la visita con enlaces.",
            font_size=50,
            size_hint_y=None,
            halign='left',
            valign='top',
            text_size=(self.width - 60, None)
        )
        self.lbl_contenido.bind(
            width=lambda inst, w: setattr(inst, 'text_size', (w - 60, None))
        )
        layout.add_widget(self.lbl_contenido)

        btn_generar = Button(
            text="Generar resumen",
            font_size=60,
            size_hint_y=None,
            height=100
        )
        btn_generar.bind(on_release=self.generar_resumen)
        layout.add_widget(btn_generar)

        btn_volver = Button(
            text="Volver",
            font_size=60,
            size_hint_y=None,
            height=100
        )
        btn_volver.bind(on_release=lambda *_: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_volver)

    def generar_resumen(self, *args):
        # Aquí pones la lógica para componer el texto y los links
        resumen = (
            "Resumen de la visita:\n\n"
            "- Tema 1: enlace1\n"
            "- Tema 2: enlace2\n"
        )
        self.lbl_contenido.text = resumen

        # Opcional: copiar al portapapeles o notificar
        plyer.notification.notify(title="Resumen creado", message="Ya puedes enviarlo")