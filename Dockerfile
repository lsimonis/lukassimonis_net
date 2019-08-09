FROM python:3
MAINTAINER Lukas Simonis <lsimonis@gmail.com>

#Set variables
ENV PROJECT=lukassimonis_net
ENV CONTAINER_HOME=/home/django/app
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

# Create user and group to run as
RUN groupadd django && useradd -m -g django -s /bin/sh django
RUN mkdir -p $CONTAINER_HOME

# Create project subdirectories
WORKDIR $CONTAINER_HOME
RUN mkdir logs

# Copy requirements.txt and install dependencies
COPY ./requirements.txt $CONTAINER_HOME
RUN pip install --no-cache-dir -r $CONTAINER_HOME/requirements.txt

# Copy django files to container
COPY . $CONTAINER_HOME

# Copy and set entrypoint
#WORKDIR $CONTAINER_PROJECT
COPY ./entrypoint.sh .
ENTRYPOINT ["./entrypoint.sh"]

# Set file permissions for unpriveliged user
RUN chown -R django:django /home/django

# Open port
EXPOSE 8000

# Set user
USER django

# Run Gunicorn - use entrypoint.sh instead
#CMD ["gunicorn", "--access-logfile", "-", "--error-logfile", "-", "-w", "2", "-b", ":8000", "lukassimonis_net.wsgi"]
