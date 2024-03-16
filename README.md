# CS50’s Web Programming with Python and JavaScript

## CS50´s Web Programming Projects (2024)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
### Proyecto 1

:negative_squared_cross_mark: - Wiki (Framework Django)

Ejecución del proyecto: 

1. Obtener fichero wiki.zip con la estructura del proyecto:

```console
wget https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip

unzip wiki.zip
```
Notas: 
- Levantar el servicio:
```python
    python manage.py runserver
```
- Convertir Markdown a HTML utilizando el paquete python-markdown2, instalar:

```python
    pip3 install markdown2
```

3.Realizar submit50

***
### Proyecto 0

:white_check_mark: 1. Search (HTML, CSS, JavaScript)

- Imitar la página Search de Google, Image Search y Advanced Search.

***
### Configuración Inicial para el curso

Dado mi sistema operativo Win8 no puedo ejecutar submit50 en vscode, por lo que además de tener los proyectos en mi laptop para trabajar necesito un codespace para hacer los submits

- Codespaces
Crear un codespace dentro del repositorio creado para el curso: web50
Crear el devcontainer.json para que utilice la imagen del CS50 codespaces: "image": "ghcr.io/cs50/codespace:bf6014b603182697b53bcd953eeae55de8ae66f3"
  - En el codespace
  Instalé submit50 y pude hacer los submits al sitio me50.
  
  - En mi PC
    Creé un entorno virtual. Aquí están los pasos generales:
    1. En tu terminal, navega al directorio donde deseas crear el entorno virtual.
    2. Crea el entorno virtual con el comando python3 -m venv web50.
    3. Activa el entorno virtual con ```. .\web50\Scripts\activate```
  - Configurar gitignore nnn
    Crear gitignore y añadir el entorno creado:
    - Desde el terminal y en el subdirectorio del proyecto:
        1. Crea un archivo .gitignore con el comando touch .gitignore.
        2. Abre el archivo .gitignore con tu editor de texto preferido.
        3. Escribe el nombre de la carpeta del entorno en una nueva línea y guarda el archivo.Por ejemplo, si tu entorno se llama "nombre_del_entorno", entonces escribes "nombre_del_entorno/" en el archivo .gitignore. Esto le dice a Git que ignore los archivos en esa carpeta.
