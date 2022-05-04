"""
WSGI config for healthy_home project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from decouple import config

from django.core.wsgi import get_wsgi_application

if config('DEBUG', default=False, cast=bool):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings.prod')

application = get_wsgi_application()
