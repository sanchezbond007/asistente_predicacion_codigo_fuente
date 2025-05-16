from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
import json
import os

RUTA_CONTACTOS = "datos/contactos.json"

class PantallaListaContactos(Screen):  # Revertido a como lo tenías originalmente
    indice_contacto = NumericProperty(-1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", spacing=15, padding=30)
        self.add_widget(self.layout)

        self.layout.add_widget(Label(
            text="Editar contacto seleccionado",
            font_size=60,
            height=90,
            size_hint_y=None
        ))

        # Campo: Nombre
        self.layout.add_widget(Label(text="Nombre del interesado", font_size=60, height=90, size_hint_y=None))
        self.input_nombre = TextInput(multiline=False, font_size=40, height=60, size_hint_y=None)
        self.layout.add_widget(self.input_nombre)

        # Campo: Correo
        self.layout.add_widget(Label(text="Correo del interesado", font_size=60, height=90, size_hint_y=None))
        self.input_correo = TextInput(multiline=False, font_size=40, height=60, size_hint_y=None)
        self.layout.add_widget(self.input_correo)

        # Campo: Teléfono
        self.layout.add_widget(Label(text="Teléfono del interesado", font_size=60, height=90, size_hint_y=None))
        self.input_telefono = TextInput(multiline=False, font_size=40, height=60, size_hint_y=None)
        self.layout.add_widget(self.input_telefono)

        # Campo: Testigo
        self.layout.add_widget(Label(text="Nombre del Testigo de Jehová", font_size=60, height=90, size_hint_y=None))
        self.input_testigo = TextInput(multiline=False, font_size=40, height=60, size_hint_y=None)
        self.layout.add_widget(self.input_testigo)

        # Botones
        botones = BoxLayout(size_hint=(1, None), height=90, spacing=10)
        btn_guardar = Button(text="Guardar", font_size=60, on_press=self.guardar_contacto)
        btn_volver = Button(text="Volver", font_size=60, on_press=self.volver_menu)
        botones.add_widget(btn_guardar)
        botones.add_widget(btn_volver)
        self.layout.add_widget(botones)

    def on_pre_enter(self):
        if os.path.exists(RUTA_CONTACTOS):
            with open(RUTA_CONTACTOS, "r", encoding="utf-8") as f:
                try:
                    contactos = json.load(f)
                    if 0 <= self.indice_contacto < len(contactos):
                        datos = contactos[self.indice_contacto]
                        self.input_nombre.text = datos.get("nombre", "")
                        self.input_correo.text = datos.get("correo", "")
                        self.input_telefono.text = datos.get("telefono", "")
                        self.input_testigo.text = datos.get("testigo", "")
                except json.JSONDecodeError:
                    pass

    def guardar_contacto(self, instance):
        if os.path.exists(RUTA_CONTACTOS):
            with open(RUTA_CONTACTOS, "r", encoding="utf-8") as f:
                contactos = json.load(f)

            if 0 <= self.indice_contacto < len(contactos):
                contactos[self.indice_contacto] = {
                    "nombre": self.input_nombre.text.strip(),
                    "correo": self.input_correo.text.strip(),
                    "telefono": self.input_telefono.text.strip(),
                    "testigo": self.input_testigo.text.strip()
                }

                with open(RUTA_CONTACTOS, "w", encoding="utf-8") as f:
                    json.dump(contactos, f, indent=4, ensure_ascii=False)

        self.manager.current = "pantalla_lista_contactos"

    def volver_menu(self, instance):
        self.manager.current = "pantalla_lista_contactos"