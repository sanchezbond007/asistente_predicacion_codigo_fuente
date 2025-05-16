# pantallas/debate.py

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

from datos.debate_handler import cargar_temas_debate

class PantallaDebate(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.add_widget(self.layout)

    def on_pre_enter(self):
        Clock.schedule_once(lambda dt: self._mostrar_temas(), 0)

    def _mostrar_temas(self):
        self.layout.clear_widgets()
        temas = cargar_temas_debate()
        if not temas:
            self.layout.add_widget(Label(text="No hay temas de debate.", font_size=24))
            return

        scroll = ScrollView()
        cont = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        cont.bind(minimum_height=cont.setter('height'))

        for tema in temas:
            btn = Button(text=tema['titulo'], size_hint_y=None, height=60)
            btn.bind(on_release=lambda inst, t=tema: self._mostrar_detalle(t))
            cont.add_widget(btn)

        scroll.add_widget(cont)
        self.layout.add_widget(scroll)

    def _mostrar_detalle(self, tema):
        # Registra en historial
        App.get_running_app().registrar_evento(f"Debate consultado: {tema['titulo']}")

        # Construye el popup
        content = BoxLayout(orientation='vertical', padding=20, spacing=20)
        content.add_widget(Label(text=f"[b]{tema['titulo']}[/b]", markup=True))
        content.add_widget(Label(text=tema.get('respuesta','')))
        for sub in tema.get('profundizar', []):
            content.add_widget(Label(text=f"{sub['subtitulo']}: {sub['texto']}"))

        btn = Button(text="Cerrar", size_hint_y=None, height=50)
        content.add_widget(btn)

        popup = Popup(title="Detalle de Debate",
                      content=ScrollView(size_hint=(1,1),  
                                         do_scroll_x=False, do_scroll_y=True,
                                         children=[content]),
                      size_hint=(0.9, 0.8),
                      auto_dismiss=False)
        btn.bind(on_release=popup.dismiss)
        popup.open()