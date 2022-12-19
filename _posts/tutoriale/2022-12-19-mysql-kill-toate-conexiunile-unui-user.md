---
title: MySQL kill toate conexiunile unui user
author: linuxtm
layout: post
permalink: /mysql-kill-toate-conexiunile-unui-user/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - comenzi mysql
  - kill mysql sessions user
  - opreste conexiunile unui user de mysql
  - kill all mysql user sessions
---

MySQL nu are o comanda cu ajutorul careia putem sa terminam toate conexiunile unui utilizator.
Din acest motiv, vom folosi functia de CONCAT pentru a combina comanda "KILL" cu ID-ul conexiuniulor utilizatorului problema, in exemplul de fata "my-user", iar lista o vom insera intr-un fisier "process_list.txt".
Dupa acest pas, importam lista si se vor executa comenzile din lista (<em>KILL PID1; KILL PID2, KILL PID3; etc</em>).


**Atentie ! Comenzile de mai jos vor inchide conexiuni ! Asigurati-va ca ati definit utilizatorul corect !**

<pre>SELECT CONCAT('KILL ',id,';') FROM information_schema.processlist WHERE user='my-user' INTO OUTFILE '/var/lib/mysql-files/process_list.txt';</pre>
<pre>source /var/lib/mysql-files/process_list.txt</pre>
<pre>exit</pre>

Dupa ce am rulat comanda, trebuie sa stergem fisierul, in caz contrar, data viitoare cand vrem sa rulam aceiasi comanda vom primi o eroare cum ca fisierul deja exista.
<pre>rm -rf /var/lib/mysql-files/process_list.txt</pre>
