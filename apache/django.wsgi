import os, sys, site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/ubuntu/.virtualenvs/alaskaenv/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/ubuntu/django/alaska.is')
sys.path.append('/home/ubuntu/django/alaska.is/alaska')

os.environ['DJANGO_SETTINGS_MODULE'] = 'alaska.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/ubuntu/.virtualenvs/alaskaenv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()