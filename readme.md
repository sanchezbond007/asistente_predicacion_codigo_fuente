# Asistente de Predicación Digital

**Aplicación Android para Testigos de Jehová**, diseñada para apoyar la predicación. Proporciona sugerencias de temas bíblicos, administración de contactos, historial de visitas, búsqueda de temas, y envío de resúmenes por correo electrónico.

---

## Características principales

- Interfaz visual con botones grandes (ideal para Android)
- Sistema multiusuario con historial y contactos independientes
- Más de 180 temas bíblicos organizados por bloques y categorías
- Búsqueda por palabra clave, temas sugeridos y temas en debate
- Envío de resúmenes por correo electrónico mediante `mailto:`
- Citas bíblicas extraídas de fuentes confiables (TNM, JW.ORG, NVI)
- Estructura modular y escalable para futuras actualizaciones
- Gestión de contactos con opción de edición y búsqueda fácil

---

## Estructura del proyecto

- `main.py` — controlador principal de la aplicación
- `pantallas/` — pantallas Kivy modulares (menú, historial, sugerencias, etc.)
- `datos/temas/` — bloques JSON con temas bíblicos y citas
- `historial/` — registros de sesiones de predicación
- `requirements.txt` — dependencias del proyecto
- `actualizar_maestro.py` — utilidad para actualizar la base de datos de temas
- `base_screen.py` — clase base común para pantallas
- `globals.py` — variables globales para el usuario y la sesión
- `RESUMEN_PROYECTO.md` — resumen técnico del desarrollo

---

## Requisitos

- Python 3.10 o superior
- Kivy 2.3 o superior
- Compatible con Pydroid (Android) y Ubuntu

---

## Instalación rápida

```bash
git clone https://github.com/josesanchez/asistente_predicacion_codigo_fuente.git
cd asistente_predicacion_codigo_fuente
pip install -r requirements.txt
python3 main.py