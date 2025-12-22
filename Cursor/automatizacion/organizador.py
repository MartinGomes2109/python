import os
from pathlib import Path



def run():
    carpeta_objetivo = Path.home() / "descargas2"

    categorias = {
        "imagenes": [".jpg", ".png", ".jpeg", ".gif"],
        "documentos": [".pdf", ".docx", ".txt", ".xlsx"],
        "video": [".mp4", ".avi", ".mkv"],
        "musica": [".mp3", ".wav"]
    }
    categorias_predefinidas = ["otros"] #donde ira lo que no entre en la categoria anterior

    extension_a_categoria = {}
    for categoria, exts in categorias.items():
        for ext in exts:
            extension_a_categoria[ext.lower()] = categoria

    archivos = [f for f in carpeta_objetivo.iterdir() if f.is_file()]
    for archivo in archivos:
        ext = archivo.suffix.lower()
        categoria = extension_a_categoria.get(ext, "otros")
        destino_dir = carpeta_objetivo / categoria
        destino_dir.mkdir(exist_ok = True)
        archivo.rename(destino_dir / archivo.name)
        print(f"movido {archivo.name} a {categoria}/")


if __name__ == '__main__':
    run()