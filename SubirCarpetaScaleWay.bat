@echo off
setlocal enabledelayedexpansion

set "nameFolder=Melendi"

set "rootFolder=C:\Users\acapaizlo\Downloads\DeemixDownloads\music\%nameFolder%"
set "bucketName=music-fragments"
set "url=https://s3.fr-par.scw.cloud"

@REM First, handle files in the root folder
for %%f in ("%rootFolder%\*") do (
    echo subiendo: %%~nxf
    aws s3api put-object --bucket %bucketName% --body "%rootFolder%\%%~nxf" --key "%nameFolder%/%%~nxf" --acl public-read --endpoint-url "%url%" --output text
    echo ---------------------------------
)

@REM Then, handle files in subfolders
for /R "%rootFolder%" %%f in (*) do (
    set "path=%%~dpf"
    set "path=!path:%rootFolder%\=!"
    for /f "tokens=1,2 delims=\" %%a in ("!path!") do (
        if "%%b"=="" (
            echo No pasa nada
        ) else (
            echo Subiendo: %nameFolder%/%%a/%%b/%%~nxf
            "C:\Program Files\Amazon\AWSCLIV2\aws.exe" s3api put-object --bucket !bucketName! --body "!rootFolder!\%%a\%%b\%%~nxf" --key "!nameFolder!/%%a/%%b/%%~nxf" --acl public-read --endpoint-url "!url!" 2>&1
            echo ---------------------------------
        )
    )
)
pause