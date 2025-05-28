pantalla_menu.py (actualizado con botón de actualización)

from kivy.uix.screenmanager import Screen from kivy.uix.boxlayout import BoxLayout from kivy.uix.button import Button import subprocess

class PantallaMenu(Screen): def init(self, **kwargs): super().init(**kwargs) layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

layout.add_widget(Button(text="1. Ver sugerencias", size_hint=(1, None), height=90, font_size=60,
                             on_press=lambda x: self.manager.current="sugerencias"))

    layout.add_widget(Button(text="2. Buscar tema", size_hint=(1, None), height=90, font_size=60,
                             on_press=lambda x: self.manager.current="buscar"))

    layout.add_widget(Button(text="3. Ver historial", size_hint=(1, None), height=90, font_size=60,
                             on_press=lambda x: self.manager.current="historial"))

    layout.add_widget(Button(text="4. Editar contacto", size_hint=(1, None), height=90, font_size=60,
                             on_press=lambda x: self.manager.current="pantalla_lista_contactos"))

    layout.add_widget(Button(text="5. Categorías", size_hint=(1, None), height=90, font_size=60,
                             on_press=lambda x: self.manager.current="categorias"))

    layout.add_widget(Button(text="6. Temas en Debate", size_hint=(1, None), height=90, font_size=60,
                             on_press=lambda x: self.manager.current="temas_profundos"))

    layout.add_widget(Button(text="7. Actualizar App", size_hint=(1, None), height=90, font_size=60,
                             on_press=self.ejecutar_actualizador))

    self.add_widget(layout)

def ejecutar_actualizador(self, instance):
    try:
        subprocess.run(["python3", "actualizador.py"])
    except Exception as e:
        print("Error al ejecutar el actualizador:", e)

