pyinstaller --noconfirm --onefile --windowed src/main.py
Rename-Item -Path dist\main.exe -NewName PendriveGuardian.exe
Write-Host "PendriveGuardian.exe built successfully"
