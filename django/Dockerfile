FROM python:3.11-slim

WORKDIR /app

COPY . .

EXPOSE 8000

RUN pip install --no-cache-dir django

CMD [ "python","manage.py","runserver","0.0.0.0:8000"]