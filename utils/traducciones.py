# utils/traducciones.py

traducciones = {
    "es": {
        "titulo": "===== Asistente de Predicación =====",
        "login": "Iniciar sesión",
        "crear_usuario": "Crear usuario",
        "actualizar": "Buscar actualizaciones",
        "seleccionar_idioma": "Selecciona el idioma:",
        "volver": "Volver"  # ✅ añadido
    },
    "en": {
        "titulo": "===== Preaching Assistant =====",
        "login": "Log in",
        "crear_usuario": "Create user",
        "actualizar": "Check for updates",
        "seleccionar_idioma": "Select Language:",
        "volver": "Back"  # ✅ añadido
    }
}

def traducir(idioma, clave):
    # Devuelve la traducción si existe, o la clave original como fallback
    return traducciones.get(idioma, traducciones["en"]).get(clave, clave)