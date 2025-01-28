import requests
import time
import os
from tqdm import tqdm

def descargar_archivo(url, ruta_destino):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.bibliatodo.com/'
    }
    response = requests.get(url, headers=headers, stream=True)
    response.raise_for_status()
    with open(ruta_destino, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

def main():
    base_url = "https://www.bibliatodo.com/assets/audio/strong/greek/{}.mp3"
    ruta_destino = r"C:\Users\acapaizlo\Desktop\Proyectos\Varios\multi-bible-compare\src\assets\strongs\Audio_Griego"

    os.makedirs(ruta_destino, exist_ok=True)

    archivos_no_descargados = []

    rangos = list(range(1, 5624))

    for numero in tqdm(rangos, desc="Descargando archivos"):
        url = base_url.format(numero)
        archivo_destino = os.path.join(ruta_destino, f"{numero}.mp3")

        try:
            descargar_archivo(url, archivo_destino)
        except requests.exceptions.RequestException as e:
            print(f"No se pudo descargar el archivo {numero}: {str(e)}")
            archivos_no_descargados.append(numero)

        time.sleep(0)  # Aumentamos el tiempo de espera a 0.5 segundos

    with open(os.path.join(ruta_destino, "archivos_no_descargados.txt"), "w") as f:
        for numero in archivos_no_descargados:
            f.write(f"{numero}\n")

    print("Proceso de descarga completado.")
    print(f"Archivos no descargados: {len(archivos_no_descargados)}")

if __name__ == "__main__":
    main()