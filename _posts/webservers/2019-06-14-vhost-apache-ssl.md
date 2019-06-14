---
title: Webservers
author: linuxtm
permalink: /vhost-apache-ssl/
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
