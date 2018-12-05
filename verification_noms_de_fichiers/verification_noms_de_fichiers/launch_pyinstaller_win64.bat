:1.Lance la compilation du code source
:2. Nettoie le répertoire build, renomme dist en "verification_noms_de_fichiers" et y place le raccourci pour le lancement du fichier
:3. Compresse le répertoire obtenu
:4. Supprime le répertoire initial "verification_noms_de_fichiers" 
@echo off
set /p version="version: "
pyinstaller verification_noms_de_fichiers.py
rd /s /q build
copy verification_noms_de_fichiers.bat dist
rename dist verification_noms_de_fichiers
"C:\Program Files\7-Zip\7z" a -tzip ..\bin\verification_noms_de_fichiers_%version%_win64_py3.6.zip verification_noms_de_fichiers/
rd /s /q verification_noms_de_fichiers