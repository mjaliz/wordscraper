FROM selenium/standalone-chrome:4.13.0-20231004

USER root
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt