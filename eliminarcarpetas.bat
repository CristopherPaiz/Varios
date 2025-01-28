@echo off
setlocal enabledelayedexpansion

set "bucketName=music-fragments"
set "folderName=Audio_Hebreo"
set "url=https://s3.fr-par.scw.cloud"

echo Borrando la carpeta %folderName% y todo su contenido del bucket %bucketName%...

aws s3 rm s3://%bucketName%/%folderName% --recursive --endpoint-url "%url%"

if %errorlevel% equ 0 (
    echo La carpeta %folderName% y su contenido han sido eliminados exitosamente.
) else (
    echo Hubo un error al intentar borrar la carpeta %folderName%. Por favor, verifica tus credenciales y conexión.
)

pause