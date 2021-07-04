# pull official base image
FROM nginx:latest

RUN mkdir -p ssl/certs
RUN mv ssl/certs /etc/ssl
VOLUME /etc/ssl/certs

RUN rm /etc/nginx/conf.d/default.conf
COPY privkey.pem /etc/ssl/certs
COPY fullchain.pem /etc/ssl/certs
# COPY nginx.conf /etc/nginx/nginx.conf
COPY ./sites-enabled/default.conf /etc/nginx/conf.d/default.conf