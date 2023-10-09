$url = "https://github.com/NoirBird/IDM-Trial-Reset/releases/download/Release/NoirBird-IDM-Reset.exe"
$tempFilePath = [System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), "NoirBird-IDM-Reset.exe")
Invoke-WebRequest -Uri $url -OutFile $tempFilePath
if (Test-Path $tempFilePath) {
    try {
        Start-Process -FilePath $tempFilePath -Wait
        Remove-Item -Path $tempFilePath -Force
        Write-Output "https://github.com/NoirBird/IDM-Trial-Reset"
    }
    catch {
        Write-Error "Error occurred: $_"
    }
}
else {
    Write-Error "Failed to download the file."
}
