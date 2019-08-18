FROM python:3-alpine

WORKDIR /web-app

COPY Requirements.txt hello-flask.py ./

RUN pip install -r Requirements.txt

EXPOSE 5050 

ENTRYPOINT ["python3", "hello-flask.py"]
