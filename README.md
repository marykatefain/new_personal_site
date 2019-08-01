# Personal Portfolio Site

A personal portfolio site built in Wagtail :computer:

Deployed with dokku.

## To run locally

First, clone the repo. Then, inside the project folder:

```
python3 -m venv env

source env/bin/activate

pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py runserver

```

## To Deploy

```
git push dokku master
```
