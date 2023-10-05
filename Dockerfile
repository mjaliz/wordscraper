FROM python:3.10.12

RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.198-1_amd64.deb   && sudo apt install -y /tmp/chrome.deb   && rm /tmp/chrome.deb

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt