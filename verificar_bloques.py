import os
import json

RUTA_BLOQUES = os.path.join(os.path.dirname(__file__), 'datos', 'temas')

def verificar_bloques():
    errores = 0
    archivos = sorted([f for f in os.listdir(RUTA_BLOQUES) if f.startswith('bloque_') and f.endswith('.json')])

    for nombre_archivo in archivos:
        ruta = os.path.join(RUTA_BLOQUES, nombre_archivo)
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if not isinstance(data, dict):
                print(f"[ERROR] {nombre_archivo}: no es un diccionario raíz.")
                errores += 1
                continue

            if "temas" not in data or not isinstance(data["temas"], list):
                print(f"[ERROR] {nombre_archivo}: falta la clave 'temas' o no es una lista.")
                errores += 1
                continue

            for i, tema in enumerate(data["temas"], 1):
                for campo in ["titulo", "respuesta"]:
                    if campo not in tema or not isinstance(tema[campo], dict):
                        print(f"[ERROR] {nombre_archivo} - tema {i}: falta o mal formato de '{campo}'")
                        errores += 1
                        continue
                    for lang in ["es", "en"]:
                        if lang not in tema[campo] or not isinstance(tema[campo][lang], str):
                            print(f"[ERROR] {nombre_archivo} - tema {i}: falta '{campo}.{lang}' o no es string")
                            errores += 1

                for campo_simple in ["cita", "categoria"]:
                    if campo_simple not in tema or not isinstance(tema[campo_simple], str):
                        print(f"[ERROR] {nombre_archivo} - tema {i}: falta o mal tipo '{campo_simple}'")
                        errores += 1

        except Exception as e:
            print(f"[ERROR] Al leer {ruta}: {e}")
            errores += 1

    if errores == 0:
        print("✅ Todos los bloques están correctos.")
    else:
        print(f"❌ Se detectaron {errores} errores en los archivos de bloques.")

if __name__ == "__main__":
    verificar_bloques()