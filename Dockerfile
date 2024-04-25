FROM ghcr.io/cdcgov/phdi/dibbs

WORKDIR /code

COPY ./phinvads/requirements.txt /code/requirements.txt
COPY ./python-hessian /python-hessian
RUN pip install -r requirements.txt

COPY ./phinvads/app /code/app
COPY ./phinvads/description.md /code/description.md

EXPOSE 8080
CMD uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload