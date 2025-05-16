# pantallas/buscar.py

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class PantallaBuscar(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.input = TextInput(hint_text="Escribe para buscar…", size_hint_y=None, height=60)
        btn = Button(text="Buscar", size_hint_y=None, height=60)
        btn.bind(on_release=lambda *_: self._realizar_busqueda(self.input.text))
        self.result_lbl = Label(text="", valign='top')

        layout.add_widget(self.input)
        layout.add_widget(btn)
        layout.add_widget(self.result_lbl)
        self.add_widget(layout)

    def _realizar_busqueda(self, texto_buscar: str):
        # Aquí iría tu lógica real de búsqueda…
        # Por ahora simulamos una lista de resultados:
        resultados = ["Tema A", "Tema B", "Tema C"] if texto_buscar else []
        self.result_lbl.text = (
            "\n".join(resultados) if resultados else "Por favor escribe algo."
        )

        # Registra el evento en el historial global
        App.get_running_app().registrar_evento(
            f"Búsqueda: '{texto_buscar}' → {len(resultados)} resultados"
        )