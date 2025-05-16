from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import json

RUTA_CONTACTOS = "datos/contactos.json"

class PantallaContacto(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Layout principal
        self.box = BoxLayout(orientation="vertical", padding=20, spacing=10)
        
        # Título
        self.box.add_widget(Label(text="Datos de Contacto", size_hint_y=None, height=50))
        
        # Nombre
        self.box.add_widget(Label(text="Nombre:"))
        self.input_nombre = TextInput(multiline=False)
        self.box.add_widget(self.input_nombre)
        
        # Teléfono
        self.box.add_widget(Label(text="Teléfono:"))
        self.input_telefono = TextInput(multiline=False)
        self.box.add_widget(self.input_telefono)
        
        # Email
        self.box.add_widget(Label(text="Correo electrónico:"))
        self.input_correo = TextInput(multiline=False)
        self.box.add_widget(self.input_correo)
        
        # Botones de acción
        boton_guardar = Button(text="Guardar")
        boton_guardar.bind(on_release=self.guardar_contacto)
        boton_volver = Button(text="Volver")
        boton_volver.bind(on_release=lambda instance: setattr(self.manager, 'current', 'menu'))
        self.box.add_widget(boton_guardar)
        self.box.add_widget(boton_volver)
        
        # Scroll por si hay muchos widgets
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.box)
        self.add_widget(scroll)

    def guardar_contacto(self, instance):
        # Carga o crea la lista de contactos
        try:
            with open(RUTA_CONTACTOS, 'r', encoding='utf-8') as f:
                contactos = json.load(f)
        except FileNotFoundError:
            contactos = []
        
        # Agrega el contacto
        nuevo = {
            'nombre': self.input_nombre.text,
            'telefono': self.input_telefono.text,
            'correo': self.input_correo.text
        }
        contactos.append(nuevo)
        
        # Guarda nuevamente en el archivo
        with open(RUTA_CONTACTOS, 'w', encoding='utf-8') as f:
            json.dump(contactos, f, ensure_ascii=False, indent=2)
        
        # Regresa al menú
        self.manager.current = 'menu'
