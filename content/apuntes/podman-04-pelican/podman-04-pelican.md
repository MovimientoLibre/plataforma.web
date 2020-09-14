Title: Podman básico: sitio web con Pelican
Slug: podman-04-pelican
Summary: .
Tags: contenedores
Date: 2020-09-13 19:58
Modified: 2020-09-13 19:58
Category: apuntes
Preview: podman.png
Status: draft


Resumen.

## Crear archivos para pelican



## Crear archivo Dockerfile

Con este contenido

    FROM python:3.7-alpine

    # Crear directorio
    RUN mkdir /pelican
    WORKDIR /pelican

    # Instalar paquetes
    RUN pip install pelican Markdown

    # Copiar
    COPY . .

    # Pelican construir
    RUN pelican content

    # Levantar servidor
    CMD pelican --autoreload --listen --bind 0.0.0.0

## Arrancar contenedor

Construir la imagen de nombre "pelican_sitio_web"

    $ podman build -t pelican_sitio_web:latest .

Arrancar un contenedor

    $ podman run --rm -d -p 8085:8000 --name mi_pelican_sitio_web pelican_sitio_web:latest

Donde...

- `--rm` Va a eliminar el contenedor cuando se pare
- `-d` Manda al fondo la orden, lo _daemoniza_
- `-p 8085:8000` "Entuba" el puerto 8000 del contenedor al puerto 8085 de nuestro equipo

Ingresar en el navegador de internet

    http://127.0.0.1:8085

Ver mapeo de puertos

    $ podman port -l

Parar y eliminar el contenedor con

    $ podman stop mi_pelican_sitio_web

## Arrancar el contenedor montando una ruta del equipo

Es posible montar de forma "viva" una ruta de nuestro equipo local en el contenedor. Los expertos en contenedores no recomiendan esta capacidad para el ámbito de producción ya que el contenedor pierde su "independencia".

