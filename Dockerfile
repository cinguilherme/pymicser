FROM ubuntu:latest
MAINTAINER Cintra, Guilherme "cinguilherme@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /user-service-f
WORKDIR /user-service-f
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]