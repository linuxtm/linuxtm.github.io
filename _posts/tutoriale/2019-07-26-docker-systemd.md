---
title: Docker ca si serviciu de sistem (systemd)
author: linuxtm
layout: post
permalink: /docker-systemd/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - configurare docker systemd
  - tutorial systemd docker
  - docker systemd
  - serviciu de sistem
  - centos7 systemd docker
  - run command inside docker container as systemd service
  - execute docker command inside docker systemd
---

Exemplu de fisier systemd pentru un container docker, in care executam niste comenzi dupa ce a pornit containerul de docker.


Foarte important este <b>sleep 1</b> , fara adaugarea unei intarzieri comenzile <em>docker exec</em> nu vor functiona deoarece <em>ExecStartPost</em> se va executa inainte sa fie ready containerul de docker.

Inca un aspect important este modul in care executam <em>docker exec</em>. In mod normal adaugam "-it" la docker exec (interactiv + alocare de tty), insa aici nu este cazul. Alocarea de tty nu este posibila si nici interactivitatea, motiv pentru care executam simplu: <b>docker exec</b>

<pre>
[Unit]
Description=Php-Fpm 7.2 Docker Container
Requires=docker.service
After=docker.service
 
[Service]
Restart=always
ExecStart=/usr/bin/bash -c \
        '/usr/bin/docker run -h="domain.com" \
        -u="www-data" -p 9000:9000 \
        -w "/var/www/domain.com/html" \
        -v /var/www:/var/www \
        -v /etc/phpconfig/php72/php.ini:/usr/local/etc/php/php.ini \
        --name domain.com \
        --log-driver=none --memory="2g" \
        php:7.2.13 >> /var/log/domain.com-phpfpm.log 2>&1'
 
ExecStartPost=/bin/bash -c '/usr/bin/sleep 1 && /usr/bin/docker exec -u root domain.com usermod -u 1000 www-data && \
        /usr/bin/docker exec -u root domain.com usermod -G 100 www-data && \
        /usr/bin/docker exec domain.com rm -rf /var/www/domain.com/html/var/composer_home && ln -snf /var/www/.composer /var/www/domain.com/html/var/composer_home'
 
ExecStopPost=/usr/bin/docker rm -f domain.com
 
[Install]
WantedBy=default.target
</pre>

**Pont pentru fisier systemd:**

Daca folositi ca si prefix "-" pentru binar, un exit code care in mod normal este considerat ca fiind eroare (non-zero), va fi tratat ca si succes.

Acest lucru este util pentru debug, in scenariul de fata containerul va ramane pornit chiar daca la ExecStartPost avem definita a comanda care a intors un raspuns diferit de zero.


De exemplu:
<pre>
ExecStartPost=-/usr/bin/sleep 1
</pre>
