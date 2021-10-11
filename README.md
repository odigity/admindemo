Dev Cycle

* `rm db.sqlite3 worlds/migrations/0001_initial.py; ./manage.py makemigrations` _(skip first time)_
*  `./manage.py migrate; ./manage.py loaddata worlds/examples`
*  `./manage.py runserver`
