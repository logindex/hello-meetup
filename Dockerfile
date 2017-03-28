FROM        python:3.6-alpine

MAINTAINER  Lukasz Skrajny "lukasz.skrajny@logindex.com"
LABEL       description="AWS Meetup Wroclaw #1"

RUN         pip install Flask

ADD         ./code /app
WORKDIR     /app

EXPOSE      5000

CMD         ["python", "server.py"]