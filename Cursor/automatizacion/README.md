# 📁 Organizador de Archivos

Script en Python que organiza automáticamente los archivos de una carpeta según su tipo (extensión), creando subcarpetas por categoría y moviendo los archivos a su ubicación correspondiente.

## 🎯 Funcionalidad

El script organiza archivos en las siguientes categorías:

- **Imágenes**: `.jpg`, `.png`, `.jpeg`, `.gif`
- **Documentos**: `.pdf`, `.docx`, `.txt`, `.xlsx`
- **Video**: `.mp4`, `.avi`, `.mkv`
- **Música**: `.mp3`, `.wav`
- **Otros**: Cualquier archivo que no coincida con las categorías anteriores

## 📋 Requisitos

- Python 3.4 o superior
- No se requieren librerías externas (usa solo la biblioteca estándar)

## 🚀 Uso

### Ejecución básica:

```bash
python organizador.py
```

### Configuración:

Por defecto, el script organiza archivos en la carpeta `descargas2` del directorio home del usuario. Para cambiar la carpeta objetivo, modifica la línea 7 en `organizador.py`:

```python
carpeta_objetivo = Path.home() / "descargas2"  # Cambia "descargas2" por tu carpeta
```

## 📂 Estructura de Carpetas

Después de ejecutar el script, la carpeta objetivo quedará organizada así:

```
descargas2/
├── imagenes/
│   ├── foto1.jpg
│   └── imagen.png
├── documentos/
│   ├── documento.pdf
│   └── archivo.docx
├── video/
│   └── video.mp4
├── musica/
│   └── cancion.mp3
└── otros/
    └── archivo_desconocido.xyz
```

## ⚙️ Personalización

### Agregar nuevas categorías:

Edita el diccionario `categorias` en el código:

```python
categorias = {
    "imagenes": [".jpg", ".png", ".jpeg", ".gif"],
    "documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "video": [".mp4", ".avi", ".mkv"],
    "musica": [".mp3", ".wav"],
    "programas": [".exe", ".dmg", ".deb"]  # Nueva categoría
}
```

### Agregar nuevas extensiones:

Simplemente agrega la extensión a la lista correspondiente:

```python
"imagenes": [".jpg", ".png", ".jpeg", ".gif", ".webp", ".svg"]  # Agregar .webp y .svg
```

## ⚠️ Advertencias

- **El script mueve archivos permanentemente**. Asegúrate de hacer una copia de seguridad si es necesario.
- Los archivos se organizan automáticamente sin confirmación.
- Si un archivo ya existe en la carpeta destino, puede haber conflictos.

## 📝 Ejemplo de Salida

```
movido foto1.jpg a imagenes/
movido documento.pdf a documentos/
movido video.mp4 a video/
movido cancion.mp3 a musica/
movido archivo_rar.rar a otros/
```

## 🔧 Solución de Problemas

### Error: "No such file or directory"
- Verifica que la carpeta objetivo existe
- Asegúrate de tener permisos de escritura en la carpeta

### Los archivos no se mueven
- Verifica que tienes permisos de lectura/escritura
- Asegúrate de que los archivos no estén abiertos en otro programa

## 📄 Licencia

Este script es de uso libre. Siéntete libre de modificarlo según tus necesidades.

## 👤 Autor
Martin Gomes
Script creado para automatizar la organización de archivos descargados.

