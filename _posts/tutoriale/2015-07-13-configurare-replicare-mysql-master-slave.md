---
title: 'Configurare replicare MySQL Master-Slave'
author: linuxtm
layout: post
permalink: /replicare-mysql-master-slave/
categories:
  - Tutoriale
tags:
  - replicare mysql
  - configurare replicare mysql
  - replicare master-slave
  - master-slave mysql
  - tutoriale linux

---

Avem doua servere diferite si vrem sa configuram replicarea MySQL de tip Master-Slave.  
Pentru acest exemplu vom folosi:  
Server 1: 127.0.0.1 - il vom folosi ca si Master (serverul principal)  
Server 2: 127.0.0.2 - Slave (serverul secundar)  	

Inainte de a continua, asigurati-va ca aveti instalat mysql si mysql-server:  
CentOS/RHEL: *yum install -y mysql mysql-client*  
Debian/Ubuntu: *sudo apt-get install -y mysql mysql-client*   
  
**CONFIGURARE MASTER**  
Incepem cu adaugarea urmatoarelor linii in */etc/my.cnf*   
**Important: Aveti grija ca liniile introduse in config sa fie sub [mysql] sau [mysqld], si nu sub [mysql_safe]**

```conf
#Replication
log-bin = /var/lib/mysql/mysql-bin
server-id = 1
sync-binlog = 1
binlog-format = mixed
relay-log = mysqld-relay-bin
```

In prima faza creem baza de date si importam din backup daca e cazul:
```sql
CREATE DATABASE linuxtmdb;
```

Daca e cazul, importam baza de date ruland:
```bash
mysql -u root linuxtmdb < linuxtmdb.sql
```

Facem utilizatorul pe care il vom utiliza la replicare si actualizam:
```sql
GRANT REPLICATION SLAVE ON *.* TO 'replication'@'127.0.0.2' IDENTIFIED BY 'parola';
```

```sql
FLUSH PRIVILEGES;
```

Selectam baza de date si o blocam:
```sql
USE linuxtmdb;
FLUSH TABLES WITH READ LOCK;
```

Verificam statusul master-ului (ne va folosi mai incolo):
```sql
SHOW MASTER STATUS;
```
Facem dump la baza de date (aveti grija sa iesiti din mysql (exit sau Ctrl+C) si apoi rulati comanda de mai jos):
```bash
mysqldump -u root --opt linuxtmdb > iulianwp.sql
```

Intram inapoi in MySQL si deblocam baza de date:
```sql
USE linuxtmdb;
UNLOCK TABLES;
```
Acum configurarea master-ului este completa. In continuare ne mutam pe celalalt server si configuram slave-ul.   

**CONFIGURARE SLAVE**   

Verificam in */etc/my.cnf* sa avem optiunea **server-id = 2** (diferita de 0 care e default sau 1 care e masterul).  
In prima faza facem baza de date:
```sql
CREATE DATABASE linuxtmdb;
```

Iesim din MySQL si importam baza de date (la care am facut dump pe serverul principal):

```bash
mysql -u root linuxtmdb < linuxtmdb.sql
```

Acum trebuie sa definim master-ul, astfel incat MySQL sa stie unde sa se conecteze pentru a face replicarea. Aici ne este de folos informatia afisata de *SHOW MASTER STATUS;* de mai devreme - inlocuim valorile de la *MASTER_LOG_FILE* si *MASTER_LOG_POS* cu cele afisate.

```sql
CHANGE MASTER TO MASTER_HOST='IP',MASTER_USER='replication', MASTER_PASSWORD='pass', MASTER_LOG_FILE='mysql-bin.000003', MASTER_LOG_POS= 289399;
```

Pornim slave-ul si verificam daca totul este in regula:
```sql
start slave;
show slave status \G;
```
Daca totul a decurs normal, nu veti vedea nici o eroare si acum orice modificari in baza de date pe serverul principal (Master) vor fi imediat vizibile si pe Slave.


