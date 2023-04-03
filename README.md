# Django-Logging
use django logging module


# Add config in settings.py:

- LOGGING = {
    - 'version': 1,
    - 'disable_existing_loggers': False,
    - 'formatters': {
        - 'verbose': {
            - 'format': '{levelname} {asctime}  {process:d}  {message}',
            - 'style': '{',
        - },
    - },
    - 'handlers': {
        - 'file': {
            - 'level': 'DEBUG',
            - 'class': 'logging.FileHandler',
            - 'filename': './debug.log',
        - },
    - },
    - 'loggers': {
        - '': { # empty string
            - 'handlers': ['file'],
            - 'level': 'DEBUG',
            - 'propagate': True,
        - },
    - },
- }
