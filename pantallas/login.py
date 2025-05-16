from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup

class PantallaLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        scroll = ScrollView(size_hint=(1, 1))
        layout = BoxLayout(orientation='vertical', padding=40, spacing=25, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Título
        layout.add_widget(Label(text="Asistente de Predicación", font_size=70, size_hint_y=None, height=100))

        # Usuario
        layout.add_widget(Label(text="Usuario:", font_size=60, size_hint_y=None, height=90))
        self.usuario_input = TextInput(size_hint_y=None, height=90, font_size=60)
        layout.add_widget(self.usuario_input)

        # PIN
        layout.add_widget(Label(text="PIN:", font_size=60, size_hint_y=None, height=90))
        self.pin_input = TextInput(password=True, size_hint_y=None, height=90, font_size=60)
        layout.add_widget(self.pin_input)

        # CheckBox Recordarme
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=90)
        self.recordarme_checkbox = CheckBox(active=True, color=[1, 1, 0, 1])  # Siempre amarillo
        checkbox_layout.add_widget(self.recordarme_checkbox)
        checkbox_layout.add_widget(Label(text="Recordarme", font_size=60))
        layout.add_widget(checkbox_layout)

        # Entrar
        btn_entrar = Button(text="Entrar", size_hint_y=None, height=90, font_size=60)
        btn_entrar.bind(on_release=self.verificar_credenciales)
        layout.add_widget(btn_entrar)

        # ¿Olvidaste tu PIN?
        btn_olvido = Button(text="¿Olvidaste tu PIN?", size_hint_y=None, height=90, font_size=60)
        btn_olvido.bind(on_release=self.olvidaste_pin)
        layout.add_widget(btn_olvido)

        scroll.add_widget(layout)
        self.add_widget(scroll)

        # Si está activo Recordarme, rellenar campos por defecto
        if self.recordarme_checkbox.active:
            self.usuario_input.text = "admin"
            self.pin_input.text = "1234"

    def verificar_credenciales(self, instance):
        usuario = self.usuario_input.text.strip()
        pin = self.pin_input.text.strip()
        if usuario.lower() == "admin" and pin == "1234":
            self.manager.current = "menu"
        else:
            self.mostrar_error("Usuario o PIN incorrecto.")

    def mostrar_error(self, mensaje):
        popup = Popup(title="Error de acceso",
                      content=Label(text=mensaje, font_size=40),
                      size_hint=(None, None), size=(500, 300))
        popup.open()

    def olvidaste_pin(self, instance):
        popup = Popup(title="Recuperación de PIN",
                      content=Label(text="Contacta a soporte para restablecer tu PIN.", font_size=40),
                      size_hint=(None, None), size=(600, 300))
        popup.open()