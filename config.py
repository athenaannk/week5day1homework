import os

basedir=os.path.abs(os.path.dir(__name__))

class Config():
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG=1')