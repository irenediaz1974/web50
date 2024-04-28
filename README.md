# CS50’s Web Programming with Python and JavaScript

## CS50´s Web Programming Projects (2024)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

### Proyecto 2

:negative_squared_cross_mark: - Tarea: Commerce (Framework Django) [Commerce](/../../../../irenediaz1974/web50/blob/main/projects/2020/x/commerce/README.md)

#### Diseñar un sitio de subastas de comercio electrónico similar a eBay que permita a los usuarios publicar listados de subastas, realizar ofertas en los listados, comentar sobre esos listados y agregar listados a una "lista de seguimiento".

Ejecución del proyecto: 

1. Obtener fichero commerce.zip con la estructura del proyecto:

```console
 https://cdn.cs50.net/web/2020/spring/projects/2/commerce.zip
```


2. Primeros pasos (En mi PC):
 - En projects\2020\x --> Descompactar: commerce.zip
 - cd into the commerce
 - Crear fichero README.md en el subdirectorio commerce
 
3. Realizar submit50


### Proyecto 1

:white_check_mark: - Wiki (Framework Django) [Wiki](/../../../../irenediaz1974/web50/blob/main/projects/2020/x/wiki/Readme.md)
#### Diseñar una enciclopedia online similar a Wikipedia.

Ejecución del proyecto: 

1. Obtener fichero wiki.zip con la estructura del proyecto:

```console
wget https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip

unzip wiki.zip
```

- Crear fichero README.md en el subdirectorio wiki


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

devcontainer.json:
{
    "image": "ghcr.io/cs50/codespace",   
    "forwardPorts": [
      5000,
      5900,
      6081,
      8080,
      8082
    ]
  }
- Luego de creado el codespace:
1. Crear environment: **python3 -m venv web50** 
2. Activarlo: **source web50/bin/activate**
3. Instalar:
```python
 pip install django
 pip install markdown2
 pip3 install submit50
```

  
  - En mi PC
    Creé un entorno virtual. Aquí están los pasos generales:
    1. En tu terminal, navega al directorio donde deseas crear el entorno virtual.
    2. Crea el entorno virtual con el comando python3 -m venv web50.
    3. Activa el entorno virtual con ```. .\web50\Scripts\activate```
  - Configurar gitignore:
    Crear gitignore y añadir el entorno creado:
    - Desde el terminal y en el subdirectorio del proyecto:
        1. Crea un archivo .gitignore con el comando touch .gitignore.
        2. Abre el archivo .gitignore con tu editor de texto preferido.
        3. Escribe el nombre de la carpeta del entorno en una nueva línea y guarda el archivo.Por ejemplo, si tu entorno se llama "nombre_del_entorno", entonces escribes "nombre_del_entorno/" en el archivo .gitignore. Esto le dice a Git que ignore los archivos en esa carpeta.
