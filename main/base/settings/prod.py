from .base import *

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '[%(levelname)s] %(asctime)s [%(name)s:%(lineno)s]: %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'file',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 10,
            'filename': os.path.join(BASE_DIR, 'logs/healthyhome.log')
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['file']
        }
    }
}


