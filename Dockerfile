FROM selenium/standalone-chrome:4.13.0-20231004

USER root
RUN apt update
RUN apt install -y python3-pip
RUN pip install selenium
RUN pip install pandas
RUN pip install beautifulsoup4