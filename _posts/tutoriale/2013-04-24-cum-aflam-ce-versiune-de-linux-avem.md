---
title: Cum aflam ce versiune de Linux avem ?
author: linuxtm
layout: post
permalink: /cum-aflam-ce-versiune-de-linux-avem/
categories:
  - Tutoriale
tags:
  - comanda afisare versiune linux
  - comenzi linux
  - cum aflam ce versiune de linux avem
  - cum aflu ce distributie de linux am
  - cum aflu ce versiune de linux am
  - cum aflu versiunea linux
  - tutoriale linux
---
Pentru a afla ce versiune (distributie) de Linux folosim, rulam urmatoarea comanda:

<pre>cat /etc/*release</pre>

Comanda *lsb_release*  
Aceasta comanda afiseaza anumite LSB-uri (Linux Standard Base) si informatii legate strict de distributia pe care o folosim. Se ruleaza urmatoarea comanda:

<pre>lsb_release -a</pre>

Cum aflam ce versiune de kernel folosim ?  
Rulam urmatoarea comanda:

<pre>uname -a</pre>

sau

<pre>uname -mrs</pre>

Pentru informatii legate de kernel si GCC (GNU Compiler Collection), rulam:

<pre>cat /proc/version</pre>