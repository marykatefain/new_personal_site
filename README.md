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
