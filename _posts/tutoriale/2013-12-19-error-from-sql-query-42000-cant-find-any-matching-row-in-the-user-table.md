---
title: 'Error from sql query: #42000: Can’t find any matching row in the user table'
author: linuxtm
layout: post
permalink: /error-from-sql-query-42000-cant-find-any-matching-row-in-the-user-table/
categories:
  - Tutoriale
tags:
  - Can’t find any matching row in the user table
  - 'eroare #42000: Can’t find any matching row in the user table'
  - 'Error from sql query: #42000'
---
Eroarea poate sa apara fie in loguri, fie in cPanel/WHM cand incercati sa accesati phpMyAdmin, sau cand incercati sa creati un user sau o baza de date noua in cPanel. Eroarea se poate rezolva prin eliminarea liniei urmatoare din ***/etc/my.cnf*** :

<pre>skip-name-resolve</pre>

Daca nu se rezolva, adaugati urmatoarea linie:

<pre>skip-networking</pre>
