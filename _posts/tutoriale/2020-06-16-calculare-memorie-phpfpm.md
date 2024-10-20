---
title: Calculare memorie procese php-fpm
author: linuxtm
layout: post
permalink: /calculator-proces-phpfpm/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - calculator phpfpm
  - phpfpm max child calculator
  - calculeaza memorie php
  - calculator memorie fpm
  - memorie proces php
---

Daca te grabesti si nu te intereseaza cum se calculeaza, poti sa folosesti calculatorul de aici: <a href="https://linuxtm.ro/pmc/">https://linuxtm.ro/pmc/</a>

Formula dupa care calculam este urmatoarea:

```bash
[Total RAM Disponibil] - [RAM Rezervat] - [10% buffer] = [RAM disponibil pentru PHP]
```

Rezultatul:
```bash
[RAM disponibil pentru PHP] / [Dimensiunea Medie a unui Proces] = [max_children]
```

```bash
pm.max_children = [max_children]
pm.start_servers = [25% din max_children]
pm.min_spare_servers = [25% din max_children]
pm.max_spare_servers = [75% din max_children]
```
