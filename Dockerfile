FROM python:3.9-slim

WORKDIR /totalizer
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./ .
RUN pip install -e ./
EXPOSE 8080
CMD python -m totalizer
