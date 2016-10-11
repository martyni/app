From nginx

COPY append /etc/nginx/conf.d/
COPY default.raw /etc/nginx/conf.d/
CMD envsubst < /etc/nginx/conf.d/default.raw > /etc/nginx/conf.d/default.conf &&\ 
    cat /etc/nginx/conf.d/append >> /etc/nginx/conf.d/default.conf &&\
    nginx -g 'daemon off;'
