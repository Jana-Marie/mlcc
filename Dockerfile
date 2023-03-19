FROM nginx:alpine
COPY . /usr/share/nginx/html
EXPOSE 5099
CMD ["/bin/sh", "-c", "sed -i 's/listen  .*/listen 5099;\\ncharset utf-8;/g' /etc/nginx/conf.d/default.conf && exec nginx -g 'daemon off;'"]