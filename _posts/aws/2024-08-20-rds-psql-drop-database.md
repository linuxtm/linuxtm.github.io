---
title: AWS RDS drop psql
author: linuxtm
layout: post
permalink: /aws-rds-psql-drop-database/
categories:
  - AWS
tags:
  - comenzi linux
  - tutoriale aws
  - aws cli drop rds psql database
  - aws export dns zone cli
  - drop psql rds
  - comenzi utile aws cli
  - aws linie comanda
  - tutoriale aws cli
  - tutoriale aws cloud
---

Putem face drop unei baze de date psql din RDS dupa cum urmeaza:

1. Conectare la RDS - important - ne conectam la alt db decat cel pe care vrem sa-l stergem.

<pre>psql -h my-db.rds.amazonaws.com -U user posgres</pre>

2. Inchide conexiunile active:

<pre>SELECT pg_terminate_backend(pg_stat_activity.pid)

FROM pg_stat_activity

WHERE pg_stat_activity.datname = 'my_database'

  AND pid <> pg_backend_pid();</pre>

3. Drop db

<pre>drop database my_database</pre> 
