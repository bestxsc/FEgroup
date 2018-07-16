#####################################
########## Django settings ##########
#####################################
# See <https://docs.djangoproject.com/en/1.11/ref/settings/>
# for more info and help. If you are stuck, you can try Googling about
# Django - many of these settings below have external documentation about them.
#
# The settings listed here are of special interest in configuring the site.

# SECURITY WARNING: keep the secret key used in production secret!
# You may use <http://www.miniwebtool.com/django-secret-key-generator/>
# to generate this key.
import raven

SECRET_KEY = 'fgrb34m@bev(0ve3y^s@tgm@1pg51&n&iy$282knd(0c5f7nj)#*5&o_f4hdf4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Change to False once you are done with runserver testing.

# Uncomment and set to the domain names this site is intended to serve.
# You must do this once you set DEBUG to False.
ALLOWED_HOSTS = ['oj.hbu.cn', 'oj.hbu.edu.cn', '10.188.65.202', '127.0.0.1', 'localhost']

# Optional apps that DMOJ can make use of.
INSTALLED_APPS += (
    'django_select2',  # Searchable comboboxes.
    'anymail',
    'raven.contrib.django.raven_compat',
)

# Your database credentials. Only MySQL is supported by HBUOJ.
# Documentation: <https://docs.djangoproject.com/en/1.11/ref/databases/>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dmoj',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES',
        },
    }
}

# Caching. You can use memcached or redis instead.
# Documentation: <https://docs.djangoproject.com/en/1.11/topics/cache/>
CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:32768",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 1024}
        }
    }
}

# Sessions.
# Documentation: <https://docs.djangoproject.com/en/1.11/topics/http/sessions/>
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Internationalization.
# Documentation: <https://docs.djangoproject.com/en/1.11/topics/i18n/>
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#########################################
########## Email configuration ##########
#########################################
# See <https://docs.djangoproject.com/en/1.11/topics/email/#email-backends>
# for more documentation. You should follow the information there to define 
# your email settings.

# Use this if you are just testing.
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# The following block is included for your convenience, if you want 
# to use Gmail.
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_SSL = True
# EMAIL_HOST_USER = 'xingji2163@163.com'
# EMAIL_HOST_PASSWORD = 'monouno000'
# EMAIL_PORT = 994
DEFAULT_FROM_EMAIL = 'HBUOJ <postmaster@noreply.zmy.im>'
EMAIL_TIMEOUT = 3000

# To use ANYMAIL, uncomment this block.
# https://github.com/anymail/django-anymail

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": "key-0ea8ae956bf5a6b8def1c8ef645647dc",
    "MAILGUN_SENDER_DOMAIN": 'noreply.zmy.im',  # your Mailgun domain, if needed
}

# The DMOJ site is able to notify administrators of errors via email,
# if configured as shown below.

# A tuple of (name, email) pairs that specifies those who will be mailed
# when the server experiences an error when DEBUG = False.

ADMINS = (
    ('Boyce', 'monobiao@gmail.com'),
)

# The sender for the aforementioned emails.
SERVER_EMAIL = 'HBU Online Judge Admin<monobiao@gmail.com>'

##################################################
########### Static files configuration. ##########
##################################################
# See <https://docs.djangoproject.com/en/1.11/howto/static-files/>.

# Change this to somewhere more permanent., especially if you are using a 
# webserver to serve the static files. This is the directory where all the 
# static files DMOJ uses will be collected to.
# You must configure your webserver to serve this directory as /static/ in production.
STATIC_ROOT = '/tmp/static'

# URL to access static files.
# STATIC_URL = '/static/'

# Uncomment to use hashed filenames with the cache framework.
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

############################################
########## DMOJ-specific settings ##########
############################################

# DMOJ site display settings.
SITE_NAME = 'HBUOJ'
SITE_LONG_NAME = 'HBU Online Judge'
SITE_ADMIN_EMAIL = 'monobiao@gmail.com'
# TERMS_OF_SERVICE_URL = '//dmoj.ca/tos' # Use a flatpage.

# Bridge controls.
# The judge connection address and port; where the judges will connect to the site.
# You should change this to something your judges can actually connect to 
# (e.g., a port that is unused and unblocked by a firewall).
# BRIDGED_JUDGE_ADDRESS = [('10.188.65.202', 9999)]

# The bridged daemon bind address and port to communicate with the site.
# BRIDGED_DJANGO_ADDRESS = [('10.188.65.202', 9998)]

# DMOJ features.
# Set to True to enable full-text searching for problems.
ENABLE_FTS = False

# Event server.
# Uncomment to enable live updating.
EVENT_DAEMON_USE = True

# Uncomment this section to use websocket/daemon.js included in the site.
EVENT_DAEMON_POST = 'ws://10.188.65.202:15101/'

# If you are using the defaults from the guide, it is this:
# EVENT_DAEMON_POST = 'ws://127.0.0.1:15101/'

# These are the publicly accessed interface configurations.
# They should match those used by the script.
# EVENT_DAEMON_GET = '<public ws:// URL for clients>'
# EVENT_DAEMON_GET_SSL = '<public wss:// URL for clients>'
# EVENT_DAEMON_POLL = '<public URL to access the HTTP long polling of event server>'
# i.e. the path to /channels/ exposed by the daemon, through whatever proxy setup you have.

# Using our standard nginx configuration, these should be.
EVENT_DAEMON_GET = 'ws://10.188.65.202/event/'
# EVENT_DAEMON_GET_SSL = 'wss://<your domain>/event/' # Optional
EVENT_DAEMON_POLL = '/channels/'

# If you would like to use the AMQP-based event server from <https://github.com/DMOJ/event-server>,
# uncomment this section instead. This is more involved, and recommended to be done
# only after you have a working event server.
# EVENT_DAEMON_AMQP = '<amqp:// URL to connect to, including username and password>'
# EVENT_DAEMON_AMQP_EXCHANGE = '<AMQP exchange to use>'

# A map of Earth in Equirectangular projection, for timezone selection.
# Please try not to hotlink this poor site.
TIMEZONE_MAP = 'http://naturalearth.springercarto.com/ne3_data/8192/textures/3_no_ice_clouds_8k.jpg'

## Camo (https://github.com/atmos/camo) usage.
# CAMO_URL = "<URL to your camo install>"
# CAMO_KEY = "<The CAMO_KEY environmental variable you used>"

# Domains to exclude from being camo'd.
# CAMO_EXCLUDE = ("https://dmoj.ml", "https://dmoj.ca")

# Set to True to use https when dealing with protocol-relative URLs.
# See <http://www.paulirish.com/2010/the-protocol-relative-url/> for what they are.
# CAMO_HTTPS = False

# HTTPS level. Affects <link rel='canonical'> elements generated.
# Set to 0 to make http URLs canonical.
# Set to 1 to make the currently used protocol canonical.
# Set to 2 to make https URLs canonical.
# DMOJ_HTTPS = 0

## PDF rendering settings.
# Directory to cache the PDF.
# PROBLEM_PDF_CACHE = '/home/dmoj-uwsgi/pdfcache'

# Path to use for nginx's X-Accel-Redirect feature.
# Should be an internal location mapped to the above directory.
# PROBLEM_PDF_INTERNAL = '/pdfcache'

# Path to a PhantomJS executable.
# PHANTOMJS = '/usr/local/bin/phantomjs'

# If you can't use PhantomJS or prefer wkhtmltopdf, set the path to wkhtmltopdf executable instead.
# WKHTMLTOPDF = '/usr/local/bin/wkhtmltopdf'

# Note that PhantomJS is preferred over wkhtmltopdf and would be used when both are defined.

# ======== Logging Settings ========
# Documentation: https://docs.djangoproject.com/en/1.11/ref/settings/#logging
#                https://docs.python.org/2/library/logging.config.html#logging-config-dictschema
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'file': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'file',
        },
    },
    'loggers': {
        # Catch all log to stderr.
        '': {
            'handlers': ['console'],
        },
        # Other loggers of interest. Configure at will.
        #  - judge.user: logs naughty user behaviours.
        #  - judge.problem.pdf: PDF generation log.
        #  - judge.html: HTML parsing errors when processing problem statements etc.
        #  - judge.mail.activate: logs for the reply to activate feature.
        #  - event_socket_server
    },
}

RAVEN_CONFIG = {
    'dsn': 'https://9c1d2c3c4b8e4a339127a8371135c29a:b64fc4f3432a4eb6b83d76956b9540fd@sentry.io/1222897',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(BASE_DIR),
}

# ======== Custom Configuration ========
# You may add whatever django configuration you would like here.
# Do try to keep it separate so you can quickly patch in new settings.
DMOJ_RATING_COLORS = True
REGISTRATION_OPEN = False
PROBLEM_DATA_ROOT = '/home/hbuoj/problems'

MARKDOWN_STYLES = {
    'comment': MARKDOWN_DEFAULT_STYLE,
    'self-description': MARKDOWN_USER_LARGE_STYLE,
    'problem': MARKDOWN_ADMIN_EDITABLE_STYLE,
    'contest': MARKDOWN_ADMIN_EDITABLE_STYLE,
    'language': MARKDOWN_ADMIN_EDITABLE_STYLE,
    'license': MARKDOWN_ADMIN_EDITABLE_STYLE,
    'judge': MARKDOWN_ADMIN_EDITABLE_STYLE,
    'blog': MARKDOWN_ADMIN_EDITABLE_STYLE,
    'solution': MARKDOWN_ADMIN_EDITABLE_STYLE,
    'contest_tag': MARKDOWN_ADMIN_EDITABLE_STYLE,
    'organization-about': MARKDOWN_ADMIN_EDITABLE_STYLE,
    'ticket': MARKDOWN_USER_LARGE_STYLE,
}
