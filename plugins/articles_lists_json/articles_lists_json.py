"""
Articles Lists JSON
===================

Create lists in JSON from articles.

"""
import json
from pathlib import Path

from bs4 import BeautifulSoup
from pelican import signals


class ArticlesListsJSONGenerator():
    """ Description """

    def __init__(self, context, settings, path, theme, output_path, *null):
        self.context = context
        self.siteurl = settings.get('SITEURL')
        self.relative_urls = settings.get('RELATIVE_URLS')
        self.output_path = output_path
        self.json_output_path = 'json'
        if settings.get('ARTICLES_LISTS_JSON_OUTPUT_PATH'):
            self.json_output_path = settings.get('ARTICLES_LISTS_JSON_OUTPUT_PATH')
        self.output_all = None
        if settings.get('ARTICLES_LISTS_JSON_OUTPUT_ALL'):
            self.output_all = settings.get('ARTICLES_LISTS_JSON_OUTPUT_ALL')
        self.categories_filters = None
        if settings.get('ARTICLES_LISTS_JSON_CATEGORIES_FILTERS'):
            self.categories_filters = settings.get('ARTICLES_LISTS_JSON_CATEGORIES_FILTERS')
        self.limit = None
        if settings.get('ARTICLES_LISTS_JSON_LIMIT'):
            self.limit = int(settings.get('ARTICLES_LISTS_JSON_LIMIT'))

    def agregar_nodo(self, item):
        """ Add node """
        # Omit when is not published
        if getattr(item, 'status', 'published') != 'published':
            return
        # Set date
        page_date = str(item.date) if item.date is not None else ''
        # Set title
        soup_title = BeautifulSoup(item.title.replace('&nbsp;', ' '), 'html.parser')
        page_title = soup_title.get_text(' ', strip=True).replace('“', '"').replace('”', '"').replace('’', "'").replace('^', '&#94;')
        # Set summary
        page_summary = ''
        if getattr(item, 'summary', 'None') != 'None':
            soup_summary = BeautifulSoup(item.summary, 'html.parser')
            page_summary = soup_summary.get_text()
        # Set category
        page_category = item.category.name if getattr(item, 'category', 'None') != 'None' else ''
        # Set URL
        page_url = '.'
        if item.url:
            page_url = item.url if self.relative_urls else (self.siteurl + '/' + item.url)
        # Set preview image
        page_preview = ''
        if getattr(item, 'preview', 'None') != 'None':
            page_preview = page_url + getattr(item, 'preview', 'None')
        # Node as dictionary
        node = {
            'date': page_date,
            'title': page_title,
            'summary': page_summary,
            'category': page_category,
            'url': page_url,
            'preview': page_preview,
        }
        # Return node
        return node

    def generate_output(self, writer):
        """ Generate output """
        if self.output_all is None and self.categories_filters is None:
            return
        # All nodes
        all_nodes = []
        for page in self.context['articles']:
            node = self.agregar_nodo(page)
            all_nodes.append(node)
        # Make directory for JSON files
        output_dir = Path(self.output_path, self.json_output_path)
        output_dir.mkdir(parents=True, exist_ok=True)
        # Save all nodes JSON file
        if self.output_all is not None:
            if self.limit is None:
                root_node = { 'data': all_nodes }
            else:
                root_node = { 'data': all_nodes[:self.limit] }
            output_file = Path(output_dir, self.output_all)
            with open(output_file, 'w', encoding='utf-8') as pointer:
                pointer.write(json.dumps(root_node, separators=(',', ':'), ensure_ascii=False))
        # Save filtered categories JSON files
        if self.categories_filters is not None:
            for category_file_name, categories in self.categories_filters:
                category_nodes = []
                count = 0
                for node in all_nodes:
                    if node['category'] in categories:
                        category_nodes.append(node)
                        count += 1
                        if self.limit is not None and count >= self.limit:
                            break
                root_node = { 'data': category_nodes }
                output_file = Path(output_dir, category_file_name)
                with open(output_file, 'w', encoding='utf-8') as pointer:
                    pointer.write(json.dumps(root_node, separators=(',', ':'), ensure_ascii=False))


def get_generators(generators):
    """ Get generators """
    return ArticlesListsJSONGenerator


def register():
    """ Register """
    signals.get_generators.connect(get_generators)
