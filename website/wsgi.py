"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__+'/../')))

project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, project)

activate_this = os.path.join(root, 'bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))


os.environ["DJANGO_SETTINGS_MODULE"] = "website.settings"


from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)