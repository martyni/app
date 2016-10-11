From nginx


COPY default.raw /etc/nginx/conf.d/
CMD envsubst < /etc/nginx/conf.d/default.raw > /etc/nginx/conf.d/default.conf &&\ 
    #echo '     return 301 https://$host$request_uri;' >> /etc/nginx/conf.d/default.conf &&\
    #echo '}' >>/etc/nginx/conf.d/default.conf &&\
    nginx -g 'daemon off;'
