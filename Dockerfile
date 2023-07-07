FROM python:3.9

RUN apt-get update
RUN apt-get install -y cron
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -U pip
RUN pip install -Ur requirements.txt

ADD cron.d /etc/cron.d/
RUN chmod 0644 /etc/cron.d/*

CMD cron && tail -f /dev/null
