import os
import boto3
import concurrent.futures

# Configuración de AWS S3
bucket_name = "music-fragments"
folder_name = "Audio_Hebreo"
local_folder = r"C:\Users\acapaizlo\Desktop\Proyectos\Varios\multi-bible-compare\src\assets\strongs\Audio_Hebreo"
max_prints = 100
current_prints = 0

# Inicializa el cliente de S3 con el endpoint de Scaleway
s3_client = boto3.client('s3',
                          endpoint_url='https://s3.fr-par.scw.cloud',
                          aws_access_key_id='SCWZPHME4GSVSM182JCQ',
                          aws_secret_access_key='0db5d743-db4b-4a82-8733-fb71b73214c0',
                          region_name='fr-par')

def upload_file(file_path):
    global current_prints
    file_name = os.path.basename(file_path)
    key = f"{folder_name}/{file_name}"  # Clave en S3

    try:
        # Subir el archivo
        s3_client.upload_file(file_path, bucket_name, key, ExtraArgs={'ACL': 'public-read'})
        return file_name
    except Exception as e:
        return f"Error: {e}"

def main():
    global current_prints
    files = [os.path.join(local_folder, f) for f in os.listdir(local_folder) if f.endswith('.mp3')]

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_file = {executor.submit(upload_file, file): file for file in files}

        for future in concurrent.futures.as_completed(future_to_file):
            result = future.result()
            if "Error" not in result:
                print(f"Subido: {result}")
                current_prints += 1

                # Limpiar la consola automáticamente al alcanzar 100 prints
                if current_prints >= max_prints:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    current_prints = 0
            else:
                print(f"Error al subir {future_to_file[future]}: {result}")

if __name__ == "__main__":
    main()
