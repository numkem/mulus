FROM ubuntu
MAINTAINER Sebastien Bariteau <numkem@numkem.org>

RUN apt-get update
RUN apt-get -y install python-pip git python-dev
RUN mkdir /server
RUN git clone https://github.com/numkem/mulus.git /server/
RUN pip install -r /server/requirements.txt

EXPOSE 5000
ENTRYPOINT python /server/app.py
