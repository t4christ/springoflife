# pull official base image
FROM nginx:latest


# VOLUME /etc/ssl

RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /etc/letsencrypt/live/missions.springsoflifeg.com-0001
# COPY privkey.pem  /etc/ssl
# COPY nginx.conf /etc/nginx/nginx.conf
COPY ./sites-enabled/default.conf /etc/nginx/conf.d/default.conf