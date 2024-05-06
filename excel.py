import pandas as pd

def procesar_archivo_excel(archivo_entrada, archivo_salida):
    # Leer el archivo Excel
    df = pd.read_excel(archivo_entrada)

    # Crear una copia del DataFrame original para la hoja con registros originales
    df_originales = df.copy()

    # Identificar los duplicados basados en "LINEA" y "DESCRIPCION"
    duplicados = df.duplicated(subset=["LINEA", "DESCRIPCION"], keep="first")

    # Filtrar los duplicados y obtener las filas a eliminar
    df_eliminados = df_originales[duplicados]

    # Crear una columna nueva para indicar en qué fila se repite cada registro eliminado
    df_eliminados["Fila Repetida"] = df[duplicados].index + 2

    # Eliminar duplicados basados en "LINEA" y "DESCRIPCION" manteniendo solo el primer registro
    df = df.drop_duplicates(subset=["LINEA", "DESCRIPCION"], keep="first")

    # Escribir el resultado en un nuevo archivo Excel con tres hojas
    with pd.ExcelWriter(archivo_salida, engine="xlsxwriter") as writer:
        df_eliminados.to_excel(writer, sheet_name="Elementos Eliminados", index=False)
        df.to_excel(writer, sheet_name="Registros Originales", index=False)

if __name__ == "__main__":
    archivo_entrada = r"C:\Users\acapaizlo\Desktop\HOJA2.xlsx"
    archivo_salida = r"C:\Users\acapaizlo\Desktop\HOJA2_salida.xlsx"

    procesar_archivo_excel(archivo_entrada, archivo_salida)

    print("Proceso completado. Revise el archivo de salida.")
