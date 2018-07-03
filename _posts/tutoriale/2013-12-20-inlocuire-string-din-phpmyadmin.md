---
title: Inlocuire string din phpmyadmin
author: linuxtm
layout: post
permalink: /inlocuire-string-din-phpmyadmin/
categories:
  - Tutoriale
tags:
  - inlocuire cuvant in phpmyadmin
  - Inlocuire string din phpmyadmin
  - inlocurie cuvinte in phpmyadmin
---
Presupunem ca avem un site facut in wordpress si vrem sa inlocuim in baza de date un sir de cuvinte (numele autorului de exemplu) cu un altul. Aceasta operatiune se poate realiza cu comanda urmatoare:

<pre>UPDATE `wp_posts` SET post_content = replace(post_content, 'cuvant_nedorit', 'cuvant_dorit') </pre>

Nota: &#8220;wp-posts&#8221; este tabela din baza de date.