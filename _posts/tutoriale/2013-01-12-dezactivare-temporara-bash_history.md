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

```bash
unset HISTFILE
```

In sesiunea curenta se poate accesa history-ul fara probleme dar nu va salva pe disk (nu va scrie in fisier). Alte sesiuni nu vor fi afectate, se vor comporta normal.

Daca se doreste stergerea .bash_history, se poate face ruland:

```bash
rm ~/.bash_history
```

Nota: La urmatoarea sesiune fisierul va fi creat din nou (automat).

Variante alternative:

se deconecteaza de la sesiune fara a salva:

```bash
unset HISTFILE && exit
```

acelasi lucru, metoda diferita:

```bash
kill -9 $$
```

la fel ca si mai sus, metoda diferita:

```bash
HISTSIZE=0 && exit
```

se deconecteaza si sterge tot history-ul:

```bash
history -c && exit
```

Daca vreti ca aceste comenzi sa fie permanente, pot fi adaugate in fisierul *~/.bash_logout* sau pot fi folosite cu aliasuri.  
Pentru detalii suplimentare vezi comanda history [aici.][1]

 [1]: http://linuxtm.ro/history/