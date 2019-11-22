FROM python:3.7-stretch

MAINTAINER Purushotham

RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi \
    vim \
&& apt-get clean \
&& apt-get autoremove \
&& rm -rf /var/lib/apt/lists/*

COPY my_profile/ app/


