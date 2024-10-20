---
title: Virtualhost Nginx Magento2 cu CDN
author: linuxtm
permalink: /vhost-nginx-magento2-cdn/
layout: post
categories:
  - Webservers
tags:
  - comenzi linux
  - apache vhost ssl 
  - vhost apache ssl
  - nginx magento2 cdn
  - magento2 cdn subdomenii nginx
  - subdomenii nginx pentru continut static magento
  - vhost magento nginx
  - exemplu vhost nginx
  - nginx vhost exemplu
  - nginx ssl
  - vhost nginx magento
  - exemple virtual host
  - tutoriale linux
---

Mai jos avem cele trei config-uri de nginx necesare pentru configurarea Magento 2 cu CDN.
In acest exemplu folosim 2 subdomenii separate pentru media si resursele statice.

**Vhost domeniu principal**
```nginx
upstream fastcgi_backend {
    server   127.0.0.1:9000;
}

server {
    listen         80;
    server_name    domain.com;

    location / {
      return 301 https://$http_host$request_uri;
    }
}

server {
    listen         80;
    server_name    www.domain.com;

    location / {
      return 301 https://$http_host$request_uri;
    }
}


server {
    listen      443 ssl http2;
    server_name www.domain.com;
    ssl_certificate /etc/letsencrypt/live/www.domain.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.domain.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    location / {
      return 301 https://domain.com$request_uri;
    }

}



server {
    listen      443 ssl http2 default_server;
    server_name domain.com;

    ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    ## Define project root
    set $MAGE_ROOT /var/www/html;

    ##  Magento mode production or developer
    set $MAGE_MODE production;

     access_log  /var/log/nginx/domain-access.log;
     error_log   /var/log/nginx/domain-error.log;

    client_max_body_size 10M;
    merge_slashes off;

    root $MAGE_ROOT/pub;

    index index.php;
    autoindex off;
    charset off;

    #Monitoring
    location /nginx_status {
        stub_status on;
        allow 127.0.0.1;
        deny all;
        #access_log   off;
    }


    location /setup {
        root $MAGE_ROOT;
        location ~ ^/setup/index.php {
            fastcgi_pass   fastcgi_backend;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            include        fastcgi_params;
        }

        location ~ ^/setup/(?!pub/). {
            deny all;
        }

        location ~ ^/setup/pub/ {
            add_header X-Frame-Options "SAMEORIGIN";
        }
    }

    location /update {
        root $MAGE_ROOT;

        location ~ ^/update/index.php {
            fastcgi_split_path_info ^(/update/index.php)(/.+)$;
            fastcgi_pass   fastcgi_backend;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            fastcgi_param  PATH_INFO        $fastcgi_path_info;
            include        fastcgi_params;
        }

        # deny everything but index.php
        location ~ ^/update/(?!pub/). {
            deny all;
        }

        location ~ ^/update/pub/ {
            add_header X-Frame-Options "SAMEORIGIN";
        }
    }

    location / {
        index index.php;
        try_files $uri $uri/ /index.php?$args;
    }

    location /pub {
        location ~ ^/pub/media/(downloadable|customer|import|theme_customization/.*\.xml) {
            deny all;
        }
        alias $MAGE_ROOT/pub;
        add_header X-Frame-Options "SAMEORIGIN";
    }

    location /static/ {
        if ($MAGE_MODE = "production") {
            expires max;
        }

        # remove signature of static files used to overcome browser cache
        location ~ ^/static/version {
          rewrite ^/static/(version\d*/)?(.*)$ /static/$2 last;
        }

        location ~* \.(ico|jpg|jpeg|png|gif|svg|js|css|swf|eot|ttf|otf|woff|woff2)$ {
            add_header Cache-Control "public";
            add_header X-Frame-Options "SAMEORIGIN";
            expires +1y;

            if (!-f $request_filename) {
                rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=$2 last;
            }
        }

        location ~* \.(zip|gz|gzip|bz2|csv|xml)$ {
            add_header Cache-Control "no-store";
            add_header X-Frame-Options "SAMEORIGIN";
            expires    off;

            if (!-f $request_filename) {
               rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=$2 last;
            }
        }
        if (!-f $request_filename) {
            rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=$2 last;
        }
        add_header X-Frame-Options "SAMEORIGIN";
    }

    location /media/ {
        try_files $uri $uri/ /get.php?$args;

        location ~ ^/media/theme_customization/.*\.xml {
            deny all;
        }

        location ~* \.(ico|jpg|jpeg|png|gif|svg|js|css|swf|eot|ttf|otf|woff|woff2)$ {
            add_header Cache-Control "public";
            add_header X-Frame-Options "SAMEORIGIN";
            expires +1y;
            try_files $uri $uri/ /get.php?$args;
        }
        location ~* \.(zip|gz|gzip|bz2|csv|xml)$ {
            add_header Cache-Control "no-store";
            add_header X-Frame-Options "SAMEORIGIN";
            expires    off;
            try_files $uri $uri/ /get.php?$args;
        }
        add_header X-Frame-Options "SAMEORIGIN";
    }

    location /media/customer/ {
        deny all;
    }

    location /media/downloadable/ {
        deny all;
    }

    location /media/import/ {
        deny all;
    }

    location ~ cron\.php {
        deny all;
    }

    location ~ (index|get|static|report|404|503)\.php$ {
        index index.php;
        try_files $uri =404 /index.php;
        fastcgi_pass   fastcgi_backend;
        fastcgi_param  PHP_FLAG  "session.auto_start=off \n suhosin.session.cryptua=off";
        fastcgi_param  PHP_VALUE "memory_limit=1024M \n max_execution_time=18000";
        fastcgi_read_timeout 600s;
        fastcgi_connect_timeout 600s;
        fastcgi_param  MAGE_MODE $MAGE_MODE;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        include        fastcgi_params;
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
```

**Vhost fisiere media**
```nginx
#Serve media files
server {
    listen         80;
    server_name media.domain.com;
    return 301 https://media.domain.com$request_uri;
}


server {
    listen      443 ssl http2;
    server_name media.domain.com;
    ssl_certificate /etc/letsencrypt/live/media.domain.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/media.domain.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot


    client_max_body_size 10M;
    merge_slashes off;

    ##  Magento mode production or developer
    set $MAGE_MODE production;

    root /var/www/html/pub;

    index index.php;
    autoindex off;
    charset off;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location /static/ {
        if ($MAGE_MODE = "production") {
            expires max;
        }
        # remove signature of static files used to overcome browser cache
        location ~ ^/static/version {
          rewrite ^/static/(version\d*/)?(.*)$ /static/$2 last;
    }

        location ~* \.(htm|html|css|js|txt|swf|asf|asx|wax|wmv|wmx|bmp|class|divx|doc|docx|eot|gz|gzip|ico|png|gif|jpg|jpeg|jpe|mdb|qt|mpeg|mpg|mpe|mpp|odb|odc|odf|odg|odp|ods|odt|ogg|ogv|webm|htc|woff|woff2|ttf|pdf|svg)$ {
            add_header Cache-Control "public";
            add_header 'X-Frame-Options' 'ALLOW-FROM *';
            add_header 'Access-Control-Allow-Origin' '*';
            expires +1y;

            if (!-f $request_filename) {
                rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=$2 last;
            }
        }

        location ~* \.(zip|gz|gzip|bz2|csv|xml)$ {
            add_header Cache-Control "no-store";
            add_header X-Frame-Options "SAMEORIGIN";
            expires    off;

            if (!-f $request_filename) {
               rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=$2 last;
            }
        }
        if (!-f $request_filename) {
            rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=$2 last;
        }
        add_header X-Frame-Options "SAMEORIGIN";
    }

    location /media/ {
        try_files $uri $uri/ /get.php?$args;

        location ~ ^/media/theme_customization/.*\.xml {
            deny all;
        }

        location ~* \.(ico|jpg|jpeg|png|gif|svg|js|css|swf|eot|ttf|otf|woff|woff2)$ {
            add_header Cache-Control "public";
            add_header X-Frame-Options "SAMEORIGIN";
            expires +1y;
            try_files $uri $uri/ /get.php?$args;
        }
        location ~* \.(zip|gz|gzip|bz2|csv|xml)$ {
            add_header Cache-Control "no-store";
            add_header X-Frame-Options "SAMEORIGIN";
            expires    off;
            try_files $uri $uri/ /get.php?$args;
        }
        add_header X-Frame-Options "SAMEORIGIN";
    }

    location /media/customer/ {
        deny all;
    }

    location /media/downloadable/ {
        deny all;
    }

    location /media/import/ {
        deny all;
    }

    location ~ cron\.php {
        deny all;
    }

    location ~ (index|get|static|report|404|503)\.php$ {
        try_files $uri $uri/ =404 /index.php;
        fastcgi_pass   fastcgi_backend;
        fastcgi_param  PHP_FLAG  "session.auto_start=off \n suhosin.session.cryptua=off";
        fastcgi_param  PHP_VALUE "memory_limit=1024M \n max_execution_time=18000";
        fastcgi_read_timeout 600s;
        fastcgi_connect_timeout 600s;
        fastcgi_param  MAGE_MODE $MAGE_MODE;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        include        fastcgi_params;
    }
}
```

**Vhost fisiere statice (css, js)**
```nginx
#Serve JS and CSS
server {
    listen         80;
    server_name static.domain.com;
    return 301 https://static.domain.com$request_uri;
}


server {
    listen      443 ssl http2;
    server_name static.domain.com;
    root /var/www/html/pub;
    
    access_log  /var/log/nginx/static-access.log;
    error_log   /var/log/nginx/static-error.log;
    
    ssl_certificate /etc/letsencrypt/live/static.domain.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/static.domain.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    client_max_body_size 10M;
    merge_slashes off;
    autoindex off;
    charset off;
    
    location ~ ^/static/version {
        # Preflighted requests - KEEP THIS ABOVE THE REWRITE RULE
        if ($request_method = OPTIONS ) {
          add_header "Access-Control-Allow-Origin"  "https://main-domain.com";
          add_header "Access-Control-Allow-Methods" "GET, POST, OPTIONS, HEAD";
          add_header "Access-Control-Allow-Headers" "Authorization, Origin, X-Requested-With, Content-Type, Accept";
          return 200;
        }
        expires +1y;
        #remove signature of static files used to overcome browser cache
        rewrite ^/static/(version\d*/)?(.*)$ /static/$2 last;
    }

    # Match MIME types
    location ~* \.(htm|html|css|js|txt|swf|asf|asx|wax|wmv|wmx|avi|bmp|class|divx|doc|docx|eot|gz|gzip|ico|png|gif|jpg|jpeg|jpe|mdb|mov|qt|mpg|mpe|mpp|odb|odc|odf|odg|odp|ods|odt|ogv|json|webm|htc|woff|woff2|ttf|pdf|svg)$ {
        add_header Cache-Control 'public';
        add_header Access-Control-Allow-Origin 'https://main-domain.com';
        add_header 'Access-Control-Allow-Headers' 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type';
        expires +1y;
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
```
