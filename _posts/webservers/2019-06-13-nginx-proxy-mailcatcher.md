---
title: Nginx proxy Mailcatcher
author: linuxtm
permalink: /nginx-proxy-mailcatcher/
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
  - nginx proxy mailcatcher
  - exemple virtual host
  - tutoriale linux
---

<pre>
    location /mailcatcher {
        satisfy any;
        allow trustedip;
        deny all;
        proxy_pass  http://backendip:1080/;
    }

    location /assets {
        proxy_pass  http://backendip:1080/assets/;
    }

    location /messages {
        proxy_pass  http://backendip:1080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
</pre>
