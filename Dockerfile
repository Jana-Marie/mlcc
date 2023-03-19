FROM nginx:alpine
COPY ./www /usr/share/nginx/html
EXPOSE 5123
CMD ["/bin/sh", "-c", "sed -i 's/listen  .*/listen 5123;\\ncharset utf-8;/g' /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'"]
