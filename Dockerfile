FROM python:3-alpine

ADD Requirements.txt Hello-World/ ./

RUN pip install -r Requirements.txt

EXPOSE 8000

ENTRYPOINT ["python3", "Hello-World/hello-flask.py"]