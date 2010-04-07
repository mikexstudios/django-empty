from django.conf import settings

#from .models import 
#from .helpers import 

#from celery.decorators import task
from celery.task import Task
from celery.registry import tasks

import os

class ExampleTask(Task):
    def run(self, username, project_name, **kwargs):
        logger = self.get_logger(**kwargs)

        logger.info('Executed example task')
        return True
#Don't really need this because of autodiscovery:
#tasks.register(ExampleTask)
