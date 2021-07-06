# pull official base image
FROM nginx:latest

RUN mkdir -p /etc/letsencrypt/live/missions.springsoflifeg.com-0001


# VOLUME /etc/letsencrypt/live/missions.springsoflifeg.com-0001

RUN rm /etc/nginx/conf.d/default.conf
COPY fullchain.pem  /etc/letsencrypt/live/missions.springsoflifeg.com-0001
COPY privkey.pem  /etc/letsencrypt/live/missions.springsoflifeg.com-0001

# COPY nginx.conf /etc/nginx/nginx.conf
COPY ./sites-enabled/default.conf /etc/nginx/conf.d/default.conf