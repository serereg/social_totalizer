#!/bin/bash
#docker system prune
docker build --tag totalizer .
docker run --rm --publish 8080:8080 --name cont_totalizer totalizer
#./venv/bin/python main.py
#docker  exec -it <container name> /bin/bash
