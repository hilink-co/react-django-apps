# React Django apps

## Prerequisite

You must have Docker installed your computer, follow [this instruction](https://docs.docker.com/get-docker/) to do so.

## Tech stack

- Frontend:
  - React
    - Node: latest
  - Typescript: latest
- Backend:
  - Python: 3.12
  - Django: 3.5
- Storage:
  - MySQL: 8.0

## Install

- Spin up apps using Docker compose

> docker-compose up -d

- Run migrations

> python manage.py makemigrations backend
> python manage.py migrate backend

## Start backend

> docker exec -ti <backend-app-container> bash

You should see a project directory like below:
```
backend/
  migrations/
  __init__.py
  asgi.py
  urls.py
  views.py
  wsgi.py
Dockerfile
manage.py
requirements.txt
```

Start Django app:

> python manage.py runserver 0.0.0.0:8000

## Run backend tests

> docker compose exec backend bash

> pytest



## Start frontend

> docker compose exec frontend bash

> yarn start

You can access the starter React app on `localhost:3000`

