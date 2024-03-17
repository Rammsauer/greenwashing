FROM python:3.12

RUN apt-get update

RUN apt-get -y install git

RUN git config --global user.email ""
RUN git config --global user.name ""

ADD . .

CMD [ "python", "-u", "main.py" ]
