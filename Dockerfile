FROM python:3-alpine

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

COPY ./ /usr/src/app

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 0

CMD ["python", "/usr/src/app/bin/sentinel.py", "-d"]