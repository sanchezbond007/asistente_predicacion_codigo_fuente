from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class PantallaBuscar(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = FloatLayout()

        # Campo de texto aún más abajo
        self.entrada = TextInput(
            hint_text='Escribe para buscar...',
            size_hint=(0.9, None),
            height=90,
            font_size=60,
            pos_hint={'x': 0.05, 'top': 0.58}
        )

        # Botón más abajo aún
        btn_buscar = Button(
            text='Buscar',
            size_hint=(0.9, None),
            height=90,
            font_size=60,
            pos_hint={'x': 0.05, 'top': 0.44}
        )
        btn_buscar.bind(on_press=self.buscar_tema)

        # Scroll para resultados debajo
        self.resultados = GridLayout(cols=1, size_hint_y=None, spacing=10, padding=10)
        self.resultados.bind(minimum_height=self.resultados.setter('height'))

        scroll = ScrollView(
            size_hint=(0.9, 0.35),
            pos_hint={'x': 0.05, 'y': 0.02}
        )
        scroll.add_widget(self.resultados)

        # Añadir todo
        root.add_widget(self.entrada)
        root.add_widget(btn_buscar)
        root.add_widget(scroll)
        self.add_widget(root)

    def buscar_tema(self, instance):
        texto = self.entrada.text.lower()
        self.resultados.clear_widgets()

        temas = ["Fe", "Esperanza", "Jesús", "Reino de Dios", "Amor"]
        for tema in temas:
            if texto in tema.lower():
                self.resultados.add_widget(Label(
                    text=tema,
                    size_hint_y=None,
                    height=60,
                    font_size=50
                ))