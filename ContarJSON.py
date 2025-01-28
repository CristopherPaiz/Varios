import json

# Ruta del archivo JSON
json_file = r'C:\Users\acapaizlo\Desktop\test.json'

# Leer el archivo JSON
with open(json_file) as file:
    data = json.load(file)

# Obtener el array de consultaFecha
consulta_fecha = data.get('consultaFecha', [])

# Contar la cantidad de objetos en el array
cantidad_objetos = len(consulta_fecha)

# Imprimir el resultado
print(f"La cantidad de objetos en el array consultaFecha es: {cantidad_objetos}")
