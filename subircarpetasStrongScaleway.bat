$bucketName = "music-fragments"
>> $url = "https://s3.fr-par.scw.cloud"
>> $folder1 = "C:\Users\acapaizlo\Desktop\Proyectos\Varios\multi-bible-compare\src\assets\strongs\Audio_Griego"
>> $folder2 = "C:\Users\acapaizlo\Desktop\Proyectos\Varios\multi-bible-compare\src\assets\strongs\Audio_Hebreo"
>> $maxParallelJobs = 20
>>
>> function Upload-Folder($folderPath, $folderName) {
>>     $files = Get-ChildItem $folderPath -Filter *.mp3
>>     $uploadedFiles = @()
>>
>>     foreach ($file in $files) {
>>         # Limitar a $maxParallelJobs trabajos en paralelo
>>         while ((Get-Job | Where-Object { $_.State -eq 'Running' }).Count -ge $maxParallelJobs) {
>>             Start-Sleep -Seconds 1
>>
>>             # Mostrar estado actual de trabajos activos
>>             $runningJobs = Get-Job | Where-Object { $_.State -eq 'Running' }
>>             Write-Host "Trabajos activos: $($runningJobs.Count)"
>>             foreach ($job in $runningJobs) {
>>                 Write-Host "  - Procesando: $($job.Name)"
>>             }
>>         }
>>
>>         # Iniciar un nuevo trabajo en paralelo
>>         $jobName = $file.Name
>>         Start-Job -Name $jobName -ScriptBlock {
>>             param ($filePath, $fileName, $bucketName, $folderName, $url)
>>             aws s3api put-object --bucket $bucketName --body $filePath --key "$folderName/$fileName" --acl public-read --endpoint-url $url --output text
>>             Write-Output $fileName
>>         } -ArgumentList $file.FullName, $file.Name, $bucketName, $folderName, $url
>>     }
>>
>>     # Monitorear trabajos activos y mostrar los archivos subidos en tiempo real
>>     while ((Get-Job).Count -gt 0) {
>>         $completedJobs = Get-Job | Where-Object { $_.State -eq 'Completed' }
>>
>>         foreach ($job in $completedJobs) {
>>             $output = Receive-Job -Job $job
>>             Write-Host "Subido: $output"
>>             $uploadedFiles += $output
>>             Remove-Job -Job $job
>>         }
>>
>>         $runningJobs = Get-Job | Where-Object { $_.State -eq 'Running' }
>>         Write-Host "Trabajos activos: $($runningJobs.Count)"
>>         foreach ($job in $runningJobs) {
>>             Write-Host "  - Procesando: $($job.Name)"
>>         }
>>
>>         Start-Sleep -Seconds 1
>>     }
>> }
>>
>> # Subir los archivos en paralelo desde ambas carpetas
>> Upload-Folder $folder2 "Audio_Hebreo"