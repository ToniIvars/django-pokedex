# Django Pokedex

This is a web project made with Django that aims to be like a Pokedex (up to the 7th generation).

## Setup

The easiest way to setup this project is with Docker. Just run the following commands:

```bash
git clone https://github.com/ToniIvars/django-pokedex
docker build -t django-pokedex .
```

After building the docker image, you must change the **SECRET_KEY** environment variable in the **docker-compose.yml** file.
You can generate one using [Djecrety](https://djecrety.ir/).

Now, to build the container, you just have to run `docker compose up -d`.

At this point, you will have the web app running, and you just have to visit [http://localhost:8000/](http://localhost:8000) to see it.