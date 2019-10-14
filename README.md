# Personal Portfolio Site

A personal portfolio site built in Wagtail :computer:

Deployed with dokku.

## To run locally

### Initial setup

```sh
sudo -H pip3 install mkvirtualenvwrapper
```

Add the following lines to the bottom of `~/.bashrc`:

```sh
# Virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Projects
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

Create the virtualenv:

```sh
mkvirtualenv mk_website
```

Clone the repo. Then, inside the project folder:

```sh
workon mk_website

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Each time

When returning to the project, change into the project directory and run:

```sh
workon mk_website
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
