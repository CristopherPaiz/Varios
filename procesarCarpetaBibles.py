# import os
# import json

# def procesar_carpeta(carpeta_raiz):
#     estructura = {}

#     for carpeta_nombre in os.listdir(carpeta_raiz):
#         print(f"Procesando carpeta {carpeta_nombre}...")
#         carpeta_path = os.path.join(carpeta_raiz, carpeta_nombre)

#         if os.path.isdir(carpeta_path):
#             new_exist = False
#             old_exist = False

#             for subcarpeta_nombre in os.listdir(carpeta_path):
#                 subcarpeta_path = os.path.join(carpeta_path, subcarpeta_nombre)

#                 if os.path.isdir(subcarpeta_path):
#                     if subcarpeta_nombre == "New":
#                         new_exist = True
#                     elif subcarpeta_nombre == "Old":
#                         old_exist = True

#             estructura[carpeta_nombre] = {
#                 "ruta": "../assets/bibles/" + carpeta_nombre,
#                 "new": new_exist,
#                 "old": old_exist
#             }

#             if new_exist:
#                 estructura[carpeta_nombre]["NewTestament"] = procesar_testamento(os.path.join(carpeta_path, "New"))

#             if old_exist:
#                 estructura[carpeta_nombre]["OldTestament"] = procesar_testamento(os.path.join(carpeta_path, "Old"))

#     return estructura

# def procesar_testamento(testamento_path):
#     testamento = {}

#     for book_nombre in os.listdir(testamento_path):
#         if book_nombre.startswith("book"):
#             book_path = os.path.join(testamento_path, book_nombre)
#             testamento[book_nombre] = procesar_libro(book_path)

#     return testamento

# def procesar_libro(libro_path):
#     capitulos = {}

#     for archivo_nombre in os.listdir(libro_path):
#         if archivo_nombre.startswith("chapter"):
#             capitulo_path = os.path.join(libro_path, archivo_nombre)
#             capitulo_content = procesar_capitulo(capitulo_path)
#             capitulos[archivo_nombre.split(".")[0]] = capitulo_content

#     return capitulos

# def procesar_capitulo(capitulo_path):
#     with open(capitulo_path, "r", encoding="utf-8") as capitulo_file:
#         capitulo_data = json.load(capitulo_file)

#     return list(capitulo_data.keys())

# carpeta_raiz = r"C:\Users\acapaizlo\Downloads\Holy-Bible-XML-Format-master\bibles"
# estructura_json = procesar_carpeta(carpeta_raiz)

# ruta_json = os.path.join(carpeta_raiz, "estructura.json")
# with open(ruta_json, "w", encoding="utf-8") as outfile:
#     json.dump(estructura_json, outfile, ensure_ascii=False, indent=4)

# print(f"Proceso completado. Se ha generado el archivo estructura.json en {ruta_json}.")

################################################
# import os
# import json

# def procesar_carpeta(carpeta_raiz):
#     estructura = {}

#     for carpeta_nombre in os.listdir(carpeta_raiz):
#         print(f"Procesando carpeta {carpeta_nombre}...")
#         carpeta_path = os.path.join(carpeta_raiz, carpeta_nombre)

#         if os.path.isdir(carpeta_path):
#             new_exist = False
#             old_exist = False

#             for subcarpeta_nombre in os.listdir(carpeta_path):
#                 subcarpeta_path = os.path.join(carpeta_path, subcarpeta_nombre)

#                 if os.path.isdir(subcarpeta_path):
#                     if subcarpeta_nombre == "New":
#                         new_exist = True
#                     elif subcarpeta_nombre == "Old":
#                         old_exist = True

#             estructura[carpeta_nombre] = {
#                 "ruta": "../assets/bibles/" + carpeta_nombre,
#                 "new": new_exist,
#                 "old": old_exist
#             }

#             if new_exist:
#                 estructura[carpeta_nombre]["NewTestament"] = procesar_testamento(os.path.join(carpeta_path, "New"))

#             if old_exist:
#                 estructura[carpeta_nombre]["OldTestament"] = procesar_testamento(os.path.join(carpeta_path, "Old"))

#     return estructura

# def procesar_testamento(testamento_path):
#     testamento = {}

#     for book_nombre in os.listdir(testamento_path):
#         if book_nombre.startswith("book"):
#             book_path = os.path.join(testamento_path, book_nombre)
#             testamento[book_nombre] = procesar_libro(book_path)

#     return testamento

# def procesar_libro(libro_path):
#     capitulos = {}

#     for archivo_nombre in os.listdir(libro_path):
#         if archivo_nombre.startswith("chapter"):
#             capitulo_path = os.path.join(libro_path, archivo_nombre)
#             capitulo_content = procesar_capitulo(capitulo_path)
#             capitulos[archivo_nombre.split(".")[0]] = capitulo_content

#     return capitulos

# def procesar_capitulo(capitulo_path):
#     with open(capitulo_path, "r", encoding="utf-8") as capitulo_file:
#         capitulo_data = json.load(capitulo_file)

#     return list(capitulo_data.keys())

# carpeta_raiz = r"C:\Users\acapaizlo\Downloads\Holy-Bible-XML-Format-master\bibles"
# estructura_json = procesar_carpeta(carpeta_raiz)

# # Crear carpeta para archivos JSON finales
# json_final_path = os.path.join(carpeta_raiz, "JSON_FINAL")
# os.makedirs(json_final_path, exist_ok=True)

# # Generar archivos JSON para cada carpeta en el root
# for carpeta_nombre, contenido in estructura_json.items():
#     json_carpeta_path = os.path.join(json_final_path, f"{carpeta_nombre}.json")
#     with open(json_carpeta_path, "w", encoding="utf-8") as json_file:
#         json.dump(contenido, json_file, ensure_ascii=False, indent=4)
#         print(f"Archivo JSON para la carpeta {carpeta_nombre} creado en {json_carpeta_path}")

# print(f"Proceso completado. Se han generado los archivos JSON en {json_final_path}.")


import os
import json

def procesar_carpeta(carpeta_raiz):
    estructura = {}

    for carpeta_nombre in os.listdir(carpeta_raiz):
        print(f"Procesando carpeta {carpeta_nombre}...")
        carpeta_path = os.path.join(carpeta_raiz, carpeta_nombre)

        if os.path.isdir(carpeta_path):
            new_exist = False
            old_exist = False

            for subcarpeta_nombre in os.listdir(carpeta_path):
                subcarpeta_path = os.path.join(carpeta_path, subcarpeta_nombre)

                if os.path.isdir(subcarpeta_path):
                    if subcarpeta_nombre == "New":
                        new_exist = True
                    elif subcarpeta_nombre == "Old":
                        old_exist = True

            estructura[carpeta_nombre] = {
                "ruta": "../assets/bibles/" + carpeta_nombre,
                "new": new_exist,
                "old": old_exist
            }

            if new_exist:
                estructura[carpeta_nombre]["NewTestament"] = procesar_testamento(os.path.join(carpeta_path, "New"))

            if old_exist:
                estructura[carpeta_nombre]["OldTestament"] = procesar_testamento(os.path.join(carpeta_path, "Old"))

    return estructura

def procesar_testamento(testamento_path):
    testamento = {}

    for book_nombre in os.listdir(testamento_path):
        if book_nombre.startswith("book"):
            book_path = os.path.join(testamento_path, book_nombre)
            testamento[book_nombre] = procesar_libro(book_path)

    return testamento

def procesar_libro(libro_path):
    capitulos = {}

    for archivo_nombre in os.listdir(libro_path):
        if archivo_nombre.startswith("chapter"):
            capitulo_path = os.path.join(libro_path, archivo_nombre)
            capitulo_content = procesar_capitulo(capitulo_path)
            capitulos[int(archivo_nombre.split(".")[0].replace("chapter", ""))] = capitulo_content

    return capitulos

def procesar_capitulo(capitulo_path):
    with open(capitulo_path, "r", encoding="utf-8") as capitulo_file:
        capitulo_data = json.load(capitulo_file)

    return [int(key) for key in capitulo_data.keys()]

carpeta_raiz = r"C:\Users\acapaizlo\Downloads\Holy-Bible-XML-Format-master\bibles"
estructura_json = procesar_carpeta(carpeta_raiz)

# Crear carpeta para archivos JSON finales
json_final_path = os.path.join(carpeta_raiz, "JSON_FINAL")
os.makedirs(json_final_path, exist_ok=True)

# Generar archivos JSON minificados para cada carpeta en el root
for carpeta_nombre, contenido in estructura_json.items():
    json_carpeta_path = os.path.join(json_final_path, f"{carpeta_nombre}.json")
    with open(json_carpeta_path, "w", encoding="utf-8") as json_file:
        json.dump(contenido, json_file, separators=(",", ":"), ensure_ascii=False)
        print(f"Archivo JSON para la carpeta {carpeta_nombre} creado en {json_carpeta_path}")

print(f"Proceso completado. Se han generado los archivos JSON en {json_final_path}.")
