# utils/temas_handler2.py

import os
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CARPETA_TEMAS_PROFUNDOS = os.path.join(BASE_DIR, 'temas_profundos')

def cargar_temas_profundos():
    temas = []
    if not os.path.exists(CARPETA_TEMAS_PROFUNDOS):
        print("No se encontró la carpeta 'temas_profundos'")
        return temas

    for nombre_archivo in os.listdir(CARPETA_TEMAS_PROFUNDOS):
        if nombre_archivo.endswith('.json'):
            ruta = os.path.join(CARPETA_TEMAS_PROFUNDOS, nombre_archivo)
            try:
                with open(ruta, 'r', encoding='utf-8') as archivo:
                    data = json.load(archivo)
                    if isinstance(data, dict):
                        temas.append(data)
            except Exception as e:
                print(f"Error al cargar {nombre_archivo}: {e}")
    return temas