"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.path.append('/srv/eleicao') 
os.path.append('/srv/eleicao/venv/Lib/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()


# add the hellodjango project path into the sys.path


# add the virtualenv site-packages path to the sys.path


# poiting to the project settings
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjango.settings")

# wsgi.py file end
# ===================