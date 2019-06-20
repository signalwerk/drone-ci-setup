FROM alpine:latest
MAINTAINER sh@signalwerk.ch

RUN apk add --no-cache bash curl

RUN mkdir -p /opt/dropbox_uploader

COPY ./dropbox_uploader.sh /opt/dropbox_uploader
RUN chmod -R a+x /opt/dropbox_uploader/dropbox_uploader.sh

# script cannot have a period "." in filename! It cannot end in .sh.
COPY ./periodic/daily/* /etc/periodic/daily
RUN chmod a+x /etc/periodic/daily/*

WORKDIR /workdir

# https://gist.github.com/AntonFriberg/692eb1a95d61aa001dbb4ab5ce00d291
# This runs cron in the foreground with loglevel 2

CMD [ "crond", "-l", "2", "-f" ]
