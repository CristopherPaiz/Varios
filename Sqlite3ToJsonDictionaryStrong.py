import sqlite3
import json
from bs4 import BeautifulSoup  # Para procesar HTML
from bs4 import NavigableString

# Conectarse a la base de datos
conn = sqlite3.connect(r"C:\Users\acapaizlo\Desktop\strong.SQLite3")
cursor = conn.cursor()

# Consulta SQL para seleccionar todos los datos de la tabla "dictionary"
cursor.execute("SELECT * FROM dictionary")

# Obtener todos los resultados
results = cursor.fetchall()

print(results)
# # Cerrar la conexión a la base de datos
# conn.close()

# # Función para procesar la definición y extraer título, pronunciación y descripción
# def process_definition(definition):
#     soup = BeautifulSoup(definition, 'html.parser')
#     title_tag = soup.find('b')
#     pron_tag = soup.find('font', {'color': '%COLOR_PURPLE%'})

#     title = title_tag.get_text() if title_tag else None
#     pron = pron_tag.get_text() if pron_tag else None

#     # Eliminar las etiquetas de título y pronunciación de la descripción
#     if title_tag:
#         title_tag.extract()
#     if pron_tag:
#         pron_tag.extract()

#     # Modificar etiquetas <a> en la descripción si existen
#     if soup.find('a'):
#         for a_tag in soup.find_all('a'):
#             href_value = a_tag.get('href')  # Obtener el valor del atributo href
#             if href_value:
#                 # Verificar si href_value contiene 'S:'
#                 if 'S:' in href_value:
#                     # Extraer el valor después de 'S:'
#                     link_value = href_value.split('S:')[1]
#                 else:
#                     link_value = ''  # Valor predeterminado si 'S:' no está presente
#                 # Crear el nuevo span y reemplazar la etiqueta <a>}
#                 datos = "onClick={strongFun('"+link_value+"')}"
#                 # span_tag = soup.new_tag('span', **{'color': '%COLOR_BLUE%'})
#                 # span_tag.string = a_tag.string
#                 # span_tag.append(soup.new_string(datos))
#                 # a_tag.replace_with(span_tag)
#                 html = f"<span color='%COLOR_BLUE%' {datos}>{a_tag.string}</span>"
#                 a_tag.replace_with(NavigableString(html))


#     desc = str(soup)
#     return {"pron": pron, "desc": desc}

# # Convertir los resultados a formato JSON
# json_data = []
# for row in results:
#     definition_data = process_definition(row[1])  # Procesar la definición
#     definition_data = {k.replace('"', "'"): v.replace('"', "'") if isinstance(v, str) else v for k, v in definition_data.items()}  # Reemplazar comillas
#     data = {
#         "id": row[0],
#         # "ti": row[3],
#         "le": row[2],
#         "pl": definition_data["pron"],
#         # "ps": row[4],
#         # "df": definition_data["desc"],
#     }
#     json_data.append(data)

# # Escribir los datos JSON en un archivo con codificación UTF-8 para manejar caracteres especiales
# with open("datos.json", "w", encoding="utf-8") as json_file:
#     json.dump(json_data, json_file, ensure_ascii=False, separators=(',', ':'))

# print("Datos extraídos y guardados en datos.json")
