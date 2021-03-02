import os
import time
from . import celery, ResourceTask

# Specifying ResourceTask as the base task so that its properties can be obtained.
@celery.task(name='background_task1', base=ResourceTask)
def background_task1():
    """
    Logic for any heavy duty task can be added here.
    :return: None
    """
    print("Task1 runs in background upon api calling. The shared data is ")
    # Calling the Base Task for getting the data stored in cache
    print(background_task1.shared_resource_data)


@celery.task(name='background_task2', base=ResourceTask)
def background_task2():
    """
    Task2 
    :return: None
    """
    print("background_task2 runs in background upon api calling. The shared data is ")
    # Calling the Base Task for getting the data stored in cache
    print(background_task2.shared_resource_data)