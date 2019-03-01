"""
WSGI config for lukassimonis_net project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
#sys.path.append('/var/www/lukassimonis_net')
#sys.path.append('/var/www/lukassimonis_net/lukassimonis_net')
#sys.path.append('/var/www/lukassimonis_net/playground')

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lukassimonis_net.settings')

application = get_wsgi_application()
