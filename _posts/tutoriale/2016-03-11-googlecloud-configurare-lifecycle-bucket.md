---
title: Configurare lifecycle pentru bucket-uri GoogleCloud
author: linuxtm
layout: post
permalink: /googlecloud-configurare-lifecycle-bucket/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - google cloud bucket lifecycle
  - configurare lifecycle
  - configurare bucket google cloud
  - sterge fisiere vechi google cloud bucket
---

Pentru a seta un lifecycle la bucketurile din Google Cloud, avem nevoie de un fisier json.

Mai jos avem un exemplu de fisier lifecycle-daily.json care sterge fisierele mai vechi de 7 zile
```json
{
"lifecycle": {
"rule":
  [
    {
      "action": {"type": "Delete"},
      "condition": {"age": 7}
    }
  ]
}
```

Dupa ce am creat fisierul, rulam comanda:
```bash
gsutil lifecycle set lifecycle-daily.json gs://bdaily
```
