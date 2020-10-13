---
title: Apache CORS domenii multiple
author: linuxtm
permalink: /apache-cors-domenii-multiple/
layout: post
categories:
  - Webservers
tags:
  - comenzi linux
  - apache cors 
  - apache cors mai multe domenii
  - apache cors exemplu domenii
  - permite apache cors domenii
  - exemplu apache cors
  - domenii cors apache
  - configurare cors apache mai multe domenii
  - apache cors multiple domains
  - tutoriale linux
---

Configurarea CORS de mai jos permite accesul de la 2 domenii (www.linuxtm.ro, linuxtm.ro, www.example.com si example.com) pe fisierul /dir/file.php
<pre>
<Location "/dir/file.php">
   Allow from all
   AllowOverride none
   SetEnvIf Origin "http(s)?://(www\.)?(linuxtm.ro|example.com)$" AccessControlAllowOrigin=$0
   Header set Access-Control-Allow-Origin %{AccessControlAllowOrigin}e env=AccessControlAllowOrigin
</Location>
</pre>
