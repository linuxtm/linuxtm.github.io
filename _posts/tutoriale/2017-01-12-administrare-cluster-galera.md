---
title: Administrare cluster Percona + Galera
author: linuxtm
layout: post
permalink: /administrare-cluster-galera/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - mysql cluster percona
  - mysql cluster galera
  - administrare cluster mysql
  - dimensiune fisier cache galera
---

Mai jos gasiti niste comenzi utile pentru administrarea unui cluster Galera.

**Verificare status cluster**
```sql
SHOW status LIKE 'wsrep%';
```

**Verificare optiuni configurare galera**
```sql
SHOW VARIABLES LIKE 'wsrep_provider_options'\G
```

**Determinare dimensiune cache file**

Comanda de mai jos va rula timp de 1 minut, timp in care va inregistra cantitatea de scrieri in db per minut. Astfel se poate determina o dimensiune corespunzatoare a fisierului de cache raportata la perioada de downtimne a unui nod.
```sql
set @start := (select sum(VARIABLE_VALUE/1024/1024) from information_schema.global_status where VARIABLE_NAME like 'WSREP%bytes'); do sleep(60); set @end := (select sum(VARIABLE_VALUE/1024/1024) from information_schema.global_status where VARIABLE_NAME like 'WSREP%bytes'); set @gcache := (select SUBSTRING_INDEX(SUBSTRING_INDEX(@@GLOBAL.wsrep_provider_options,'gcache.size = ',-1), 'M', 1)); select round((@end - @start),2) as `MB/min`, round((@end - @start),2) * 60 as `MB/hour`, @gcache as `gcache Size(MB)`, round(@gcache/round((@end - @start),2),2) as `Time to full(minutes)`;
```
