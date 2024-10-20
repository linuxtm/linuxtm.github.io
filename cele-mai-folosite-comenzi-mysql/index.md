---
title: MySQL 
author: linuxtm
layout: page
tags:
  - comenzi mysql
  - grant user parola mysql
  - recuperare parola root mysql
  - mysql restore din backup
  - mysql backup
  - administrare mysql
---

**Comenzi uzuale MySQL**

```sql
CREATE DATABASE dbname;
```
```sql
GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';
```
```sql
CREATE USER 'user'@'localhost' IDENTIFIED BY 'somepass';
```
```sql
GRANT ALL PRIVILEGES ON dbname.* TO 'user'@'localhost';
```
```sql
GRANT ALL PRIVILEGES ON `dbname`.* TO 'user'@'127.2.1.%';
```
```sql
UPDATE mysql.user SET PASSWORD=PASSWORD('somepass') WHERE USER='user';
```
```sql
SELECT user, host FROM mysql.user;
```
```sql
SELECT * FROM `table` ORDER BY id DESC LIMIT 10;
```
```sql
DELETE FROM mysql.user WHERE USER='user' AND HOST='localhost';
```


**MySQLdump**
```bash
mysqldump -u root -p dbname > dbname.sql
```

```bash
mysqldump --single-transaction -u root dbname > dbname.sql #recomandat pentru baze de date mari
```

```bash
mysqldump --routines --triggers --events -u root dbname > dbname.sql #blocheaza temporar scrierile in db
```

Dump + compresie:
```bash
mysqldump -u root -p dbname > dbname.sql |gzip > dbname.sql.gz
```

Dump doar la schema:
```bash
mysqldump -u root -p --no-data dbname > dbname.sql
```

Dump doar anumite tabele:
```bash
mysqldump -u root -p dbname TABLE1 TABLE2 TABLE3 ... > dbname.sql
```

Dump fara anumite tabele:
```bash
mysqldump -u root -p dbname --ignore-table=DATABASE.TABLE --ignore-table=DATABASE.TABLE2 ... > dbname.sql
```
```bash
mysqldump -uroot -p dbname --ignore-table=dbname.users > dbname.sql  #dump fara tabela cu useri
```


**Restore o singura baza de date din dump facut cu --all-databases**
```bash
mysql -u root --force --one-database dbname < all_dbdump.sql
```

**Restore din backup**
```bash
mysqldump dbname > dbname-today.sql
```
```bash
mysql
```
```bash
drop database dbname;
```
```bash
create database dbname;
```
```bash
exit
```
```bash
cd /backup/path
```
```bash
mysql dbname &lt; dbname.create
```
```bash
mysql dbname &lt; dbname.sql
```

**Recuperare parola root**

#Pentru sisteme de operare mai vechi (CentOS 6, Ubuntu 14 sau mai vechi)
```bash
/etc/init.d/mysql stop 
```
#Pentru sisteme de operare mai noi (CentOS 7, Ubuntu 16 sau mai noi)
```bash
systemctl stop mysql / mariadb / mysqld
```
```bash
sudo mysqld_safe --skip-grant-tables &
```
```bash
mysql -u root
```
```bash
use mysql;
```

MySQL 5.6 sau mai vechi:
```sql
update user set password=PASSWORD("parolanoua") where User='root';
```

MySQL 5.7 sau mai nou:
```sql
update mysql.user set authentication_string=PASSWORD('parolanoua') where user='root';
```
```sql
flush privileges;
```
```bash
quit
```
```bash
mysqladmin -uroot -p shutdown
```
```bash
sudo /etc/init.d/mysql start
```

**Kill toate procesele unui user**
```sql
select concat('KILL ',id,';') from information_schema.processlist where user='username';
```
Sau:
```sql
select concat('KILL ',id,';') from information_schema.processlist where user='username' into outfile '/tmp/a.txt';
source /tmp/a.txt;
```

Acelasi lucru se poate face pentru un DB specific:
```sql
select concat('KILL ',id,';') from information_schema.processlist where db='dbname' into outfile '/tmp/a.txt';
source /tmp/a.txt;
```

