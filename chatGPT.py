import os
import json

# Ruta del archivo de entrada
ruta_entrada = r"C:\Users\acapaizlo\Desktop\Proyectos\datos.json"

# Ruta de la carpeta de salida
ruta_salida = r"C:\Users\acapaizlo\Desktop\Proyectos\Varios\multi-bible-compare\src\assets\strongs\Hebreo"

# Leer el archivo de entrada
with open(ruta_entrada, 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

# Crear una lista para almacenar los elementos procesados
elementos_procesados = []

# Procesar cada objeto en el array de objetos
for i, objeto in enumerate(datos, start=1):
    # Obtener el valor del campo "id"
    id_valor = objeto["id"]

    # Quitar la letra "H" del valor de "id"
    numero = id_valor[1:]

    # Agregar el objeto procesado a la lista
    elementos_procesados.append(objeto)

    # Exportar los elementos cada 150 elementos
    if i % 150 == 0 or i == len(datos):
        # Calcular el rango de los elementos en el archivo
        inicio = (i // 150 - 1) * 150 + 1
        fin = i

        # Crear el nombre del archivo de salida
        nombre_archivo = f"{str(inicio).zfill(4)}-{str(fin).zfill(4)}.json"

        # Crear el archivo de salida
        ruta_archivo_salida = os.path.join(ruta_salida, nombre_archivo)
        with open(ruta_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
            json.dump(elementos_procesados, archivo_salida, ensure_ascii=False)

        # Reiniciar la lista de elementos procesados
        elementos_procesados = []
