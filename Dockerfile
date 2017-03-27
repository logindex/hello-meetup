FROM centos:7

MAINTAINER Lukasz Skrajny "lukasz.skrajny@logindex.com"
LABEL      description="AWS Meetup Wroclaw #1"

RUN yum -y update
RUN yum install -y epel-release

RUN yum install -y python-pip python-devel; \
    yum clean all;

RUN pip install --upgrade pip

RUN pip install Flask

COPY        server.py /app/server.py
WORKDIR     /app

EXPOSE      5000

CMD         ["python", "server.py"]