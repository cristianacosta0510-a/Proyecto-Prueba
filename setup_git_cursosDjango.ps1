$GIT = "C:\Program Files\Git\cmd\git.exe"
$PROJECT = "C:\Proyecto Integrador II\CursosDjango"
$REMOTE_URL = $args[0]  # Pasar la URL del nuevo repo como argumento

Set-Location $PROJECT

# Crear requirements.txt
pip freeze | Out-File -Encoding utf8 requirements.txt

# Crear .gitignore
$gitignore = @"
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.so
*.egg
*.egg-info/
dist/
build/
.eggs/
env/
venv/
.venv/
*.env
db.sqlite3
*.sqlite3
media/
.DS_Store
Thumbs.db
"@
$gitignore | Out-File -Encoding utf8 .gitignore

# Git init y push
& $GIT init
& $GIT config user.name "Christian Acosta"
& $GIT config user.email "cristianacosta0510@gmail.com"
& $GIT add .
& $GIT commit -m "Agregando proyecto CursosDjango - Oasis Negro"
& $GIT remote add origin $REMOTE_URL
& $GIT push -u origin master

Write-Host "`n✅ ¡Proyecto subido exitosamente a GitHub!" -ForegroundColor Green
