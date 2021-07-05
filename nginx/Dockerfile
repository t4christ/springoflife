# pull official base image
FROM nginx:latest


VOLUME /etc/ssl

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx-selfsigned.crt /etc/ssl
COPY nginx-selfsigned.key /etc/ssl
# COPY nginx.conf /etc/nginx/nginx.conf
COPY ./sites-enabled/default.conf /etc/nginx/conf.d/default.conf