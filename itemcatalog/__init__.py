
""" Module summary:
Initialize the Flask application.
"""

from flask import Flask

from .views.index import index
from .views.login import login
from .views.logout import logout
from .views.farm import farm
from .views.catalog import catalog
from .views.profile import profile
from .views.event import event
from .views.error import error
from .apis import apis

#from runpy import run_path

############################################################################

#configs = run_path('/var/www/html/itemcatalog_venv/config.py')
#flask_config_object = configs['flask_config_object']


#import logging
#logger = logging.getLogger()
#logger.warning(configs['CLIENT_SECRETS_FILE']



# Initialize flask application:
application = Flask(__name__)

application.config.from_pyfile('/var/www/html/itemcatalog_venv/config.py')

#application.config.from_object(flask_config_object)
#application.config['APPLICATION_NAME'] = 'testing'

application.register_blueprint(index)
application.register_blueprint(login)
application.register_blueprint(logout)
application.register_blueprint(farm)
application.register_blueprint(catalog)
application.register_blueprint(profile)
application.register_blueprint(event)
application.register_blueprint(error)
application.register_blueprint(apis)

