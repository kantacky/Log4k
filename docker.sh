#!/bin/bash
docker stop log4k
docker build -t log4k .
docker run -d --rm --name log4k -t log4k -v /etc/cron.d ./cron.d -v /var/log ./log
