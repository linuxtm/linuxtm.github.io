---
title: Eroare Drupal + Nginx - sites/default/files not writable
author: linuxtm
layout: post
permalink: /drupal-nginx-sites-not-writable/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - sites/default/files not writable
  - drupal files not writable
  - tutoriale linux
---

Daca folositi ca si setup Nginx+PHP-FPM, atunci e foarte probabil sa intampinati eroarea intr-o instalare de Drupal.
Rezolvarea este una simpla, trebuie sa modificam userul sub care ruleaza php-fpm astfel incat sa corespunda cu userul si grupul nginx.

```bash
vim /etc/php-fpm.d/www.conf
```

Astfel, in config vom avea:

```conf
user = nginx
group = nginx
```
