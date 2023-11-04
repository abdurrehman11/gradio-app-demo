FROM python:3.10

RUN apt-get update

WORKDIR /code 

COPY ./requirements.txt /code/requirements.txt 

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENV GRADIO_SERVER_PORT=7860
EXPOSE ${GRADIO_SERVER_PORT}

CMD [ "python", "./app/demo.py" ]