import json
import glob
import os
import shutil

DATA_DIR = '/storage/emulated/0/asistente_predicacion_migracion_kivy/datos'

def buscar_archivos(data_dir):
    patrones = [
        os.path.join(data_dir, 'bloque_*.json'),
        os.path.join(data_dir, 'temas', 'bloque_*.json'),
    ]
    archivos = []
    for p in patrones:
        archivos.extend(glob.glob(p))
    return archivos

def cargar_temas_sin_modificar(archivos):
    todos = []
    for archivo in archivos:
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                bloque = json.load(f)
                temas = bloque.get("temas", [])
                todos.extend(temas)
        except Exception as e:
            print(f"[ERROR] al leer {archivo}: {e}")
    return todos

def deduplicar(temas):
    vistos = {}
    for tema in temas:
        clave = json.dumps(tema.get("titulo", ""), ensure_ascii=False)
        if clave not in vistos:
            vistos[clave] = tema
    return list(vistos.values())

def asignar_ids(temas):
    for i, tema in enumerate(temas, 1):
        tema["id"] = i
    return temas

def guardar_json(ruta, data):
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def backup_maestro(ruta):
    if os.path.exists(ruta):
        backup = ruta.replace('.json', '_backup.json')
        shutil.copy(ruta, backup)
        print(f"Copia de seguridad creada: {backup}")

def main():
    archivos = buscar_archivos(DATA_DIR)
    if not archivos:
        print("No se encontraron archivos.")
        return

    temas = cargar_temas_sin_modificar(archivos)
    temas = deduplicar(temas)
    temas = asignar_ids(temas)

    maestro_path = os.path.join(DATA_DIR, 'maestro.json')
    backup_maestro(maestro_path)
    guardar_json(maestro_path, temas)

    print(f"Archivo maestro.json generado con {len(temas)} temas exactamente como estaban en los bloques.")

if __name__ == "__main__":
    main()