#!/usr/bin/python
activate_this = '/var/www/html/itemcatalog_venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))


import sys, os
import logging

logging.basicConfig(stream=sys.stderr)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,BASE_DIR)


def application(environ, start_response):
  for key in ['DATABASE_URI']:
    os.environ[key] = environ.get(key,'')

  from itemcatalog import application
  CONFIG_FILE = environ.get('CONFIG_FILE','')
  application.config.from_pyfile(CONFIG_FILE)

  return application(environ, start_response)
