FROM ubuntu:14.04
MAINTAINER Arne Schauf

RUN apt-get update && apt-get upgrade -y &&  apt-get install -y\
    python-dev\
    python-pip\
    zlib1g-dev\
    libjpeg8-dev\
    libxml2-dev\
    libxslt1-dev\
    lib32z1-dev\
    libmemcached-dev\
    postgresql-server-dev-all\
    git\
    python-virtualenv\
    postgresql-client

EXPOSE 8000

ADD . /opt/code
WORKDIR /opt/code
RUN pip install -Ur requirements.txt

RUN useradd hopperpw
USER hopperpw

WORKDIR hopperpw
CMD ["python2", "manage.py", "runserver", "0.0.0.0:8000"]
