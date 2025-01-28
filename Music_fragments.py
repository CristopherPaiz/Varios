import os
import json
import glob
from pydub import AudioSegment
from pydub.utils import mediainfo
from mutagen.mp3 import MP3
from PIL import Image

def process_mp3_files(source_folder):
    # Obtener la lista de archivos mp3 en la carpeta de origen
    mp3_files = glob.glob(os.path.join(source_folder, "*.mp3"))

    # Crear una lista para almacenar las canciones procesadas
    processed_songs = []

    # Recorrer cada archivo mp3
    print("\n\n########################## **PROCESANDO ARCHIVOS MP3** ##########################")
    for mp3_file in mp3_files:
        # Leer la metadata del archivo mp3
        metadata = mediainfo(mp3_file)

        # Obtener los atributos de la canción
        title = metadata["TAG"]["title"]
        artist = metadata["TAG"]["artist"]
        length = str(metadata["duration"])
        album = metadata["TAG"]["album"]
        date = metadata["TAG"]["date"]

        # Crear la carpeta del artista si no existe
        artist_folder = os.path.join(source_folder, artist)
        if not os.path.exists(artist_folder):
            os.makedirs(artist_folder)

        # Crear la carpeta de la canción dentro de la carpeta del artista
        song_folder = os.path.join(artist_folder, title)
        if not os.path.exists(song_folder):
            os.makedirs(song_folder)

        # Leer el archivo de audio
        audio = AudioSegment.from_file(mp3_file, format="mp3")

        # Extraer la carátula del álbum
        audio_file = MP3(mp3_file)
        coverart = audio_file.tags.getall('APIC')[0]
        if coverart:
            with open(os.path.join(song_folder, "cover.jpg"), "wb") as img:
                img.write(coverart.data)
            # Convertir la imagen a webp y cambiar su tamaño
            image_path = os.path.join(song_folder, "cover.jpg")
            image = Image.open(image_path)
            image = image.resize((400, 400))
            image.save(os.path.join(song_folder, "cover.webp"), "webp")

        # Dividir la canción en fragmentos de 10 segundos
        segments = len(audio) // 10000
        fragment_names = []
        print("")
        for i in range(segments):
            print(f"\rProcesando {len(processed_songs) + 1}/{len(mp3_files)}: {artist} - {title} [{i+1}/{segments}]", end="    ")
            fragment_name = f"{i+1}"
            fragment_names.append(fragment_name)
            start_time = i * 10000
            end_time = (i + 1) * 10000
            audio_segment = audio[start_time:end_time]
            audio_segment.export(os.path.join(song_folder, f"{fragment_name}.mp3"), format="mp3", tags=metadata)

        # Calcular la duración del último fragmento
        last_fragment_duration = len(audio) % 10000

        # Si la duración del último fragmento es menor a 10 segundos, ajustarla
        if last_fragment_duration < 10000:
            fragment_name = f"{segments + 1}"
            fragment_names.append(fragment_name)
            start_time = segments * 10000
            end_time = len(audio)
            audio_segment = audio[start_time:end_time]
            audio_segment.export(os.path.join(song_folder, f"{fragment_name}.mp3"), format="mp3", tags=metadata)

            # Actualizar el número de fragmentos
            segments += 1

        # Agregar la canción procesada a la lista
        processed_song = {
            "id": len(processed_songs) + 1,
            "title": title,
            "artist": artist,
            "length": length,
            "album": album,
            "date": date,
            "fragments": len(fragment_names)
        }
        processed_songs.append(processed_song)

        # Eliminar la imagen de la carátula
        os.remove(image_path)

    # Guardar la lista de canciones procesadas en un archivo JSON
    json_file = os.path.join(source_folder, "ricardoArjona.json")
    with open(json_file, "w") as f:
        json.dump(processed_songs, f, indent=4)

    print("\n\n########################## **COMPLETADO** ##########################\n\n")

# Ruta de la carpeta que contiene los archivos mp3
source_folder = r"C:\Users\acapaizlo\Downloads\DeemixDownloads\Melendi"

# Llamar a la función para procesar los archivos mp3
process_mp3_files(source_folder)
