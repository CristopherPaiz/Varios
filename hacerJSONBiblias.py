import os
import json

def obtener_info_carpetas(ruta):
    carpetas = os.listdir(ruta)
    resultado = {}

    for carpeta in carpetas:
        ruta_carpeta = os.path.join(ruta, carpeta)
        if os.path.isdir(ruta_carpeta):
            nombre = carpeta.split("- ")[1]
            new = os.path.isdir(os.path.join(ruta_carpeta, "New"))
            old = os.path.isdir(os.path.join(ruta_carpeta, "Old"))
            year = carpeta.split(" (")[1].split(")")[0]
            resultado[nombre] = {
                "ruta": carpeta,
                "new": new,
                "old": old,
                "year": year
            }

    return resultado

ruta_base = r"C:\Users\acapaizlo\Desktop\Browser\BibliasProcesadas"
resultado = obtener_info_carpetas(ruta_base)

json_resultado = json.dumps(resultado, indent=4, ensure_ascii=False)
print(json_resultado)
