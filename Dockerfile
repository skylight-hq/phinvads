FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY ./src /code

EXPOSE 8080
CMD uvicorn main:app --host 0.0.0.0 --port 8080 --reload