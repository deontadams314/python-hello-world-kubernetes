FROM python:3-alpine

WORKDIR /web-app

COPY Requirements.txt ./

RUN pip install -r Requirements.txt

COPY . ./

EXPOSE 5050 

ENTRYPOINT ["python3", "hello-flask.py"]

#test
