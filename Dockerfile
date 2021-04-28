FROM python:3.8.9-slim-buster

WORKDIR /scripts

COPY highest-profit.py requirements.txt /scripts/

RUN pip install -r requirements.txt && ln -s /scripts/highest-profit.py /usr/local/bin

WORKDIR /root

ENTRYPOINT [ "highest-profit.py" ]