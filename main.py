LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'simple': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },

        'extra_warning_email': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'style': '{',
        },

        'extra_error': {
            'format': '{asctime} {levelname} {message} {pathtime} {exc_info}',
            'style': '{',
        },

        'general__security_file': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },

        'errors_file': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
            'style': '{'
        },



    },


    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },


    'handlers': {
        'console_debug': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },

        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'extra_warning_email'
        },

        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'extra_error'
        },

        'general_file': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'general_security_file',
        },

        'errors_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'errors_file',
        },
        'security_file': {
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'general_security_file',
        },

        'email': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandle',
            'formatter': 'extra_warning_email',
            'filters': ['require_debug_true'],
        }
    },


    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_error', 'general_file'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors_file', 'email'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['errors_file', 'email'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security_file'],
            'propagate': False,
        }
    }
}