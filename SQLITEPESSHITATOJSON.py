import sqlite3
import json
import os
import re

# Ruta de la carpeta principal
PATH = 'C:\\Users\\acapaizlo\\Desktop\\Browser\\BibliasProcesadas'

# Crear la carpeta principal si no existe
if not os.path.exists(PATH):
    os.makedirs(PATH)

# Ruta de la carpeta de origen de los archivos SQLite3
source_folder = 'C:\\Users\\acapaizlo\\Desktop\\Browser\\Biblias'

# Obtener la lista de archivos SQLite3 en la carpeta de origen
file_list = [f for f in os.listdir(source_folder) if f.endswith('.SQLite3')]

try:
    # Procesar cada archivo
    for file_name in file_list:
        # Obtener el nombre del archivo sin la extensión
        file_name_without_extension = os.path.splitext(file_name)[0]

        # Obtener el número de tres dígitos para el nombre de la carpeta
        folder_number = file_list.index(file_name) + 1
        folder_number_padded = str(folder_number).zfill(3)

        # Crear la carpeta correspondiente al archivo
        file_folder = f'{PATH}\\{folder_number_padded}. {file_name_without_extension}'
        if not os.path.exists(file_folder):
            os.makedirs(file_folder)

        # Conexión a la base de datos
        conn = sqlite3.connect(os.path.join(source_folder, file_name))
        cursor = conn.cursor()

        # Consulta para contar libros diferentes
        cursor.execute("SELECT COUNT(DISTINCT book_number) FROM verses")
        count = cursor.fetchone()[0]

        # Consulta a la base de datos
        cursor.execute("SELECT * FROM verses")
        rows = cursor.fetchall()

        if count == 66 or count == 39 or count == 27:
            print(f'Procesando {folder_number_padded}. {file_name_without_extension}...', f"Número de libros: {count}")
            # Procesar las filas de la base de datos}
            for row in rows:
                book_number, chapter, verse, text = row
                try:
                    # Aplicar el regex para eliminar el href y la URL del texto si existe
                    if text:
                        text = re.sub(r'href=".*?"', '', text)
                        text = re.sub(r'<S>', '<sup>', text)
                        text = re.sub(r'<s>', '<sup>', text)
                        text = re.sub(r'</S>', ' </sup>', text)
                        text = re.sub(r'</s>', ' </sup>', text)


                    # # Crear la carpeta del libro si no existe
                    if book_number > (39 * 10):
                        book_folder = f'{file_folder}\\New\\book{(int(book_number/10))}'
                    else:
                        book_folder = f'{file_folder}\\Old\\book{(int(book_number/10))}'

                    if not os.path.exists(book_folder):
                        os.makedirs(book_folder)

                    # Crear el archivo del capítulo si no existe y escribir el versículo
                    chapter_file = f'{book_folder}\\chapter{chapter}.json'

                    # Verificar si el archivo del capítulo ya existe
                    if os.path.exists(chapter_file):
                        # Cargar el contenido actual del archivo del capítulo
                        with open(chapter_file, 'r', encoding='utf-8') as f:
                            chapter_data = json.load(f)
                    else:
                        chapter_data = {}

                    # Agregar el versículo al capítulo
                    chapter_data[verse] = text

                    # Escribir el contenido actualizado en el archivo del capítulo
                    with open(chapter_file, 'w', encoding='utf-8') as f:
                        json.dump(chapter_data, f, ensure_ascii=False)


                except Exception as e:
                    None
            # Cerrar la conexión a la base de datos
            conn.close()
        else:
            print(f'Libro omitido {file_name_without_extension}...', f"Número de libros: {count}")

except Exception as e:
    print(e)
