FROM nginx:1.19.0-alpine

RUN \
    rm /etc/nginx/nginx.conf && \
    rm /etc/nginx/conf.d/default.conf

ADD nginx.conf /etc/nginx/
ADD nginx.d/service.conf /etc/nginx/conf.d
