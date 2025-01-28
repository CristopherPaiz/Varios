import os
import json
import re
import xml.etree.ElementTree as ET

def process_xml(xml_path, output_dir):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        bible_name = sanitize(root.attrib.get('name', 'UnknownBible'))
        bible_translation = sanitize(root.attrib.get('translation', 'UnknownTranslation'))
        bible_translation_number = sanitize(root.attrib.get('translationumber', ''))
        bible_language = sanitize(root.attrib.get('language', 'UnknownLanguage'))

        output_bible_dir = os.path.join(output_dir, f"{bible_name}_{bible_translation}_{bible_translation_number}_{bible_language}")
        os.makedirs(output_bible_dir, exist_ok=True)

        testaments = root.findall('./testament')

        for testament in testaments:
            testament_name = sanitize(testament.attrib.get('name', 'UnknownTestament'))

            testament_dir = os.path.join(output_bible_dir, testament_name)
            os.makedirs(testament_dir, exist_ok=True)

            for book in testament.findall('./book'):
                book_number = book.attrib.get('number')
                book_dir = os.path.join(testament_dir, f"book{book_number}")
                os.makedirs(book_dir, exist_ok=True)

                for chapter in book.findall('./chapter'):
                    chapter_number = chapter.attrib.get('number')
                    chapter_json = {}

                    for verse in chapter.findall('./verse'):
                        verse_number = verse.attrib.get('number')
                        verse_text = verse.text.strip() if verse.text else ""
                        chapter_json[verse_number] = verse_text

                    chapter_json_path = os.path.join(book_dir, f"chapter{chapter_number}.json")
                    with open(chapter_json_path, 'w', encoding='utf-8') as json_file:
                        json.dump(chapter_json, json_file, indent=2, ensure_ascii=False)

        print(f"Procesado archivo XML: {xml_path}")

    except Exception as e:
        print(f"Error al procesar el archivo XML: {xml_path}")
        print(f"Error: {str(e)}")

def sanitize(text):
    # Reemplazar caracteres no alfanuméricos por guiones bajos
    return re.sub(r'\W+', '_', text)

# Ruta de la carpeta con los archivos XML
input_dir = "C:\\Users\\acapaizlo\\Downloads\\Holy-Bible-XML-Format-master"

# Ruta de la carpeta de salida
output_dir = os.path.join(input_dir, "output")
os.makedirs(output_dir, exist_ok=True)

# Procesamiento de los archivos XML
for file_name in os.listdir(input_dir):
    if file_name.endswith(".xml"):
        xml_path = os.path.join(input_dir, file_name)
        process_xml(xml_path, output_dir)

print("############################## Proceso completado ##############################")