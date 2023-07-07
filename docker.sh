#!/bin/bash
docker stop log4k
docker build -t log4k .
docker run -v ./log:/var/log -d --rm --name log4k -t log4k
