# DO NOT TOUCH
from flask import Flask
import config

app = Flask(__name__)

app.config.from_object(config)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
# END DO NOT TOUCH

#import all the routes from the routes.py
from StructOpt.views import *;