#######################################################################################################################
############################# SE INSTALA EL PAQUETE PyPDF2: pip install PyPDF2  #######################################
#######################################################################################################################

import os
from PyPDF2 import PdfMerger

# Especifica la carpeta que contiene los archivos PDF
carpeta_pdf = 'C:\\Users\\acapaizlo\\Desktop\\informes\\Todos los informes 2024'

# Listar todos los archivos PDF en la carpeta
pdfs = [f for f in os.listdir(carpeta_pdf) if f.endswith('.pdf')]

# Ordenar alfabéticamente los archivos PDF
pdfs.sort()

# Crear el objeto PdfMerger
merger = PdfMerger()

# Añadir cada PDF en orden alfabético
for pdf in pdfs:
    pdf_path = os.path.join(carpeta_pdf, pdf)
    merger.append(pdf_path)

# Guardar el PDF final fusionado
output_path = os.path.join(carpeta_pdf, "result.pdf")
merger.write(output_path)
merger.close()

print(f"Se ha generado el archivo result.pdf en: {output_path}")

# Abrir el PDF final fusionado
os.startfile(output_path)
