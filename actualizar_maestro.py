# actualizar_maestro.py
"""
Script para generar maestro.json y debates.json a partir de bloque_*.json
Ignora bloques con JSON inválido e informa errores.
"""

import json
import glob
import os

# Ruta absoluta a la carpeta datos
DATA_DIR = '/storage/emulated/0/asistente_predicacion_migracion_kivy/datos'

def find_block_files(data_dir):
    """Devuelve lista de archivos bloque_*.json en datos/ y datos/temas"""
    patterns = [
        os.path.join(data_dir, 'bloque_*.json'),
        os.path.join(data_dir, 'temas', 'bloque_*.json'),
    ]
    files = []
    for pat in patterns:
        found = glob.glob(pat)
        print(f"Buscando en {pat}: {len(found)} archivos")
        files.extend(found)
    return files

def load_blocks(files):
    """Carga y devuelve lista de temas de los archivos JSON"""
    all_temas = []
    for filepath in files:
        print(f"Leyendo: {filepath}")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                bloque = json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR JSON en {os.path.basename(filepath)}: {e}")
            continue
        temas = bloque.get('temas', [])
        print(f"  -> {len(temas)} temas en este bloque")
        all_temas.extend(tema.copy() for tema in temas)
    return all_temas

def deduplicate(temas):
    """Elimina duplicados basándose en id o titulo"""
    unique = {}
    for tema in temas:
        key = tema.get('id') or tema.get('titulo')
        if key not in unique:
            unique[key] = tema
    return list(unique.values())

def assign_ids(temas):
    """Asigna IDs secuenciales si faltan"""
    result = []
    for idx, tema in enumerate(temas, start=1):
        t = tema.copy()
        t['id'] = t.get('id', idx)
        result.append(t)
    return result

def save_json(path, data):
    """Guarda data en path como JSON"""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    files = find_block_files(DATA_DIR)
    if not files:
        print("No se encontraron bloques. Verifica nombres y rutas.")
        return

    temas = load_blocks(files)
    print(f"Total de temas leídos: {len(temas)}")
    unique = deduplicate(temas)
    print(f"Temas únicos tras deduplicar: {len(unique)}")
    temas_final = assign_ids(unique)

    maestro_path = os.path.join(DATA_DIR, 'maestro.json')
    save_json(maestro_path, temas_final)
    print(f"Maestro generado con {len(temas_final)} temas en {maestro_path}")

    debates = [t for t in temas_final if t.get('categoria', '').lower() == 'debate']
    debates_path = os.path.join(DATA_DIR, 'debates.json')
    save_json(debates_path, debates)
    print(f"Debates generado con {len(debates)} temas en {debates_path}")

if __name__ == '__main__':
    main()