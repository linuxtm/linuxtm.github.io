---
title: Virtualhost Nginx + php-fpm
author: linuxtm
permalink: /vhost-nginx-phpfpm/
layout: post
categories:
  - Webservers
tags:
  - comenzi linux
  - apache vhost ssl 
  - vhost apache ssl
  - exemplu vhost apache
  - vhost magento nginx
  - exemplu vhost nginx
  - nginx vhost exemplu
  - nginx ssl
  - exemple virtual host
  - nginx phpfpm
  - tutoriale linux
---

Exemplu de virtual host Nginx cu php-fpm, ssl, compresie gzip si forward IP real in caz ca suntem in spatele unui proxy.
De asemenea, configul contine si un exemplu de basic auth.

```nginx
#
# A virtual host using mix of IP-, name-, and port-based configuration
#

server {
    listen       80;
    server_name  test.com www.test.com;
    #Redirect to https
    return 301 https://test.com$request_uri;
}

#HTTPS Vhost
server {
    listen       443 ssl;
    server_name  test.com;
    root         /var/www/html;
    index  index.php;
    access_log  /var/log/nginx/test-access.log  main;
    error_log   /var/log/nginx/test-error.log;
    ssl_certificate      /etc/certs/test.com.crt;
    ssl_certificate_key  /etc/certs/test.com.key;
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    
    #PHP-FPM    
    location ~ \.php$ {
    fastcgi_pass 127.0.0.1:9000;
    try_files $uri =404;
    fastcgi_index index.php;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    include fastcgi_params;
    #Set custom php values
    fastcgi_param PHP_VALUE max_execution_time=180;
    fastcgi_param PHP_VALUE max_input_vars=1600;
    
#Set expires
location ~* \.(htm|css|js|txt|swf|asf|asx|wax|wmv|wmx|avi|bmp|class|divx|doc|docx|eot|exe|gz|gzip|ico|png|gif|jpg|jpeg|jpe|mdb|mid|midi|mov|qt|mp3|m4a|mp4|m4v|mpeg|mpg|mpe|mpp|odb|odc|odf|odg|odp|ods|odt|ogg|ogv|webm|htc|ttf|woff2|woff)$ {
    access_log off;
    log_not_found off;
    expires         1y;
    add_header      Cache-Control "max-age=31536000, public";
    add_header 'X-Frame-Options' 'ALLOW-FROM *';
    add_header 'Access-Control-Allow-Origin' '*';
    add_header 'Access-Control-Allow-Credentials' 'true';
    add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
    add_header 'Access-Control-Allow-Headers' 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type';
    }

#Enable gzip compression
    gzip on;
    gzip_types
        application/atom+xml
        application/javascript
        application/json
        application/rss+xml
        application/vnd.ms-fontobject
        application/x-javascript
        application/x-font-ttf
        application/x-web-app-manifest+json
        application/xhtml+xml
        application/xml
        font/opentype
        image/svg+xml
        image/x-icon
        text/css
        text/plain
        text/javascript
        text/x-component;

     }
     
# Forward real IP
http {
        charset             UTF-8;
        set_real_ip_from   192.168.255.0/24;
        real_ip_header     X-Forwarded-For;
        real_ip_recursive  on;

}

#Restrict access to IP / use auth
#location / {
#    satisfy any;
#    allow 192.168.1.0/24;
#    deny  all;

#    auth_basic           "closed site";
#    auth_basic_user_file conf/htpasswd;
#   }

}
```
