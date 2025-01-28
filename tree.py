import os

def crear_arbol(ruta, nivel=0):
    # Obtener la lista de nombres de archivos y carpetas en la ruta
    archivos = os.listdir(ruta)

    for archivo in archivos:
        # Agregar el nivel de indentación
        indentacion = "    " * nivel

        # Obtener la ruta completa del archivo
        ruta_completa = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_completa):
            # Si es un archivo, imprimir su nombre con indentación
            print(f"{indentacion}- {archivo}")
        else:
            # Si es una carpeta, imprimir su nombre con indentación y llamar recursivamente a la función para esa carpeta
            print(f"{indentacion}+ {archivo}")
            crear_arbol(ruta_completa, nivel + 1)

# Ruta de la carpeta
ruta = r"C:\Users\acapaizlo\Desktop\Browser"

# Crear el árbol de archivos
crear_arbol(ruta)
