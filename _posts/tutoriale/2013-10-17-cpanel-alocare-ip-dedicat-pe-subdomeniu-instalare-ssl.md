---
title: 'cPanel: Alocare IP dedicat pe subdomeniu + Instalare SSL'
author: linuxtm
layout: post
permalink: /cpanel-alocare-ip-dedicat-pe-subdomeniu-instalare-ssl/
categories:
  - Tutoriale
tags:
  - Alocare IP dedicat pe subdomeniu
  - cpanel instalare ssl pe subdomeniu
  - cpanel ip dedicat
  - instalare ssl pe subdomeniu
  - instalare ssl pe subdomeniu cpanel
  - ip dedicat pentru subdomeniu cpanel
  - ip dedicat subdomeniu
  - ip dedicat subdomeniu cpanel
---
Chiar daca interfata WHM nu permite alocarea unui IP dedicat subdomeniilor, se poate face. Motivul principal pentru care s-ar putea sa vreti sa alocati un IP dedicat unui subdomeniu este instalarea unui certificat SSL.

Pentru exemplul de fata vom folosi:

Domeniu/Subdomeniu Adresa IP  
exemplu.ro 192.168.0.1  
sub.exemplu.ro 192.168.0.2

Pentru a continua, este nevoie de access SSH.  
Adaugarea se face usor prin ediatarea fisierului aferent subdomeniului respectiv.

1. Intram in directorul **userdata**

<pre>cd /var/cpanel/userdata</pre>

2. Localizam utilizatorul si navigam in directorul respectiv:

<pre>cd exemplu</pre>

3. In interiorul directorului gasim urmatoarele fisiere:

<pre>exemplu.ro
exemplu.ro.cache
sub.exemplu.ro
sub.exemplu.ro.cache
etc, etc</pre>

4. Folosind editorul preferat (vi, vim, nano), editam ce ne intereseaza, adica fisierul pentru subdomeniu, in cazul de fata sub.exemplu.ro  
5. In dreptul campului &#8220;ip&#8221;, inlocuim cu ip-ul ce ne intereseaza, dupa care salvam fisierul.

<pre>ip: 192.168.0.2</pre>

6. Dupa ce am salvat, facem rebuild la Apache, apoi restartam Apache-u:

<pre>/usr/local/cpanel/scripts/rebuildhttpdconf
/usr/local/cpanel/scripts/restartsrv_apache
</pre>

7. Intram in WHM si editam zona DNS pentru domeniul exemplu.ro, si inlocuim ip-ul in toate campurile care contin subdomeniul , salvam.  
8. Ne asiguram ca IP-ul va ramane dedicat subdomeniului respectiv urmand pasii de mai jos:

*Home >> IP Functions >> Show/Edit Reserved IPs*  
Bifam in dreptul IP-ului casuta si specificam cui a fost alocat, in cazul de fata: sub.exemplu.ro

Instalare certificat SSL  
Se urmeaza pasii normali: din WHM se acceseaza &#8220;Install an SSL Certificate on a Domain&#8221; unde se completeaza cu numele subdomeniului si adresa IP corecta.  
Daca WHM nu gaseste automat certificatul (crt) acesta se cere de la clienti.