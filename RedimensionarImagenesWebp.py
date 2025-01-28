import os
from PIL import Image
from pathlib import Path

# Constantes
CARPETA_ORIGEN = r"C:\Users\acapaizlo\Downloads\loteriaMexicana\SD"
CARPETA_DESTINO = "WEBP"
ANCHO_MAXIMO = 700
EFFORT_WEBP = 6
QUALITY_WEBP = 50

def convertir_a_webp(carpeta_origen, carpeta_destino):
    # Crear la carpeta de destino si no existe
    Path(carpeta_origen, carpeta_destino).mkdir(exist_ok=True)

    # Obtener la lista de archivos de imagen en la carpeta de origen
    archivos = [f for f in os.listdir(carpeta_origen) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    total_archivos = len(archivos)

    for i, archivo in enumerate(archivos, 1):
        ruta_origen = os.path.join(carpeta_origen, archivo)
        nombre_base = os.path.splitext(archivo)[0]
        ruta_destino = os.path.join(carpeta_origen, carpeta_destino, f"{nombre_base}.webp")

        try:
            with Image.open(ruta_origen) as img:
                # Redimensionar la imagen manteniendo la proporción
                img.thumbnail((ANCHO_MAXIMO, ANCHO_MAXIMO))

                # Guardar como WEBP
                img.save(ruta_destino, 'WEBP', method=EFFORT_WEBP, quality=QUALITY_WEBP)

            print(f"Procesado {i}/{total_archivos}: {archivo}")
        except Exception as e:
            print(f"Error al procesar {archivo}: {str(e)}")

    print(f"\nProceso completado. Se han convertido {total_archivos} imágenes.")

if __name__ == "__main__":
    convertir_a_webp(CARPETA_ORIGEN, CARPETA_DESTINO)