import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app
app.secret_key = 'jgygh647uhjf7uyughjfycnbcgjhfg'
