import os
import json
import chardet

# Detecta la ruta base del proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RUTA_ARCHIVO = os.path.join(BASE_DIR, "datos", "maestro_bilingue_corregido.json")

def detectar_codificacion(ruta):
    with open(ruta, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def cargar_json_seguro(ruta):
    try:
        encoding_detectada = detectar_codificacion(ruta)
        with open(ruta, "r", encoding=encoding_detectada) as f:
            data = json.load(f)
        print(f"[OK] Archivo leído correctamente con codificación: {encoding_detectada}")
        return data, encoding_detectada
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo JSON: {e}")
        return None, None

def guardar_json_utf8(data, ruta):
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[GUARDADO] Archivo corregido y guardado en UTF-8: {ruta}")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")

def validar_estructura(data):
    if not isinstance(data, dict):
        return False
    if "temas" not in data or not isinstance(data["temas"], dict):
        return False
    for lang in ["es", "en"]:
        if lang not in data["temas"] or not isinstance(data["temas"][lang], list):
            return False
    return True

def ejecutar_verificacion():
    if not os.path.exists(RUTA_ARCHIVO):
        print(f"[ERROR] Archivo no encontrado: {RUTA_ARCHIVO}")
        return

    data, codificacion = cargar_json_seguro(RUTA_ARCHIVO)
    if data is None:
        return

    if not validar_estructura(data):
        print("[ERROR] La estructura del JSON no es válida. Se esperaba 'temas' con claves 'es' y 'en'.")
        return

    if codificacion.lower() != "utf-8":
        guardar_json_utf8(data, RUTA_ARCHIVO)
    else:
        print("[OK] El archivo ya está en UTF-8 y tiene estructura válida.")

if __name__ == "__main__":
    ejecutar_verificacion()