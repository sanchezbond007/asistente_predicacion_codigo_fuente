import os
import json
import glob

# 1) Detectar en cuál carpeta están tus JSON de temas
posibles = [
    os.path.join(os.path.dirname(__file__), 'temas'),  # junto al módulo
    os.path.join(os.getcwd(), 'temas'),                # en el working dir
]
for p in posibles:
    if os.path.isdir(p):
        TEMAS_DIR = p
        break
else:
    TEMAS_DIR = posibles[0]  # si no existe ninguna, usa la primera

def cargar_todos_los_bloques():
    """
    Carga todos los archivos JSON de bloques desde TEMAS_DIR.
    Retorna una lista de dicts, uno por cada bloque.
    """
    bloques = []
    pattern = os.path.join(TEMAS_DIR, 'bloque_*.json')
    for ruta in sorted(glob.glob(pattern)):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                bloque = json.load(f)
            bloques.append(bloque)
        except Exception as e:
            print(f"Error cargando {ruta}: {e}")
    return bloques

def cargar_todos_los_temas(unificar_duplicados=True):
    """
    Carga todos los temas de todos los bloques, opcionalmente eliminando duplicados.
    Retorna una lista de temas (dicts con keys: titulo, respuesta, cita, categoria).
    """
    bloques = cargar_todos_los_bloques()
    todos = []
    vistos = set()
    for bloque in bloques:
        for tema in bloque.get('temas', []):
            titulo = tema.get('titulo')
            if unificar_duplicados:
                if titulo in vistos:
                    continue
                vistos.add(titulo)
            todos.append(tema)
    return todos

if __name__ == '__main__':
    # Prueba rápida por consola
    print(f"Cargando bloques desde: {TEMAS_DIR}")
    bloques = cargar_todos_los_bloques()
    print(f"Bloques cargados: {len(bloques)}")
    temas = cargar_todos_los_temas()
    print(f"Total de temas únicos: {len(temas)}")
