# Personal Portfolio Site

A personal portfolio site built in Wagtail :computer:

Deployed with dokku.

## To run locally

First, clone the repo. Then, inside the project folder:
```
pip install -r requirements.txt
```

```
python manage.py migrate
```

```
python manage.py runserver
```

## To Deploy

```
git push dokku master
```

## Pull Database

```
scp root@marykatefain.com:/var/lib/dokku/data/storage/mkf/db.sqlite3 .
scp -r root@marykatefain.com:"/var/lib/dokku/data/storage/mkf/media/*" ./media/

```
