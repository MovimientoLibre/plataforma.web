Articles Lists JSON
===================

Create lists in JSON from articles and pages.

## Instructions

Modify your pelicanconf.py or publishconf.py

    PLUGIN_PATHS = ['plugins']
    PLUGINS = ['articles_lists_json']

For default create a `json` directory (ARTICLES_LISTS_JSON_OUTPUT_PATH) and a file `all.json` (ARTICLES_LISTS_JSON_OUTPUT_ALL) with all articles.

Optionally configurate like this...

    ARTICLES_LISTS_JSON_OUTPUT_PATH = 'json'
    ARTICLES_LISTS_JSON_OUTPUT_ALL = 'all.json'
    ARTICLES_LISTS_JSON_CATEGORIES_FILTERS = [
        ('noticias-eventos.json', ['Comunicados', 'News Letters', 'Noticias']),
        ('transmisiones-sesiones.json', ['Sala Penal', 'Sala Regional']),
    ]
    ARTICLES_LISTS_JSON_LIMIT = 50

For not create a JSON file with all use...

    ARTICLES_LISTS_JSON_OUTPUT_ALL = None

Limit the number of items in all lists or set to None to unlimited...

    ARTICLES_LISTS_JSON_LIMIT = None
