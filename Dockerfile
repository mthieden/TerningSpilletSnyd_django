FROM python:3.7
RUN mkdir /code
COPY requirements.txt /code
WORKDIR /code
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN pip3 install -r requirements.txt
