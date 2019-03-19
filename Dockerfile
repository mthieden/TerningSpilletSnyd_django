FROM python:3.7
RUN mkdir /code
COPY requirements.txt /code
WORKDIR /code
ENV PYTHONUNBUFFERED 1
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN pip3 install -r requirements.txt
COPY . /code/

RUN apt-get update && apt-get -y install cron

# Add crontab file in the cron directory
ADD cronjob /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Apply cron job
RUN cronjob /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log
