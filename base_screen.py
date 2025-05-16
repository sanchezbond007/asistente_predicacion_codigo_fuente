# pantallas/base_screen.py
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.metrics import dp

class BaseScreen(Screen):
    def add_back_button(self, target='menu', text='Volver'):
        """
        Añade al final de self.layout un botón que vuelve a la pantalla `target`.
        """
        btn = Button(
            text=text,
            size_hint_y=None,
            height=dp(50)
        )
        btn.bind(on_release=lambda *a: setattr(self.manager, 'current', target))
        # asumimos que cada pantalla ha definido self.layout como su BoxLayout padre:
        self.layout.add_widget(btn)