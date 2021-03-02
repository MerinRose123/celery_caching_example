from . import app
from .tasks import background_task1, background_task2


@app.route('/task1')
def run_task1():
    # Here background task is called which will run independently. Heavy duty tasks like sending
    # email notifications or processing huge data can be done by this method.
    background_task1.delay()
    return "Flask is up and running. The First celery task is running in background."

@app.route('/task2')
def run_task2():
    """
    View which will call the second celery task.
    """
    background_task2.delay()
    return "Flask is up and running. The Second celery task is running in background."
