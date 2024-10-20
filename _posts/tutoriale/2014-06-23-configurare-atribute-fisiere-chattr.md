---
title: Configurare atribute fisiere (chattr)
author: linuxtm
layout: post
permalink: /configurare-atribute-fisiere-chattr/
categories:
  - Tutoriale
tags:
  - atribute fisiere linux
  - chattr
  - fisier immutable linux
  - fisier imuabil
  - fisier imutabil linux
  - nu pot sterge fisier linux
  - prevenire stergere fisier linux
---
Comanda folosita este *chattr* , iar cu ajutorul acesteia putem sa adauga/scoate atributele fisierelor in Linux. Folosind chattr, putem face in fisier imuabil (neschimbator). Un fisier cu un astfel de atribut nu poate fi sters nici macar de root.

Pentru a face un fisier imuabil, rulam comanda:

```bash
chattr +i fisier
```

Nota: acest atribut ( +i ), poate fi dat doar de catre root, deci fie aveti acces root fie trebuie exacutata comanda cu sudo.

Daca vrem sa scoatem atributul fisierului, rulam:

```bash
chattr -i fisier
```

In Linux, fiecare fisier are un numar de atribute asociate, atributul imuabil (immutable) fiind doar unul dintre ele. Pentru a vedea toate atributele unui fisier, rulam comanda:

```bash
lsattr fisier
```

Pentru mai multe informatii referitor la folosirea atributelor verificati pagina de ajutor a comenzii (man chattr).