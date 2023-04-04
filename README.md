# django_euf

## Installation
1. Clone this repository.
2. Download and install Node (v.16+) from this URL:
```
https://nodejs.org/en/download
```
3. Once Node is installed you should be able to install Yarn using:
```
npm install --global yarn
```
4. Next, run:
```
gulp
```
5. Finally, install Python 3.9+ from:
```
https://www.python.org/downloads/
```
- For best compatability, use python 3.9.13

6. Create a new account on sendgrid.com and obtain your API key. We'll use this API to send emails 
(password recovery, account verification, etc.). Free plan allows you to send 100 emails a day.
```
https://sendgrid.com/
```



## Configuration
1. Make sure you have virtual environment installed and ready. If not, run following:
```
python -m venv venv
source venv/bin/activate
```

2. Once the virtual environment is ready, run following:
```
pip install -r requirements.txt
pip install django django-allauth django-embed-video django-crispy-forms
python -m pip install --upgrade pip
```

3. Run the scripts inside mariadb_scripts folder to create a new user and database. Modify init file as per your needs.

4. If you don't want to modify the scripts, your default database name will be 'django_euf' and the database username and
password will be 'root' and 'asdasdasd'

5. Update settings.py in the main directory to configure database connectivity:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.#databaseservername#',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': 'host',
        'PORT': 'port',
    }
}
```
- Follow the official documentation if you want to use a new database:
```
https://docs.djangoproject.com/en/4.1/ref/databases/
```

6. Execute the following command to create a superuser:
```
python manage.py createsuperuser
```
- If you don't want to create a new superuser, the default superuser is provided:
```
pranav
asdASD123!
```

7. Finally, run:
```
python manage.py runserver
```

- If you want to have extensive overview of runserver, run:
```
python manage.py runserver_plus
```

## Usage
1. By default, your website will run at:
```
http://localhost:8000/
```
2. Admin panel access (login with superuser credentials:
```
http://localhost:8000/admin/
```
3. Account access:
```
http://localhost:8000/account/login/?next=/
```

## Support
This repository is still not fully developed. We're adding new features as and when required. If you face any errors,
please contact the authors.

## Authors and acknowledgment

## License
