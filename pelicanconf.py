#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jordan Chapman'
SITENAME = 'Superfluous Sextant'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = '../themes/pelican-clean-blog'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('globe', 'http://jordan-chapman.com'),
          ('twitter', 'https://twitter.com/supersextant'),
          ('github', 'https://github.com/jChapman'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GOOGLE_ANALYTICS = "UA-82486268-1"
DISQUS_SITENAME = "superfluoussextant"

STATIC_PATHS = ['static']

# Clean Blog Theme Settings
HEADER_COVER = 'static/soft_blue_glow-darkened.jpg'
COLOR_SCHEME_CSS = 'tomorrow_night.css'

