FROM python:3.12-slim

WORKDIR /code

COPY ./src/requirements.txt /code/requirements.txt
COPY ./src/python-hessian /code/python-hessian
RUN pip install -r requirements.txt
RUN pip install uvicorn

COPY ./src/app /code/app

EXPOSE 8080
CMD uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload