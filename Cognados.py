import sqlite3
import json

# Ruta del archivo SQLite3
db_path = r'C:\Users\acapaizlo\Desktop\Cosas varias\Bibles\Varios\Español - Cognados Chávez-Tuggy-Vine-Swanson.SQLite3'

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Consulta para obtener todos los valores de la tabla 'cognate_strong_numbers'
query = 'SELECT group_id, strong_number FROM cognate_strong_numbers'
cursor.execute(query)

# Crear un diccionario para almacenar los resultados agrupados
result = {}

# Iterar sobre las filas obtenidas
for row in cursor.fetchall():
    group_id = row[0]
    strong_number = row[1]

    if group_id not in result:
        result[group_id] = []

    result[group_id].append(strong_number)

# Cerrar la conexión a la base de datos
conn.close()

# Convertir el diccionario a formato JSON minificado
json_result = json.dumps(result, separators=(',', ':'))

# Guardar el resultado en un archivo JSON
output_path = r'C:\Users\acapaizlo\Desktop\Cognates_Grouped_Minified.json'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(json_result)

print(f"Minified JSON result saved to {output_path}")
