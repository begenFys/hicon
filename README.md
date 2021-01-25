# hicon
Для начала нужно установить Django 3 версии(И, конечно же, python 3).
После чего зайти в директорию hicon/web/hicon ввести данные команды по порядку:
- python manage.py makemigrations 
- python manage.py migrate 

И создание суперпользователя:
- python manage.py createsuperuser
Где в username нужно указать email
И в email также email

- python manage.py runserver

И будет запущен локальный сервер, где можно будет всё протестировать.
