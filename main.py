import os
import sys

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

# Asegura que el sistema encuentre los módulos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from pantallas.login import PantallaLogin
from pantallas.crear_usuario import PantallaCrearUsuario
from pantallas.menu import PantallaMenu
from pantallas.contacto import PantallaContacto
from pantallas.historial import PantallaHistorial
from pantallas.lista_contactos import PantallaListaContactos
from pantallas.sugerencias import PantallaSugerencias
from pantallas.temas_profundos import PantallaTemasProfundos
from pantallas.buscar import PantallaBuscar
from pantallas.editar_contacto import PantallaEditarContacto

class AsistentePredicacionApp(App):
    def build(self):
        self.idioma = 'es'  # idioma por defecto
        self.sm = ScreenManager()

        # Pantallas base
        self.sm.add_widget(PantallaLogin(name='login', idioma_callback=self.cambiar_idioma, continuar_callback=self.ir_a_menu))
        self.sm.add_widget(PantallaCrearUsuario(name='crear_usuario', volver_callback=self.volver_al_menu))
        self.sm.add_widget(PantallaMenu(name='menu', idioma=self.idioma, navegar_callback=self.navegar_a))
        self.sm.add_widget(PantallaContacto(name='contacto', volver_callback=self.volver_al_menu))
        self.sm.add_widget(PantallaHistorial(name='historial', volver_callback=self.volver_al_menu))
        self.sm.add_widget(PantallaListaContactos(name='lista_contactos', volver_callback=self.volver_al_menu, editar_callback=self.ir_a_editar_contacto))
        self.sm.add_widget(PantallaSugerencias(name='sugerencias', volver_callback=self.volver_al_menu, idioma=self.idioma))
        self.sm.add_widget(PantallaTemasProfundos(name='temas_profundos', volver_callback=self.volver_al_menu, idioma=self.idioma))
        self.sm.add_widget(PantallaBuscar(name='buscar', volver_callback=self.volver_al_menu))
        self.sm.add_widget(PantallaEditarContacto(name='editar_contacto', volver_callback=self.volver_al_menu))

        return self.sm

    def cambiar_idioma(self, idioma):
        self.idioma = idioma
        self.sm.get_screen('menu').idioma = idioma
        self.sm.get_screen('sugerencias').idioma = idioma
        self.sm.get_screen('temas_profundos').idioma = idioma

    def ir_a_menu(self):
        self.sm.current = 'menu'

    def volver_al_menu(self, *args):
        self.sm.current = 'menu'

    def ir_a_editar_contacto(self, contacto_id):
        editar_pantalla = self.sm.get_screen('editar_contacto')
        editar_pantalla.cargar_contacto(contacto_id)
        self.sm.current = 'editar_contacto'

    def navegar_a(self, nombre_pantalla):
        if nombre_pantalla in self.sm.screen_names:
            self.sm.current = nombre_pantalla

if __name__ == '__main__':
    AsistentePredicacionApp().run()