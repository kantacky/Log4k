FROM python:3.9

RUN apt-get update
RUN apt-get install -y cron
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN chmod 0644 /etc/cron.d/cron

RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD cron -f
