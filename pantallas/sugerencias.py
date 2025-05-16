# pantallas/sugerencias.py

import os
import json
import random

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout    import BoxLayout
from kivy.uix.gridlayout   import GridLayout
from kivy.uix.scrollview   import ScrollView
from kivy.uix.button       import Button
from kivy.metrics          import dp

# 1) Calculamos la ruta de datos/temas relativa a este archivo:
HERE = os.path.dirname(__file__)                       # .../pantallas
PROJECT = os.path.dirname(HERE)                        # raíz de tu proyecto
RUTA_TEMAS = os.path.join(PROJECT, 'datos', 'temas')   # .../datos/temas


class PantallaSugerencias(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout principal vertical
        self.layout = BoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10)
        )
        self.add_widget(self.layout)

        # Scroll + GridLayout para los botones
        self.scroll = ScrollView(size_hint=(1, 1))
        self.grid   = GridLayout(
            cols=1,
            size_hint_y=None,
            spacing=dp(10),
            padding=[0, 0, 0, dp(10)]
        )
        self.grid.bind(minimum_height=self.grid.setter('height'))
        self.scroll.add_widget(self.grid)
        self.layout.add_widget(self.scroll)

        # Botón recargar
        btn_recargar = Button(
            text="🔄 Nuevas 10 sugerencias",
            size_hint_y=None,
            height=dp(50)
        )
        btn_recargar.bind(on_release=self.mostrar_sugerencias)
        self.layout.add_widget(btn_recargar)

        # Botón volver
        btn_volver = Button(
            text="Volver al menú",
            size_hint_y=None,
            height=dp(50)
        )
        btn_volver.bind(on_release=lambda *_: setattr(self.manager, 'current', 'menu'))
        self.layout.add_widget(btn_volver)

    def on_pre_enter(self, *args):
        # cada vez que entres a esta pantalla, recarga
        self.mostrar_sugerencias()

    def _cargar_todos_los_temas(self):
        # 1) Rutas posibles
        rutas = [
            RUTA_TEMAS,  # la calculada con __file__
            os.path.join(os.getcwd(), 'datos', 'temas'),  # la basada en cwd
        ]

        # ———> Prints de debug para saber qué rutas existen <———
        print("🔍 Rutas posibles de temas:")
        for r in rutas:
            print(f"   • {r} → existe? {os.path.isdir(r)}")
        # ————————————————————————————————————————————————

        temas = []

        # 2) Averiguamos cuál existe
        ruta_valida = None
        for r in rutas:
            if os.path.isdir(r):
                ruta_valida = r
                break

        # 3) Si ninguna existe, lo imprimimos para debug
        if ruta_valida is None:
            print("⚠️  No encontré carpeta temas en ninguna de estas rutas:")
            for r in rutas:
                print("   -", r)
            return temas

        # 4) Recorremos archivos JSON dentro de la ruta válida
        for fname in os.listdir(ruta_valida):
            if not fname.lower().endswith('.json'):
                continue
            path = os.path.join(ruta_valida, fname)
            try:
                data = json.load(open(path, encoding='utf-8'))
            except Exception:
                continue

            # Solo listas de títulos
            if isinstance(data, list):
                for elem in data:
                    if isinstance(elem, dict) and 'titulo' in elem:
                        temas.append(elem['titulo'])
                    elif isinstance(elem, str):
                        temas.append(elem)

        return temas

    def mostrar_sugerencias(self, *args):
        self.grid.clear_widgets()

        todos     = self._cargar_todos_los_temas()
        random.shuffle(todos)
        seleccion = todos[:10] if len(todos) >= 10 else todos

        if not seleccion:
            self.grid.add_widget(Button(
                text="(No hay temas disponibles)",
                size_hint_y=None,
                height=dp(50)
            ))
            return

        for tema in seleccion:
            btn = Button(
                text=tema,
                size_hint_y=None,
                text_size=(None, None),
                halign='left',
                valign='middle'
            )
            btn.bind(
                size=lambda inst, sz: inst.setter('text_size')((sz[0] - dp(20), None))
            )
            btn.bind(
                texture_size=lambda inst, ts: setattr(inst, 'height', ts[1] + dp(20))
            )
            btn.bind(on_release=lambda inst, t=tema: self.abrir_popup_tema(t))
            self.grid.add_widget(btn)

        # Registra en el historial de la aplicación (si lo usas)
        App.get_running_app().registrar_evento(
            f"Sugerencias mostradas: {seleccion}"
        )

    def abrir_popup_tema(self, tema):
        from kivy.uix.popup import Popup
        from kivy.uix.label import Label

        texto = "(No hay contenido disponible.)"
        ruta  = os.path.join(PROJECT, 'datos', 'debates.json')
        if os.path.isfile(ruta):
            try:
                debates = json.load(open(ruta, encoding='utf-8'))
                if tema in debates and 'texto' in debates[tema]:
                    texto = debates[tema]['texto']
            except Exception:
                pass

        contenido = Label(
            text=texto,
            halign='center',
            valign='top'
        )
        contenido.bind(size=lambda w, h: setattr(
            contenido, 'text_size', (w.width - dp(20), None)
        ))

        popup = Popup(
            title=tema,
            content=contenido,
            size_hint=(0.9, 0.9)
        )
        popup.open()
        App.get_running_app().registrar_evento(f"Tema abierto: {tema}")