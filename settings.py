"""Settings for pelican."""

# This can also be the absolute path to a theme that you downloaded
# i.e. './themes/anothertheme/'
#THEME = 'notmyidea'
THEME = 'octopress'
#THEME = 'pelican-svbtle'
#THEME = 'pelican-cait'

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
SITEURL = 'http://mandarvaze.github.com'

# I like to have ``Archives`` in the main menu.
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
)

WITH_PAGINATION = True
DEFAULT_PAGINATION = 5
REVERSE_ARCHIVE_ORDER = True

# Uncomment what ever you want to use
#GOOGLE_ANALYTICS = 'XX-XXXXXXX-XX'
#DISQUS_SITENAME = 'yourdisqushandle'
GITHUB_URL = 'http://github.com/mandarvaze/mandarvaze.github.com'
TWITTER_USERNAME = 'mandarvaze'
