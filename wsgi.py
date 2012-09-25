#!/usr/bin/env python2.7

import sys
import os

PROJECT="webtools"

base = os.path.dirname(__file__)
execfile(os.path.join(base, "bin/django"), {})

os.environ['DJANGO_SETTINGS_MODULE'] = PROJECT + '.settings'

sys.path[0:0] = [
    os.path.join(base, PROJECT),
    os.path.join(base, 'lib/python2.7/site-packages')
]
try:
    import newrelic.agent
    newrelic.agent.initialize(os.path.join(base, 'newrelic.ini'))
except ImportError:
    pass

import django.core.handlers.wsgi 
application = django.core.handlers.wsgi.WSGIHandler()
#from django.core.handlers.wsgi import WSGIHandler
