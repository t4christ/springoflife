FROM alpine





#run package installations
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add \
    nano \
    postgresql-dev \
    libpng \
    git \
    libjpeg-turbo \
    freetype-dev \
    libpng-dev \
    jpeg-dev \
    libjpeg \
    libjpeg-turbo-dev 
    

EXPOSE 8005


