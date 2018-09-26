#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Sitio web
SITEURL = 'http://www.movimientolibre.com'
SITENAME = 'Movimiento Libre'
SITELOGO = 'theme/images/movimientolibre.png'
SITEDESCRIPTION = 'Colección de ideas.'
SITETWITTER = '@guivaloz'

# Autor
AUTHOR = 'Guillermo Valdés Lozano'

# Directorio donde esta el contenido
PATH = 'content'

# Directorios que tienen los articulos
ARTICLE_PATHS = ['apuntes', 'articulos', 'presentaciones']

# Directorios que tienen páginas fijas, no artículos
PAGE_PATHS = ['licencias', 'portafolio']

# Directorios y archivos que son fijos
# Agregue también los directorios que tienen archivos para artículos y páginas
STATIC_PATHS = ['CNAME', 'favicon.ico', 'LICENSE', 'README.md', 'robots.txt',
                'apuntes', 'articulos', 'presentaciones', 'portafolio']

# Usar el nombre del directorio como la categoría
USE_FOLDER_AS_CATEGORY = True

# Los artículos van en directorios por categoria/titulo/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Las páginas fijas van en directorios categoria/titulo/
PAGE_URL = '{category}/{slug}/'
PAGE_SAVE_AS = '{category}/{slug}/index.html'

# Encabezados para las categorías
CATEGORIES_TITLES = {'apuntes': 'Apuntes',
                     'articulos': 'Artículos',
                     'presentaciones': 'Presentaciones'}

# Tema
THEME = 'themes/startbootstrap-blog-post'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Lenguaje y zona horaria
DEFAULT_LANG = 'es'
TIMEZONE = 'America/Mexico_City'

# Borrar toda la salida,
# puede borrar directorios ocultos como .git, use si está seguro
DELETE_OUTPUT_DIRECTORY = False

# Para desarrollo los vinculos son relativos
RELATIVE_URLS = True

# Para desarrollo, se desactiva la paginacion
DEFAULT_PAGINATION = False
#DEFAULT_PAGINATION = 8
#DEFAULT_ORPHANS = 2

# Para desarrollo se desactiva la generacion de feeds
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

# Para desarrollo, recomendado mantener en falso
LOAD_CONTENT_CACHE = True

# Para desarrollo, no usar dependencias en Internet
USE_REMOTE_SERVICES = False
