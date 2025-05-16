from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button

# Simulación de historial (luego se puede cargar desde archivo real)
HISTORIAL_EJEMPLO = [
    "Tema: ¿Quién es Dios? - Juan 17:3",
    "Tema: ¿Qué esperanza hay para los muertos? - Juan 5:28, 29",
    "Tema: ¿Por qué debemos orar? - Mateo 6:9-13",
    "Tema: ¿Existe el infierno? - Eclesiastés 9:5",
    "Tema: ¿Qué es el Reino de Dios? - Daniel 2:44",
    "Tema: ¿Quién es Jesucristo? - Mateo 16:16",
    "Tema: ¿Qué enseña la Biblia sobre el sufrimiento? - Job 14:1, 2",
    "Tema: ¿Qué es la fe? - Hebreos 11:1",
    "Tema: ¿Cómo vivir en paz? - Romanos 12:18",
    "Tema: ¿Qué es la vida eterna? - Juan 17:3"
]

class PantallaHistorial(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout_principal = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.scroll = ScrollView(size_hint=(1, 0.85))
        self.caja_texto = BoxLayout(orientation='vertical', size_hint_y=None)
        self.caja_texto.bind(minimum_height=self.caja_texto.setter('height'))

        self.scroll.add_widget(self.caja_texto)
        self.layout_principal.add_widget(self.scroll)

        self.boton_volver = Button(text="Volver al menú", size_hint=(1, 0.15))
        self.boton_volver.bind(on_release=self.volver_menu)
        self.layout_principal.add_widget(self.boton_volver)

        self.add_widget(self.layout_principal)

    def on_pre_enter(self):
        self.caja_texto.clear_widgets()
        for linea in HISTORIAL_EJEMPLO:
            self.caja_texto.add_widget(Label(text=linea, size_hint_y=None, height=40))

    def volver_menu(self, instance):
        self.manager.current = "menu"