FROM python:3.10-slim

FROM python:3.9

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

ENV FLASK_APP=manage:app
ENV TZ America/Bogota

EXPOSE 5000

CMD ["bash", "-c", "flask --app  manage --debug run --host=0.0.0.0"]
