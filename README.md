# celery_caching_example
Caching in celery using LRUCache in flask framework.

The application serves as an example for using the in build LRUCache option of celery. This cache can be used to store and use a data across mulltipel tasks. The data can be kry-values, models etc.

### Prerequisites
* The redis server should be up and running in port 6379.

* Python should be installed in the system. The application is compatible with python 3.8.5. 
  Generally python3 would be suitable for the app.

### Setting up virtual environment

To avoid conflict with the system environment it is recommended to use the application inside a virtual environment.
steps:

* Install virtual env with the command `sudo pip3 install virtualenv ` if not already installed.

* Create a virtual env for your app `virtualenv -p python3  venv_name`

* Activate the virtual env with command `source venv_name/bin/activate`
  
* Run the application in virtual env activated terminal.
  
After use, you can deactivate the virtual env using command `deactivate`

### Installing requirements

The requirements for the application can be installed by getting into the folder where requirement.txt resides.

Then type `pip install -r requirements.txt`

### How To Run the App
* To run the application  type `python manage.py`.

* To start celery along with celery beat type 
`celery worker -A manage.celery --loglevel=INFO`
