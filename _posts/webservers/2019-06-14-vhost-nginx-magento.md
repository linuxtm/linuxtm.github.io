---
title: Virtualhost Nginx Magento
author: linuxtm
permalink: /vhost-nginx-magento/
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
  - vhost nginx magento
  - exemple virtual host
  - tutoriale linux
---

Exemplu de virtualhost Nginx pentru Magento 2. Configul de mai jos este similar cu cel dat ca si exemplu pe pagina de documentatie a Magento, deci este o varianta simplificata.

```nginx
server {
    listen 80;
    server_name DOMAIN.com;
    rewrite / $scheme://www.$host$request_uri permanent; ## Forcibly prepend a www
}
  
server {
    listen 80 default;
## SSL directives might go here
    server_name www.DOMAIN.com *.DOMAIN.com; ## Domain is here twice so server_name_in_redirect will favour the www
    root /var/www/vhosts/DOMAIN.com;
  
    location / {
        index index.html index.php; ## Allow a static html file to be shown first
        try_files $uri $uri/ @handler; ## If missing pass the URI to Magento's front handler
        expires 30d; ## Assume all files are cachable
    }
  
    ## These locations would be hidden by .htaccess normally
    location ^~ /app/                { deny all; }
    location ^~ /includes/           { deny all; }
    location ^~ /lib/                { deny all; }
    location ^~ /media/downloadable/ { deny all; }
    location ^~ /pkginfo/            { deny all; }
    location ^~ /report/config.xml   { deny all; }
    location ^~ /var/                { deny all; }
  
    location /var/export/ { ## Allow admins only to view export folder
        auth_basic           "Restricted"; ## Message shown in login window
        auth_basic_user_file htpasswd; ## See /etc/nginx/htpassword
        autoindex            on;
    }
  
    location  /. { ## Disable .htaccess and other hidden files
        return 404;
    }
  
    location @handler { ## Magento uses a common front handler
        rewrite / /index.php;
    }
  
    location ~ .php/ { ## Forward paths like /js/index.php/x.js to relevant handler
        rewrite ^(.*.php)/ $1 last;
    }
  
    location ~ .php$ { ## Execute PHP scripts
        if (!-e $request_filename) { rewrite / /index.php last; } ## Catch 404s that try_files miss
  
        expires        off; ## Do not cache dynamic content
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_param  HTTPS $fastcgi_https;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        fastcgi_param  MAGE_RUN_CODE default; ## Store code is defined in administration > Configuration > Manage Stores
        fastcgi_param  MAGE_RUN_TYPE store;
        include        fastcgi_params; ## See /etc/nginx/fastcgi_params
    }
}
 

    location ~ .php/ { ## Forward paths like /js/index.php/x.js to relevant handler
 
        rewrite ^(.*.php)/ $1 last;
 
    }
 
  
    location ~ .php$ { ## Execute PHP scripts
        if (!-e $request_filename) { rewrite / /index.php last; } ## Catch 404s that try_files miss
        expires        off; ## Do not cache dynamic content
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_param  HTTPS $fastcgi_https;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        fastcgi_param  MAGE_RUN_CODE default; ## Store code is defined in administration > Configuration > Manage Stores
        fastcgi_param  MAGE_RUN_TYPE store;
        include        fastcgi_params; ## See /etc/nginx/fastcgi_params
 
    }
 
}
```
