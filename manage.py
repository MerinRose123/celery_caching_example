from app import create_app, make_celery

app = create_app()
celery = make_celery(app)

app.app_context().push()

# Importing the api routes. You can also use blueprint for routing in larger applications.
from app import run

if __name__ == '__main__':
    # Running the application in the given port
    print("Running the app")
    app.run(host='0.0.0.0', port=5002)