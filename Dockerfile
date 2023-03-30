FROM python:slim

WORKDIR /app
COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt --no-cache-dir
RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "-b", ":8000", "-w", "2","pokedex.wsgi"]