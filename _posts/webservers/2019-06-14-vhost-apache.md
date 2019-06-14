---
title: Webservers
author: linuxtm
permalink: /vhost-apache/
layout: page
tags:
  - comenzi linux
  - apache vhost ssl 
  - vhost apache ssl
  - exemplu vhost apache
  - vhost magento nginx
  - exemplu vhost nginx
  - nginx vhost exemplu
  - nginx ssl
  - exeple virtual host
  - tutoriale linux
---

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
