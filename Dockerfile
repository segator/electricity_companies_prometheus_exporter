ARG BASE_IMAGE=jfloff/alpine-python
ARG BASE_IMAGE_TAG=2.7-slim

FROM $BASE_IMAGE:$BASE_IMAGE_TAG

WORKDIR /usr/local/bin

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

ENV LISTENPORT 8111
ENV VERSION 0.58

ADD electricity_exporter.py .
ADD entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 8111

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

