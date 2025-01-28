import os
import json
from xml.dom import minidom

# Ruta de la carpeta que contiene los archivos XML
folder_path = r'C:\Users\acapaizlo\Downloads\Varios\Holy-Bible-XML-Format-master\xml'

# Diccionario para almacenar los resultados
result = {}

# Itera sobre cada archivo en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith('.xml'):
        file_path = os.path.join(folder_path, filename)
        print(f"Procesando archivo: {filename}")  # Imprime el nombre del archivo

        try:
            # Analiza el archivo XML
            doc = minidom.parse(file_path)

            # Busca la etiqueta <bible>
            bible_tags = doc.getElementsByTagName('bible')

            if bible_tags:
                attributes = []
                for bible_tag in bible_tags:
                    # Extrae los atributos de la etiqueta <bible>
                    for attr in bible_tag.attributes.values():
                        # Almacena el valor sin alterar
                        attributes.append(f"{attr.name}='{attr.value}'")

                # Une los atributos y agrega al diccionario
                result[filename[:-4]] = ', '.join(attributes)  # Sin la extensión .xml
                print(f"Atributos encontrados en {filename}: {result[filename[:-4]]}")
            else:
                print(f"No se encontró la etiqueta <bible> en: {filename}")

        except Exception as e:
            print(f"Se produjo un error con el archivo {filename}: {e}")

# Guarda el resultado en un archivo JSON
with open('bibles.json', 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, ensure_ascii=False, indent=4)

print("Los datos se han guardado en bibles.json")
print("Resultado final:", result)  # Muestra el resultado final
