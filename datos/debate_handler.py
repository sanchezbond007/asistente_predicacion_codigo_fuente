# datos/debate_handler.py

import os
import json
import logging

# Configura el logger para este módulo
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # DEBUG para ver toda la traza
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s %(name)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def cargar_temas_debate():
    """
    Busca todos los .json en datos/debate/, los lee y extrae
    los temas de debate en una lista de dicts.
    """
    carpeta = os.path.join(os.path.dirname(__file__), "debate")
    logger.debug(f"Buscando archivos en: {os.path.abspath(carpeta)}")

    if not os.path.isdir(carpeta):
        logger.warning(f"No existe el directorio de debates: {carpeta}")
        return []

    lista_temas = []
    archivos = [fn for fn in os.listdir(carpeta) if fn.endswith(".json")]
    logger.debug(f"Archivos .json encontrados: {archivos}")

    for fn in archivos:
        path = os.path.join(carpeta, fn)
        logger.debug(f" → Leyendo {path}")
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"   ¡Error decodificando {fn}! {e}")
            continue
        except Exception as e:
            logger.error(f"   ¡No se pudo abrir {fn}! {e}")
            continue

        # Determina la lista de temas dentro de 'data'
        if isinstance(data, list):
            temas = data
        elif isinstance(data, dict) and "temas" in data:
            temas = data["temas"]
        elif isinstance(data, dict) and "titulo" in data and "respuesta" in data:
            temas = [data]
        else:
            logger.warning(f"   Formato inesperado en {fn}, se omite.")
            continue

        # Asegura que cada tema tenga key 'profundizar'
        for tema in temas:
            tema.setdefault("profundizar", [])
            lista_temas.append(tema)

    logger.info(f">>> Debate: cargados {len(lista_temas)} temas de {len(archivos)} archivos")
    return lista_temas
