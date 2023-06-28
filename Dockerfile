FROM python:3.9

RUN apt-get update
RUN apt-get install -y cron
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -U pip
RUN pip install -Ur requirements.txt

CMD cron -f
