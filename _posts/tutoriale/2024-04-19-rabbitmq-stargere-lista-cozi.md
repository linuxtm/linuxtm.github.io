---
title: Stergere o lista de cozi din RabbitMQ (CLI)
author: linuxtm
layout: post
permalink: /rabbitmq-stergere-lista-cozi/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - comenzi rabbitmq
  - stergere lista cozi rabbitmq
  - delete rabbitmq queues list
---

Presupunem ca avem o lista de cozi in rabbit pe care vrem sa le stergem. 

Daca avem multe, stergerea manuala nu este o optiune.

In acest sens, lista de cozi o punem intr-un fisier text, si iteram prin fiecare linie cu ajutorul unui for.

```bash
for i in `cat cozi.txt`; do curl -k -i -XDELETE https://admin:pass@rabbitmq.mysite.com/api/queues/$i; done
````

Exemplu fisier cozi.txt:

<em>coada1

coada2</em>

In esenta fiecare coada trebuie sa fie pe o linie noua in fisierul txt.


Alternativ putem folosi comenzile de mai jos pentru a sterge cate o coada sau pentru a exporta lista de cozi intr-un fisier txt.

```bash
rabbitmqctl delete_queue queue1
```

```bash
rabbitmqadmin delete queue name=queue1
```

```bash
rabbitmqctl list_queues name > list1.txt
```
