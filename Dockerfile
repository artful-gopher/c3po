FROM python:3.7.7-slim
MAINTAINER Yugam Sharma (yugam.sharma@yahoo.com)
RUN apt-get update
RUN apt-get install -y curl
RUN pip3 install slackclient
