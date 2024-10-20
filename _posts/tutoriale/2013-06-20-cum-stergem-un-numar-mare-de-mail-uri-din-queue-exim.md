---
title: Cum stergem un numar mare de mail-uri din queue (exim) ?
author: linuxtm
layout: post
permalink: /cum-stergem-un-numar-mare-de-mail-uri-din-queue-exim/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - stergere mailuri exim
  - stergere multe mailuri din exim
  - stergere numar mare de mailuri
  - tutorial exim
  - tutoriale linux
---
In cazul in care vorbim de zeci, sute de mii de mail-uri (sau mai multe), metodele traditionale pentru curatarea mesajelor din queue tind sa nu functioneze tocmai bine. Fie ca vorbim de I/O mare, o durata de timp exagerat de mare pentru stergerea mesajelor sau afisarea inutila a progresului (afisearea fiecarui MessageID sters), este cel putin nepractic. Comenzile de mai jos rezolva aceasta problema:

```bash
for dir in /var/spool/exim/input/*; do cd $dir; ls | xargs rm -f; done
```

sau

```bash
find /var/spool/exim/input -type f -exec rm -f {} +
```

In cazul in care aveti mai putine mailuri, variantele traditionale sunt:

```bash
exim -bp | awk '/^ *[0-9]+[mhd]/{print "exim -Mrm " $3}' | bash
```

```bash
exim -bp | exiqgrep -i | xargs exim -Mrm
```