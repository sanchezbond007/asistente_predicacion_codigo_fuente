#!/bin/bash

echo "Subiendo proyecto actualizado a GitHub..."

# Navega a la carpeta actual del script
cd "$(dirname "$0")"

# Inicializa git si no existe
if [ ! -d .git ]; then
    git init
    git remote add origin https://github.com/josesanchez/asistente_predicacion_codigo_fuente.git
fi

# Establece la URL remota por si cambia
git remote set-url origin https://github.com/josesanchez/asistente_predicacion_codigo_fuente.git

# Añadir todos los archivos
git add .

# Confirmar los cambios
git commit -m "Actualización desde script automático"

# Enviar al repositorio y sobrescribir
git push -u origin main --force

echo "Proyecto subido exitosamente a GitHub."