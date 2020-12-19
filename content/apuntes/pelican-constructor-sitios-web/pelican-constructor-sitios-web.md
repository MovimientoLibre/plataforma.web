Title: Pelican: Constructor de sitios web
Slug: pelican-constructor-sitios-web
Summary: Pelican es un constructor de sitios web estáticos programado en Python que no necesita de una base de datos.
Tags: python
Date: 2020-03-30 16:08
Modified: 2020-12-12 14:48
Category: apuntes
Preview: python.png


### Qué es Pelican

[Pelican](https://blog.getpelican.com/) es un constructor de sitios web estáticos programado en [Python](https://www.python.org/) que no necesita de una base de datos.

### Cómo funciona

Pelican puede recibir contenidos en archivos en [Markdown](https://movimientolibre.com/apuntes/markdown/), [reStructuredText](http://docutils.sourceforge.net/rst.html) y/o HTML.

Cada archivo en _contents_ va crear un artículo o una página en el sitio web. La sintaxis indica que las primeras líneas deben ser para los [metadados](https://docs.getpelican.com/en/stable/content.html#file-metadata), por ejemplo, en el comienzo de un archivo **md** se define el título, la categoría y la fecha así:

    Title: Hola Mundo
    Category: Comunicados
    Date: 2020-03-21 18:32

Cuando vaya a planear la estructura del sitio web, debe determinar qué va ser artículo y qué va ser página...

* **Artículos:** Aquellos contenidos que se deben de ordenar cronológicamente, que se listen del más reciente al más antiguo.
* **Página:** Aquellos contenidos atemporales que rara vez cambien, como los datos de contacto.

Como parte de su versatilidad, Pelican es capaz de manejar **temas**. Hay [muchos temas compartidos por los usuarios](http://pelicanthemes.com/) que puedes descargar y adecuar. O bien, porqué no, [puedes crear uno desde cero.](https://docs.getpelican.com/en/stable/themes.html)

Además, también puedes agregar **plug-ins** para [obtener capacidades adicionales.](https://github.com/getpelican/pelican-plugins)

### Requisitos

Previamente debe tener instalado Python, de preferencia la versión 3, verifique con...

    $ python --version

El gestor de paquetes [Python Package Index](https://pypi.org/) alias _pip_...

    $ which pip

Y una herramienta para crear entornos virtuales de Python, como **venv** o **virtualenv**...

### Pasos para su instalación

Puede crear los entornos virtuales en cualquier lugar de sus dispositivos de almacenamiento. Por ejemplo, pada disponer de esta herramienta en su escritorio...

    $ cd ~/Escritorio
    $ mkdir Pelican
    $ cd Pelican
    $ python -m venv venv

Active el entorno virtual

    $ . venv/bin/activate

E instale los paquetes Pelican y Markdown...

    (venv) $ pip install pelican markdown

Revise los paquetes instalados con...

    (venv) $ pip list

### Crear un sitio web rápidamente con el asistente

El asistente nos pregunta las variables necesarias para crear un sitio web, ejecute con...

    (venv) $ pelican-quickstart

Por ejemplo, vamos a crear un sitio web llamado _Demostracion_...

    > Where do you want to create your new web site? [.] Demostracion
    > What will be the title of this web site? Este es mi primer sitio web!!!
    > Who will be the author of this web site? Guillermo Valdés
    > What will be the default language of this web site? [es]
    > Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
    > Do you want to enable article pagination? (Y/n) n
    > What is your time zone? [Europe/Paris] America/Mexico_City
    > Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) y
    > Do you want to upload your website using FTP? (y/N) n
    > Do you want to upload your website using SSH? (y/N) n
    > Do you want to upload your website using Dropbox? (y/N) n
    > Do you want to upload your website using S3? (y/N) n
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) n
    > Do you want to upload your website using GitHub Pages? (y/N) n
    Done. Your new project is available at /home/guivaloz/Capacitacion/Pelican/Demostracion

Al terminar nos crea un directorio `Demostracion`. Veamos lo que el asistente creó...

    (venv) $ cd Demostracion
    (venv) $ ls

Pelican necesita de estos directorios y archivos:

* `contents` Directorio donde hay que poner los artículos y las páginas.
* `output` Directorio donde se va a depositar el sitio web resultante cuando se contruya o publique.
* `pelicanconf.py` Programa en Python donde se definen las variables para su uso local.
* `publishconf.py` Programa en Python donde se carga `pelicanconf.py` y se definen variables para publicar en internet.

Cuando en el asistente se contesta con Sí en generar **tasks.py/Makefile** también se crean:

* `tasks.py` Contiene las configuraciones para publicar en los proveedores de hospedaje.
* `Makefile` Sirve al comando `make`.

### Agregue su primer contenido y contruya con make

Cámbiese al directorio `contents`...

    (venv) $ cd contents

Cree un archivo para un comunicado...

    (venv) $ nano -w primer-comunicado.md

Por ejemplo, inicie con los [metadados](https://docs.getpelican.com/en/stable/content.html#file-metadata) y el contenido en **markdown**...

    Title: Primer Comunicado
    Slug: primer-comunicado
    Category: Comunicados
    Date: 2020-03-21 18:32
    Tags: Demostraciones, Desarrollo, Python

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Regrese al directorio `Demostracion`...

    (venv) $ cd ..

Construya el sitio...

    (venv) $ make html

Arranque el servidor web, por defecto usará el puerto 8000...

    (venv) $ make serve

Revise en su navegador el sitio web `Demostracion`...

    http://localhost:8000

Mate el servidor presionando `CTRL-C`.

Ahora, pruebe el comando para construir el sitio web cada vez que haya cambios y levantar el servicio web al mismo tiempo...

    (venv) $ make devserver

Deje la terminal en el fondo y siga agregando o modificando. En su navegador de internet presione `F5` para refrescar. Mate presionando `CTRL-C`.

Para generar el sitio web para subir a internet, leyendo las variables de `publishconf.py`, debe ejecutar...

    (venv) $ make publish

Copie el contenido de `output` a su servidor web o a su proveedor en la nube.

### Comandos con pelican

Si contestó que NO en el asistente, donde pregunta _Do you want to generate a tasks.py/Makefile?_, no tendrá el archivo `Makefile` y no funciona `make`. Aun así puede ejecutar Pelican para hacer lo mismo...

Para        | Ejecute
------------|-------------------------------------------
construir   | `pelican content`
reconstruir | `pelican --delete-output-directory content`
servir      | `pelican --listen content`
desarrollar | `pelican --autoreload --listen content`
publicar    | `pelican --settings publishconf.py content`

### Agregue un tema

Los temas deben estar contenidos en su propio directorio y dentro de `themes`.

Cada tema tiene a su vez dos directorios:

* Un `static` para CSS, imágenes, JavaScript, etc.
* Un `templates` con las plantillas hechas con [Jinja2](https://palletsprojects.com/p/jinja/).

La estructura básica de un tema es así...

    ├── static
    │   ├── css
    │   └── images
    └── templates
        ├── archives.html   // índice de archivos
        ├── article.html    // estructura para cada artículo
        ├── author.html     // índice de contenidos de un autor
        ├── authors.html    // índice de autores
        ├── categories.html // índice de categorías
        ├── category.html   // índice de contenidos de una categoría
        ├── index.html      // índice o página inicial
        ├── page.html       // estructura para cada página
        ├── tag.html        // índice de contenidos de una etiqueta
        └── tags.html       // índice de etiquetas

Luego, por ejemplo, si tiene listo el tema `blue-penguin`, edite el archivo `pelicanconf.py` y agregue...

    THEME = 'themes/blue-penguin'

Así la próxima vez que construya o publique se usará ese tema.

Aprenda [Jinja2](https://palletsprojects.com/p/jinja/) para dominar la creación y modificación de los temas.

### Salir del entorno virtual

Si ya terminó, puede simplemente cerrar la terminal o pedir su desactivación...

    (venv) $ deactivate

### Aprenda más en

* [Pelican Develpment Blog](https://blog.getpelican.com/)
* [Pelican Documentation](https://docs.getpelican.com/en/stable/)
* [Pelican Themes](http://pelicanthemes.com/)
* [Collection of plugins for the Pelican static site generator](https://github.com/getpelican/pelican-plugins)
* [Jinja2](https://palletsprojects.com/p/jinja/)
