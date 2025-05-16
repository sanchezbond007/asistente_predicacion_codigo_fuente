import os

# Ruta donde se guardará el historial
RUTA_HISTORIAL = os.path.join(os.path.dirname(__file__), "historial.txt")

def guardar_en_historial(linea):
    try:
        with open(RUTA_HISTORIAL, "a", encoding="utf-8") as f:
            f.write(linea + "\n")
    except Exception as e:
        print("Error al guardar historial:", e)

def cargar_historial():
    if not os.path.exists(RUTA_HISTORIAL):
        return []
    try:
        with open(RUTA_HISTORIAL, "r", encoding="utf-8") as f:
            return [linea.strip() for linea in f if linea.strip()]
    except Exception as e:
        print("Error al leer historial:", e)
        return []