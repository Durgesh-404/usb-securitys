$exeName = 'PendriveGuardian.exe'
$sourcePath = Join-Path -Path (Get-Location) -ChildPath $exeName
$installDir = 'C:\Program Files\PendriveGuardian'
if (-Not (Test-Path $installDir)) { New-Item -ItemType Directory -Path $installDir | Out-Null }
Copy-Item -Path $sourcePath -Destination (Join-Path $installDir $exeName) -Force
$WshShell = New-Object -ComObject WScript.Shell
$startMenu = [Environment]::GetFolderPath('Programs')
$shortcutPath = Join-Path $startMenu 'Pendrive Guardian.lnk'
$shortcut = $WshShell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = Join-Path $installDir $exeName
$shortcut.WorkingDirectory = $installDir
$shortcut.Save()
Write-Host "Installation complete."
