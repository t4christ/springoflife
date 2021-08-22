# pull official base image
FROM nginx:latest

RUN mkdir -p /etc/letsencrypt/live/mission.springsoflifeg.com


# VOLUME /etc/letsencrypt/live/missions.springsoflifeg.com-0001

RUN rm /etc/nginx/conf.d/default.conf

# COPY fullchain.pem  /etc/letsencrypt/live/mission.springsoflifeg.com
# COPY privkey.pem  /etc/letsencrypt/live/mission.springsoflifeg.com

# COPY nginx.conf /etc/nginx/nginx.conf
COPY ./sites-enabled/default.conf /etc/nginx/conf.d/default.conf