FROM ubuntu:16.04

MAINTAINER Cintra, Guilherme "cinguilherme@gmail.com"

RUN adduser ubuntu

WORKDIR /home/ubuntu/

RUN apt-get update -y \
	&& apt-get install -y python-pip python-dev python3-pip python3-dev build-essential gcc wget \
	&& wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz \
	&& tar -xf Python-3.6.4.tgz \
	&& cd Python-3.6.4 \
	&& ./configure \
	&& make altinstall

WORKDIR /home/ubuntu/

RUN git clone https://github.com/cinguilherme/pymicser.git \
	&& mkdir user-service-f
	&& mv -R /home/ubuntu/pymicser/ /home/ubuntu/user-service-f/

WORKDIR /user-service-f

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3.6","app.py"]