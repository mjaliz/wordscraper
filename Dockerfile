FROM selenium/standalone-chrome:4.13.0-20231004

USER root
RUN apt update
RUN apt install -y python3-pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt