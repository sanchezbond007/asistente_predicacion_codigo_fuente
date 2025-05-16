from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import datetime
from kivy.clock import Clock

class PantallaRecordatorio(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.add_widget(layout)

        layout.add_widget(Label(
            text="Programar Recordatorio",
            font_size=60,
            size_hint_y=None,
            height=100
        ))

        layout.add_widget(Label(
            text="Mensaje:",
            font_size=60,
            size_hint_y=None,
            height=60
        ))
        self.input_msg = TextInput(
            font_size=50,
            size_hint_y=None,
            height=100
        )
        layout.add_widget(self.input_msg)

        layout.add_widget(Label(
            text="Minutos para recordarme:",
            font_size=60,
            size_hint_y=None,
            height=60
        ))
        self.input_min = TextInput(
            font_size=50,
            size_hint_y=None,
            height=100,
            input_filter='int'
        )
        layout.add_widget(self.input_min)

        btn_set = Button(
            text="Programar",
            font_size=60,
            size_hint_y=None,
            height=100
        )
        btn_set.bind(on_release=self.programar)
        layout.add_widget(btn_set)

        btn_volver = Button(
            text="Volver",
            font_size=60,
            size_hint_y=None,
            height=100
        )
        btn_volver.bind(on_release=lambda *_: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_volver)

    def programar(self, *args):
        mins_text = self.input_min.text.strip()
        if not mins_text.isdigit():
            return
        minutos = int(mins_text)
        mensaje = self.input_msg.text.strip() or "¡Es hora de tu recordatorio!"

        # Programa con Clock un recordatorio tras 'minutos'
        Clock.schedule_once(lambda dt: self._mostrar_recordatorio(mensaje),
                            minutos * 60)
        self.input_msg.text = ""
        self.input_min.text = ""
        # Podrías añadir una notificación de confirmación aquí

    def _mostrar_recordatorio(self, mensaje):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label
        popup = Popup(title="Recordatorio",
                      content=Label(text=mensaje, font_size=50),
                      size_hint=(0.8, 0.4))
        popup.open()