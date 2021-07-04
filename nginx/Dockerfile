# pull official base image
FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY privkey.pem /etc/letsencrypt/live/missions.springsoflifeg.com
COPY fullchain.pem /etc/letsencrypt/live/missions.springsoflifeg.com

# COPY nginx.conf /etc/nginx/nginx.conf
COPY ./sites-enabled/default.conf /etc/nginx/conf.d/default.conf