from .base import *

env = os.environ.copy()

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

if 'SECRET_KEY' in env:
    SECRET_KEY = env['SECRET_KEY']

if 'ALLOWED_HOSTS' in env:
    ALLOWED_HOSTS = env['ALLOWED_HOSTS'].split(',')
else:
    ALLOWED_HOSTS = ['*']
