---
title: Webservers
author: linuxtm
layout: page
tags:
  - comenzi linux
  - apache vhost ssl 
  - vhost apache ssl
  - exemplu vhost apache
  - vhost magento nginx
  - exemplu vhost nginx
  - nginx vhost exemplu
  - tutoriale linux
---

Vhost Apache
<pre>
<VirtualHost *:80>
    DocumentRoot "/var/www/html"
    ServerName domain.com
    ServerAlias www.domain.com
    LogLevel error
    ErrorLog logs/domain-error_log
    CustomLog logs/domain-access_log combined

    #Redirect http to https
    RewriteEngine On
    RewriteCond %{HTTPS} !=on
    RewriteRule ^/?(.*) https://%{SERVER_NAME}/$1 [R,L]
    
    #Redirect any url to new domain homepage
    RewriteEngine on
    RewriteRule (.*) https://site.com/ [R=301,L]

    #Port Forwarding
    #ProxyPass / http://localhost:5000/
    #ProxyPassReverse / http://localhost:5000/
    
    #Use https on Wordpress with load balancer (https) when Wordpress server uses http
    #Make sure that X-FORWARDED-PROTO is set on LoadBalancer.
    #Then, add the following to wp-config.php
    #if (strpos($_SERVER['HTTP_X_FORWARDED_PROTO'], 'https') !== false)
    #$_SERVER['HTTPS']='on';
    
<Directory "/var/www/html">
    Options All -Indexes
    AllowOverride All
    Order allow,deny
    Allow from all
    #Order deny,allow
    #Deny from all
    #Allow from 127.1.0.0/16
    #AuthType Basic
    #AuthName "Auth required"
    #AuthUserFile /etc/httpd/user
    #Require valid-user
    #Satisfy any
    DirectoryIndex index.html index.php
    
    #Enable compression
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE text/x-component
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/x-javascript
    
   #Expire headers
    &lt;IfModule mod_expires.c>
    ExpiresActive On
    ExpiresDefault "access plus 10 days"
    ExpiresByType text/css "access plus 1 week"
    ExpiresByType text/plain "access plus 1 day"
    ExpiresByType image/gif "access plus 1 month"
    ExpiresByType image/png "access plus 1 month"
    ExpiresByType image/jpeg "access plus 1 month"
    ExpiresByType application/x-javascript "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 week"
    ExpiresByType application/x-icon "access plus 1 year"
    &lt;/IfModule>
&lt;/Directory>
&lt;/VirtualHost>
</pre>

Vhost Apache SSL
<pre>
<VirtualHost *:443>
    DocumentRoot "/var/www/html/domain/"
    ServerName domain.com
    ServerAlias domain.com
    LogLevel error
    ErrorLog logs/domain-ssl-error_log
    CustomLog logs/domain-ssl-access_log combined
    SSLEngine on
    SSLCertificateFile "/etc/httpd/conf/cert/domain.com.crt"
    SSLCertificateChainFile "/etc/httpd/conf/cert/domain-bundle.crt"
    SSLCertificateKeyFile "/etc/httpd/conf/sslkey/domain.key"
    SSLCipherSuite ALL:-ADH:+HIGH:!MEDIUM:!LOW:!SSLv2:!EXP
	
<Directory "/var/www/html">
    Options All -Indexes
    AllowOverride All
    Order allow,deny
    Allow from all
    #Order deny,allow
    #Deny from all
    #Allow from 127.22.0.0/16
    #AuthType Basic
    #AuthName "Access required"
    #AuthUserFile /etc/httpd/user
    #Require valid-user
    #Satisfy any
    DirectoryIndex index.html index.php
&lt;/Directory>
&lt;/VirtualHost>
</pre>

Vhost Nginx + PHP-FPM
<pre>
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
</pre>

Vhost Nginx + PHP-FPM + Magento 
<pre>
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
</pre>
