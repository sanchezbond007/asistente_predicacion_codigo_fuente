# pantallas/editar_contacto.py

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
import json
import os

RUTA_CONTACTOS = os.path.join(os.path.dirname(__file__), "..", "datos", "contactos.json")

class PantallaGestionContacto(Screen):
    indice_contacto = NumericProperty(-1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", spacing=10, padding=20)
        self.input_nombre = TextInput(hint_text="Nombre", multiline=False)
        self.input_correo = TextInput(hint_text="Correo", multiline=False)
        self.input_telefono = TextInput(hint_text="Teléfono", multiline=False)
        self.input_testigo = TextInput(hint_text="Testigo", multiline=False)

        self.layout.add_widget(Label(text="Editar contacto seleccionado", font_size=24))
        self.layout.add_widget(self.input_nombre)
        self.layout.add_widget(self.input_correo)
        self.layout.add_widget(self.input_telefono)
        self.layout.add_widget(self.input_testigo)

        botones = BoxLayout(size_hint=(1, 0.2), spacing=10)
        btn_guardar = Button(text="Guardar", background_color=(0, 0.5, 0, 1))
        btn_volver = Button(text="Volver", background_color=(0.2, 0.2, 0.2, 1))

        btn_guardar.bind(on_press=self.guardar_contacto)
        btn_volver.bind(on_press=self.volver_menu)

        botones.add_widget(btn_guardar)
        botones.add_widget(btn_volver)
        self.layout.add_widget(botones)

        self.add_widget(self.layout)

    def on_pre_enter(self):
        # Al entrar a esta pantalla, carga los datos del contacto seleccionado
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
        # Guarda la edición en el JSON
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

        # Regresa a la lista usando el nombre correcto
        self.manager.current = "lista_contactos"

    def volver_menu(self, instance):
        # Regresa sin guardar usando también el nombre "lista_contactos"
        self.manager.current = "lista_contactos"