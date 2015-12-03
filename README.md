# View Logger

This module logs to page requests to the database. It works through a
monkey patch so it does not run anything until the request has been
sent to the user.

In your settings.py add the line

    'viewcount.middleware.ViewCountMiddleware',

Also run 

    ./manage.py makemigrations
    ./manage.py migrate
