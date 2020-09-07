"""
WSGI config for what_if_i_had_invested_in_vanguards project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'what_if_i_had_invested_in_vanguards.settings')

application = get_wsgi_application()
