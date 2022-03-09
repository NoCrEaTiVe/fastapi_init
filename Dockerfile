FROM python:3.8-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/"

WORKDIR /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "--workers=3", "-b 0.0.0.0:5500", "-k uvicorn.workers.UvicornWorker", "app.main:app"]
