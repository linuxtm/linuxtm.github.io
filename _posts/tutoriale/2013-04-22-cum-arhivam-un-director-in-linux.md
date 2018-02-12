---
title: Cum arhivam un director in Linux ?
author: linuxtm
layout: post
permalink: /cum-arhivam-un-director-in-linux/
categories:
  - Tutoriale
tags:
  - arhiva linux
  - arhivare fisiere linux
  - arhiva linux data de azi
  - arhiva linux data curenta
  - arhivare folder linux
  - comenzi linux
  - cum arhivam un director in linux
  - cum dezarhivam un director in linux
  - gzip linux
  - tar -zcvf
  - tar -zxvf
  - tar linux
  - tutoriale linux
---
Este destul de usor si folositor pentru a face backup unor fisiere, pentru a le trimite pe mail si asa mai departe.  
Pentru a arhiva un director, trebuie sa folosim comanda *tar* cu sintaxa de mai jos:

<pre>tar -zcvf nume-arhiva.tar.gz nume-director</pre>

Unde:  
-z: Compreseaza arhiva folosind gzip  
-c: Creaza arhiva  
-v: Detaliat (afiseaza progresul in timp ce creaza arhiva)  
-f: Numele arhivei

De exemplu, avem un director numit /home/linuxtm/documente si vrem sa il arhivam. Rulam comanda de mai jos:

<pre>tar -zcvf documente.tar.gz /home/linuxtm/documente</pre>

Comanda de mai sus va crea o arhiva numita *documente.tar.gz* in directorul curent. 

De asemenea, putem crea o arhiva care sa includa in nume data de astazi:
<pre> tar cfz backup-$(date +%Y-%m-%d).tar.gz test/ </pre>
Comanda de mai sus va arhiva directorul *test* intr-o arhiva numita numita *backup-* +data de azi (in cazul de fata: backup-2013-04-22.tar.gz)

Daca vrem sa facem restore din arhiva (va dezarhiva in directorul curent), folosim urmatoarea comanda:

<pre>tar -zxvf documente.tar.gz</pre>

Unde:  
-x: Extrage fisierele

Daca dorim sa dezarhivam intr-un alt director, de exemplu in /root rulam comanda:

<pre>tar -zxvf documente.tar.gz -C /root</pre>
