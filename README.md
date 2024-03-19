This is a Restaurant booking API
stack: Django web framework, 
Important note: There may be variations in terms of the username and password set for the MySQL user depending on your local machine. Be mindful that the MySQL database that you will be accessing is local to your machine. 

You need to clone the repo. Then, prepare the virtual environment and install all dependencies using the following commands.

```bash
cd <project directory>

pipenv shell

pipenv install django 

pipenv install mysqlclient

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```
