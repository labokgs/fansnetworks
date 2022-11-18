from .settings_common import *
from .local_settings import *
import os


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "private_diary",
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": "",
        "PORT": "",
    }
}

DEBUG = False

try:
    # 存在する場合、ローカルの設定読み込み
    from .local_settings import *
    from .settings_common import *
except ImportError:
    pass

if not DEBUG:
    # Heroku settings

    # staticの設定
    import os
    import django_heroku

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Static files (CSS, JavaScript, Images)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'

    # Extra places for collectstatic to find static files.
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    MIDDLEWARE += [
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]

    # HerokuのConfigを読み込み
    django_heroku.settings(locals())