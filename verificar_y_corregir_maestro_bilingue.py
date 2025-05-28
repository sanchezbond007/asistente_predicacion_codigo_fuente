import json
import os

RUTA_ARCHIVO = os.path.join("datos", "maestro_bilingue.json")

def es_entrada_valida(entrada):
    if not isinstance(entrada, dict):
        return False
    if "titulo" not in entrada:
        return False
    titulo = entrada["titulo"]
    return (
        isinstance(titulo, dict) and
        "es" in titulo and isinstance(titulo["es"], str) and titulo["es"].strip() and
        "en" in titulo and isinstance(titulo["en"], str) and titulo["en"].strip()
    )

def verificar_y_corregir():
    if not os.path.exists(RUTA_ARCHIVO):
        print(f"Archivo no encontrado: {RUTA_ARCHIVO}")
        return

    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
        try:
            datos = json.load(f)
        except json.JSONDecodeError:
            print("Error: El archivo JSON no tiene formato válido.")
            return

    if not isinstance(datos, list):
        print("Corrigiendo: el archivo no es una lista, envolviendo en lista...")
        datos = [datos]

    entradas_validas = []
    for entrada in datos:
        if es_entrada_valida(entrada):
            entradas_validas.append(entrada)
        else:
            print(f"Entrada inválida detectada y excluida: {entrada}")

    print(f"Total válido: {len(entradas_validas)} de {len(datos)} entradas.")

    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(entradas_validas, f, ensure_ascii=False, indent=2)

    print("Archivo corregido y guardado exitosamente.")

if __name__ == "__main__":
    verificar_y_corregir()