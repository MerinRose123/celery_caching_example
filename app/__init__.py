import os

from celery import Celery, Task
from celery_config import CeleryConf
from config import config_by_name
from flask import current_app
from flask import Flask

# Declared globally for easy access
celery = Celery(__name__)
app = Flask(__name__)


def create_app():
    # Change environment variable to get into development environment mode
    app.config.from_object(config_by_name[os.getenv('FLASK_ENVIRONMENT') or 'local'])
    return app


def make_celery(app):
    # create context tasks in celery
    celery.conf.update(app.config)
    celery.config_from_object(CeleryConf)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


class ResourceTask(Task):
    """
    Class to load all the big resources like the csv files only once which can be used by all celery processes.
    """    
    def __init__(self):
        # The cache is initialized here. It can be acces though all child tasks whose base is ResourceTask.
        #  The cache will get initialized when celery is initialized.
        self.cache = current_app.config['RESOURCE_CACHE']    

    @property
    def shared_resource_data(self):
        if self.cache.get("shared_resource_data") is None:
            print("Reloading the cache with the required value")   
            self.cache["shared_resource_data"] = "The big resource data to be stored. Can include models key-values etc"

        return self.cache.get("shared_resource_data")

