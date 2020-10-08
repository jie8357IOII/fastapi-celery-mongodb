import celery

# set the default Django settings module for the 'celery' program.
app = celery.Celery('app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix. 

config = {}

celery_app.config_from_object(config, namespace='CELERY')