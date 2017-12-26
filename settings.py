"""Settings for pelican."""

# This can also be the absolute path to a theme that you downloaded
# i.e. './themes/anothertheme/'
#THEME = 'notmyidea'
#THEME = 'octopress'
THEME = './themes/pelican-elegant'

# The folder ``images`` should be copied into the folder ``static`` when
# generating the output.
STATIC_PATHS = ['images', ]

# See http://pelican.notmyidea.org/en/latest/settings.html#timezone
TIMEZONE = 'UTC'

# Pelican will take the ``Date`` metadata and put the articles into folders
# like ``/posts/2012/02/`` when generating the output.
ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/'

# I like to put everything into the category ``Blog``, which also appears on
# the main menu. Tags will not appear on the menu.
DEFAULT_CATEGORY = 'Blog'

AUTHOR = 'Mandar Vaze'
SITENAME = 'Desi Penguin\'s Blog'
SITEURL = 'https://mandarvaze.github.io'

# I like to have ``Archives`` in the main menu.
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
)

WITH_PAGINATION = True
DEFAULT_PAGINATION = 5
REVERSE_ARCHIVE_ORDER = True

# Post upgrade to 3.6, it is suggested that caching be disabled
LOAD_CONTENT_CACHE = False

# Uncomment what ever you want to use
#GOOGLE_ANALYTICS = 'XX-XXXXXXX-XX'
DISQUS_SITENAME = 'desipenguinsblog'
GITHUB_URL = 'https://github.com/mandarvaze/mandarvaze.github.com'
TWITTER_USERNAME = 'mandarvaze'

SOCIAL = (('twitter', 'https://twitter.com/mandarvaze'),
          ('linkedin', 'https://www.linkedin.com/in/mandarvaze'),
          ('github', 'https://github.com/mandarvaze'),)

PLUGIN_PATHS = ['/projects/myblog/pelican-plugins']

# Elegant theme specific configurations
PLUGINS = ['asciidoc_reader', 'sitemap', 'extract_toc', 'tipue_search', 'neighbors', 'share_post']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True
DEFAULT_PAGINATION = False
RECENT_ARTICLES_COUNT = 5
# SMO
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'
