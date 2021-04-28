FROM python:3.8.9-slim-buster

COPY highest-profit.py data.csv requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT [ "./highest-profit.py" ]