import os
import glob
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def obtener_sugerencias(idioma='es'):
    carpeta = os.path.join(BASE_DIR, 'datos', 'temas')
    archivos = glob.glob(os.path.join(carpeta, 'bloque_*.json'))
    sugerencias = []

    for archivo in archivos:
        with open(archivo, 'r', encoding='utf-8') as f:
            bloque = json.load(f)
            for tema in bloque.get('temas', []):
                sugerencias.append({
                    'titulo': tema['titulo'].get(idioma, ''),
                    'respuesta': tema['respuesta'].get(idioma, ''),
                    'cita': tema.get('cita', ''),
                    'categoria': tema.get('categoria', ''),
                })

    return sugerencias

def obtener_detalle_tema(titulo_buscado, idioma='es'):
    temas = obtener_sugerencias(idioma)
    for tema in temas:
        if tema['titulo'] == titulo_buscado:
            return tema
    return None