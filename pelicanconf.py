#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Clemens Bartz'
AUTHORURL = u'https://www.clemens-bartz.de'
SITENAME = u'de.clemensbartz'
SITEURL = u'https://clemensbartz.de'

# Clear everything
DELETE_OUTPUT_DIRECTORY = True

# Only render index and no HTML
DIRECT_TEMPLATES = ['index']
READERS = {'html': None}

# Configure paths
PATH = 'content'
PAGE_PATHS = ['']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['']

# Disable any dynamic content
ARTICLE_SAVE_AS = ''
ARTICLE_LANG_SAVE_AS = ''
DRAFT_SAVE_AS = ''
DRAFT_LANG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''
INDEX_SAVE_AS = ''

# Theming
THEME = './theme'

# Configure pages
SLUGIFY_SOURCE = 'basename'
PAGE_URL = '{slug}/index.html'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{slug}/index_{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}/index_{lang}.html'
PAGE_ORDER_BY = 'weight'

# Time
TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Language function
def lang_to_locale(l):
	return {
		'en': 'English',
		'de': 'Deutsch',
	}.get(l, l);

JINJA_FILTERS = {
	"lang_to_locale": lang_to_locale,
}
