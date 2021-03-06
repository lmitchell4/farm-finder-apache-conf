
""" Module summary:
Initialize the Flask application.
"""

import os
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

############################################################################

# Initialize flask application:
application = Flask(__name__)


application.register_blueprint(index)
application.register_blueprint(login)
application.register_blueprint(logout)
application.register_blueprint(farm)
application.register_blueprint(catalog)
application.register_blueprint(profile)
application.register_blueprint(event)
application.register_blueprint(error)
application.register_blueprint(apis)

