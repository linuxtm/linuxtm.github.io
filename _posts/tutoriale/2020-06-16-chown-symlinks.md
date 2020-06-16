---
title: Chown recursiv in symlinkuri
author: linuxtm
layout: post
permalink: /chown-symlinks/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - chown recursiv symlinkuri
  - chown recursive symlinks
  - chown doesnt change permissions inside symlinks
  - change file ownership inside symlinks
  - schimbare owner fisiere chown simlinkuri
---

In mod normal daca vrem sa schimbam ownership-ul fisierelor recursiv folosim parametrul "-R" (recursiv), insa in mod implicit, chown nu traverseaza linkurile simbolice. 

Astfel, ne gasim in situatia in care desi am dat chown -R pe un director, daca acesta contine linkuri simbolice ownerul fisierelor din interiorul directorului de tip symlink, nu va fi schimbat.

In manualul chown, gasim urmatoarea optiune:

<em> -L   traverse every symbolic link to a directory encountered</em>

Astfel, daca dorim ca ownershipul fisieirelor sa fie schimbat si in interiorul directoarelor de tip symlink folosim:

<pre>chown -RL /my/dir/</pre>

Bonus, avem optiunea "-h"

<em>-h, --no-dereference   affect symbolic links instead of any referenced file (useful only on systems that can change the ownership of a symlink</em>

Aceasta optiune nu schimba drepturile sau ownership-ul fisierelor din interiorul directorului nostru symlink, insa are un rol pur estetic. Mai exact, daca dam un "ls -l" si observam directorul nostru symlink, probabil ownerul este root. Folosind aceasta optiune putem schimba ownerul aparent al symlinkului.

<pre>chown -h mysymlink</pre>
