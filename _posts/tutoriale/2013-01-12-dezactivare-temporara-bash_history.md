---
title: Dezactivare temporara .bash_history
author: linuxtm
layout: post
permalink: /dezactivare-temporara-bash_history/
wpsd_autopost:
  - 1
categories:
  - Tutoriale
tags:
  - comenzi linux
  - cum dezactivez bash_history
  - cum dezactivez history linux
  - cum sterg bash_history
  - cum sterg history linux
  - dezactivare history linux
  - dezactivare temporara bash_history
  - dezactivare temporara history
  - dezactivare temporara history linux
  - stergere history la logout
  - tutoriale linux
---
Sa zicem ca aveti de introdus niste parole in linia de comanda ca si argument la ceva. Nu e tocmai cea mai buna idee sa ramana salvate in ~/.bash_history dar nici nu dorim sa stergem fisierul.  
In acest caz, dezactivam temporar (pentru sesiunea curenta) history-ul. Se poate face ruland comanda:

<pre>unset HISTFILE</pre>

In sesiunea curenta se poate accesa history-ul fara probleme dar nu va salva pe disk (nu va scrie in fisier). Alte sesiuni nu vor fi afectate, se vor comporta normal.

Daca se doreste stergerea .bash_history, se poate face ruland:

<pre>rm ~/.bash_history</pre>

Nota: La urmatoarea sesiune fisierul va fi creat din nou (automat).

Variante alternative:

&#8211; se deconecteaza de la sesiune fara a salva:

<pre>unset HISTFILE && exit</pre>

&#8211; acelasi lucru, metoda diferita:

<pre>kill -9 $$</pre>

&#8211; la fel ca si mai sus, metoda diferita:

<pre>HISTSIZE=0 && exit</pre>

&#8211; se deconecteaza si sterge tot history-ul:

<pre>history -c && exit</pre>

Daca vreti ca aceste comenzi sa fie permanente, pot fi adaugate in fisierul *~/.bash_logout* sau pot fi folosite cu aliasuri.  
Pentru detalii suplimentare vezi comanda history [aici.][1]

 [1]: http://linuxtm.ro/history/