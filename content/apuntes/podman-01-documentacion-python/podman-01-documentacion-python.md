Title: Podman básico: Contenedor con documentación de Python
Slug: podman-01-documentacion-python
Summary: Primer ejercicio para probar Podman donde se crea un contenedor, se copia y desempaca la documentación de Python y se levanta un servidor web para consultarla.
Tags: contenedores
Date: 2020-08-04 22:00
Modified: 2020-08-04 22:00
Category: apuntes
Preview: podman.png


Crear un directorio para este ejercicio

    $ mkdir podman-01-documentacion-python
    $ cd podman-01-documentacion-python

Visite [Download Python 3 Documentation](https://docs.python.org/3/download.html) y descargue el archivo comprimido que tiene todos los archivos HTML empacados en .tar.bz2. Al momento de escribir esto se encuentra la versión 3.8.5

    $ wget https://docs.python.org/3/archives/python-3.8.5-docs-html.tar.bz2

Crear el archivo `Dockerfile`

    $ nano Dockerfile

Con este contenido...

    FROM python:3.8-alpine

    # Crear directorio
    RUN mkdir /app
    WORKDIR /app

    # Copiar la documentación
    COPY python-3.8.5-docs-html.tar.bz2 .

    # Desempacar
    RUN tar -xjf python-3.8.5-docs-html.tar.bz2 && \
      ln -s python-3.8.5-docs-html python3

    # Arrancar el servidor web
    CMD python -m http.server 8000

Descargar la imagen `python:3.8-alpine`

    $ podman pull python:3.8-alpine
    $ podman images

Construir tu contenedor python_docs en su versión 3.8.5

    $ podman build -t python_docs:3.8.5 .

Correr el contenedor, que se autodestruya, mandar al fondo, canalizar el puerto 8000 y con nombre python_docs_web

    $ podman run --rm -d -p 8000:8000 --name python_docs_web python_docs:3.8.5

Probar el navegador de internet con esta URL

    http://127.0.0.1:8000/python3/

<img class="img-fluid" src="python-3-8-5-documentation.png" alt="Mozilla Firefox con Python 3.8.5 Documentation">

Terminar la ejecución del contenedor con...

    $ podman stop python_docs_web
