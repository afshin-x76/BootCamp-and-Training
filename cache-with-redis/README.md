# Django Caching with redis

simple app to show caching in python

you can change backend to whatever you want.

### install dependencies

- django_redis
- Redis
- django-debug-toolbar

#### install redis

1. `sudo apt update`
2. `sudo apt install redis-server`
3. test it with `redis-cli ping` output must be `PONG`

pip3 install -r requirements.txt

if you have your own database, you can load data with:
`python3 manage.py loaddata fixture.json`