FROM python:3.8.3-alpine

# FROM python:3.7-alpine
# FROM ubuntu
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements.txt to /requirements.txt in the container
# to avoid reinstalling packages when a container is rebuilt
# it will only reinstall packages when changes has been made to the file
COPY requirements.txt /requirements.txt



#run package installations
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add \
    libffi-dev \
    postgresql-dev \
    libpng \
    git \
    libjpeg-turbo \
    freetype-dev \
    libpng-dev \
    jpeg-dev \
    libjpeg \
    libjpeg-turbo-dev \
    && pip3 install -r /requirements.txt 
    # && pip install -e git+https://github.com/gbozee/django-paystack.git@master#egg=paystack 
    

# RUN apt-get -y update && \
#     apt-get install python3 -y \
#     python3-pip \
#     git \
    # apt-get install -y \
    # libffi-dev \
    # postgresql-dev \
    # libpng \
    # git \
    # libjpeg-turbo \
    # freetype-dev \
    # libpng-dev \
    # jpeg-dev \
    # libjpeg \
    # libjpeg-turbo-dev \
    # && pip3 install -r /requirements.txt 


# set working directory
WORKDIR /var/www/app

# copy project root to app folder in the container
COPY .doc_env /var/www/app
COPY . /var/www/app

EXPOSE 8009
# RUN chmod 400 /var/www/app/start.sh

# ENTRYPOINT ["./start.sh" ]