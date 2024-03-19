This is a Restaurant booking API
stack: Django web framework, 
Important note: There may be variations in terms of the username and password set for the MySQL user depending on your local machine. Be mindful that the MySQL database that you will be accessing is local to your machine. 

You need to download their zipped project folder and unzip it. Then, prepare the virtual environment and install all dependencies using the following commands.

```bash
cd <project directory>

pipenv shell

pipenv install 

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```
