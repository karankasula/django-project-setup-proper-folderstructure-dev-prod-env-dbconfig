"""
ASGI config for healthy_home project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from decouple import config

from django.core.asgi import get_asgi_application

if config('DEBUG', default=False, cast=bool):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings.prod')

application = get_asgi_application()
