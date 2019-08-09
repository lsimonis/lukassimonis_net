"""
WSGI config for lukassimonis_net project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lukassimonis_net.settings')
#exec(open(os.path.join(os.sep, "etc" + os.sep, "django", 'db.py')).read())
exec(open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "db.py")).read())

application = get_wsgi_application()
