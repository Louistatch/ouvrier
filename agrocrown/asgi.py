"""
ASGI config for agrocrown project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrocrown.settings')

application = get_asgi_application()

from django.core.management import execute_from_command_line
from pyngrok import ngrok

# Démarrez un tunnel ngrok
public_url = ngrok.connect(port="80")

execute_from_command_line()
