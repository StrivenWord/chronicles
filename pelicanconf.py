AUTHOR = 'Paul Lee'
SITENAME = 'AI Chronicles'
SITEURL = ""
THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'yeti'
RELATIVE_URLS = True    # Only for local development.

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

LANGUAGES = {
    'en': 'English',
    'eo': 'Esperanto',
    'es': 'Español',
}

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
I18N_TEMPLATES_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
