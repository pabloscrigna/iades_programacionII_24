#!/bin/bash

# Variables
SOURCE_DIR="/tmp/"                   # Carpeta de origen
BACKUP_DIR="/home/pablo/backup"            # Carpeta de backup
DATE=$(date +%Y-%m-%d)              # Fecha actual
BACKUP_FILE="backup-$DATE.tar.gz"   # Nombre del archivo de backup

echo $DATE

# Crear la carpeta de backup si no existe
if [ ! -d "$BACKUP_DIR" ]; then
  mkdir -p "$BACKUP_DIR"
fi

# Crear el archivo de backup
# tar -czf "$BACKUP_DIR/$BACKUP_FILE" -C "$SOURCE_DIR" .

# Verificar si el backup fue exitoso
# if [ $? -eq 0 ]; then
#   echo "Backup realizado exitosamente: $BACKUP_DIR/$BACKUP_FILE"
# else
#   echo "Error al realizar el backup"
# fi