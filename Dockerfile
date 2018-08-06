FROM python:3-alpine

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

COPY ./ /usr/src/app

WORKDIR /usr/src/app

CMD ["python", "/usr/src/app/bin/sentinel.py", "-d"]