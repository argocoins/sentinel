FROM python:3-alpine

RUN mkfifo -m 0666 /var/log/cron.log
RUN echo "* * * * * python /usr/src/app/bin/sentinel.py >> /var/log/cron.log 2>&1"

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

COPY ./ /usr/src/app

WORKDIR /usr/src/app

CMD ["python", "/usr/src/app/bin/sentinel.py", "-d"]