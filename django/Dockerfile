FROM python:3.11-slim

WORKDIR /app

COPY . .

EXPOSE 8000

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "votesystem.wsgi:application"]