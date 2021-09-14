FROM python:alpine

RUN apk add dialog && apk update && pip3 install click pythondialog pyyaml jinja2

COPY . /

ENTRYPOINT ["/dialog_selector.py"]