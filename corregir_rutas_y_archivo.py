import os
import json
import shutil

# Ruta base del proyecto (donde esté este script)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DATOS = os.path.join(BASE_DIR, "datos")
ARCHIVO_DESTINO = os.path.join(RUTA_DATOS, "maestro_bilingue.json")

# Asegurar carpeta datos/
if not os.path.exists(RUTA_DATOS):
    os.makedirs(RUTA_DATOS)
    print(f"[CREADO] Carpeta 'datos/' creada en: {RUTA_DATOS}")

# Buscar archivos alternativos
candidatos = [
    f for f in os.listdir(BASE_DIR)
    if f.endswith(".json") and "maestro" in f and f != "maestro_bilingue.json"
]

if os.path.exists(ARCHIVO_DESTINO):
    print(f"[OK] El archivo ya existe: {ARCHIVO_DESTINO}")
elif candidatos:
    origen = os.path.join(BASE_DIR, candidatos[0])
    shutil.copy(origen, ARCHIVO_DESTINO)
    print(f"[COPIADO] {candidatos[0]} -> datos/maestro_bilingue.json")
else:
    print("[ERROR] No se encontró ningún archivo maestro*.json para corregir.")
    exit()

# Verificar el contenido
try:
    with open(ARCHIVO_DESTINO, "r", encoding="utf-8") as f:
        datos = json.load(f)
        if isinstance(datos, dict) and "es" in datos.get("temas", {}) and "en" in datos.get("temas", {}):
            print("[OK] El contenido del JSON parece válido con 'es' y 'en'.")
        else:
            print("[ADVERTENCIA] El archivo no tiene claves 'es' y 'en' esperadas en 'temas'.")
except Exception as e:
    print(f"[ERROR] Fallo al leer o validar el JSON: {e}")