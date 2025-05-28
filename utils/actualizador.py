import os
import urllib.request

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from traducciones import traducir


URL_VERSION_REMOTA = "https://raw.githubusercontent.com/sanchezbond007/asistente_predicacion_bilingue/main/version.txt"
RUTA_VERSION_LOCAL = os.path.join(os.path.dirname(__file__), '..', 'datos', 'version_local.txt')


def obtener_version_local():
    if not os.path.isfile(RUTA_VERSION_LOCAL):
        return "0.0.0"
    with open(RUTA_VERSION_LOCAL, 'r', encoding='utf-8') as f:
        return f.read().strip()


def obtener_version_remota():
    try:
        with urllib.request.urlopen(URL_VERSION_REMOTA) as response:
            return response.read().decode('utf-8').strip()
    except Exception as e:
        return None


def comparar_versiones(v1, v2):
    def normalizar(v): return [int(x) for x in v.split(".")]
    return normalizar(v1) < normalizar(v2)


def verificar_actualizaciones():
    v_local = obtener_version_local()
    v_remota = obtener_version_remota()

    layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

    if v_remota is None:
        mensaje = Label(text="No se pudo conectar con GitHub.")
    elif comparar_versiones(v_local, v_remota):
        mensaje = Label(text=f"¡Hay una nueva versión disponible!\nActual: {v_local} → Nueva: {v_remota}")
    else:
        mensaje = Label(text="Ya estás usando la versión más reciente.")

    layout.add_widget(mensaje)

    btn_cerrar = Button(text=traducir("cerrar"), size_hint_y=None, height=50)
    layout.add_widget(btn_cerrar)

    popup = Popup(title=traducir("buscar_actualizaciones"), content=layout, size_hint=(0.8, 0.5))
    btn_cerrar.bind(on_release=popup.dismiss)
    popup.open()