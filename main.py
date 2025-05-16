# main.py

import os, sys

# Asegura que la carpeta donde está main.py esté en la ruta de búsqueda
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition

# Para que el teclado no desplace los layouts
Window.softinput_mode = 'pan'

# Importa todas tus pantallas
from pantallas.login import PantallaLogin
from pantallas.menu import PantallaMenu
from pantallas.buscar import PantallaBuscar
from pantallas.sugerencias import PantallaSugerencias
from pantallas.categorias import PantallaCategorias
from pantallas.debate import PantallaDebate
from pantallas.contacto import PantallaContacto
from pantallas.resumen_digital import PantallaResumenDigital
from pantallas.recordatorio import PantallaRecordatorio
from pantallas.editar_contacto import PantallaGestionContacto
from pantallas.historial import PantallaHistorial

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Inicializamos el historial desde el arranque
        self.historial = []

    def build(self):
        sm = ScreenManager(transition=FadeTransition())

        sm.add_widget(PantallaLogin(name='login'))
        sm.add_widget(PantallaMenu(name='menu'))
        sm.add_widget(PantallaBuscar(name='buscar'))
        sm.add_widget(PantallaSugerencias(name='sugerencias'))
        sm.add_widget(PantallaCategorias(name='categorias'))
        sm.add_widget(PantallaDebate(name='debates'))
        sm.add_widget(PantallaContacto(name='contacto'))
        sm.add_widget(PantallaResumenDigital(name='resumen_digital'))
        sm.add_widget(PantallaRecordatorio(name='recordatorio'))
        sm.add_widget(PantallaGestionContacto(name='editar_contacto'))
        sm.add_widget(PantallaHistorial(name='historial'))

        sm.current = 'login'
        return sm

    def registrar_evento(self, texto_evento: str):
        """
        Guarda en lista cada acción relevante.
        """
        self.historial.append(texto_evento)

if __name__ == '__main__':
    MainApp().run()