"""
WSGI config for springs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "springs.settings")

application = get_wsgi_application()

# print('postgres host',os.environ.get('POSTGRES_HOST'))
