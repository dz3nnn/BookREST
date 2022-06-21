### The environment variables
DJANGO_SECRET_KEY
DEBUG
DATABASE_URL
#### Gunicorn
```
gunicorn --worker-tmp-dir /dev/shm BookREST.wsgi
```
