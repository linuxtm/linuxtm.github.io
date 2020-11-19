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

<pre>CREATE DATABASE dbname;</pre>
<pre>GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';</pre>
<pre>CREATE USER 'user'@'localhost' IDENTIFIED BY 'somepass'; </pre>
<pre>GRANT ALL PRIVILEGES ON dbname.* TO 'user'@'localhost';</pre>
<pre>GRANT ALL PRIVILEGES ON `dbname`.* TO 'user'@'127.2.1.%';</pre>
<pre>UPDATE mysql.user SET PASSWORD=PASSWORD('somepass') WHERE USER='user';</pre>
<pre>SELECT user, host FROM mysql.user;</pre>
<pre>SELECT * FROM `table` ORDER BY id DESC LIMIT 10;</pre>
<pre>DELETE FROM mysql.user WHERE USER='user' AND HOST='localhost';</pre>


**MySQLdump**
<pre>mysqldump -u root -p dbname > dbname.sql</pre>
<pre>mysqldump --routines --triggers --events -u root dbname > dbname.sql #blocheaza scrierile in db temporar</pre>

Dump doar la schema:
<pre>mysqldump -u root -p --no-data dbname > dbname.sql</pre>

Dump doar anumite tabele:
<pre>mysqldump -u root -p dbname TABLE1 TABLE2 TABLE3 ... > dbname.sql</pre>

Dump fara anumite tabele:
<pre>mysqldump -u root -p dbname --ignore-table=DATABASE.TABLE --ignore-table=DATABASE.TABLE2 ... > dbname.sql</pre>
<pre>mysqldump -uroot -p dbname --ignore-table=dbname.users > dbname.sql  #dump fara tabela cu useri</pre>


**Restore o singura baza de date din dump facut cu --all-databases**
<pre>
mysql -u root --force --one-database dbname < all_dbdump.sql
</pre>

**Restore din backup**
<pre>
mysqldump dbname > dbname-today.sql
</pre>
<pre>
mysql
</pre>
<pre>
drop database dbname;
</pre>
<pre>
create database dbname;
</pre>
<pre>
exit
</pre>
<pre>
cd /backup/path
</pre>
<pre>
mysql dbname &lt; dbname.create
</pre>
<pre>
mysql dbname &lt; dbname.sql
</pre>

**Recuperare parola root**

#Pentru sisteme de operare mai vechi (CentOS 6, Ubuntu 14 sau mai vechi)
<pre>
/etc/init.d/mysql stop 
</pre>
#Pentru sisteme de operare mai noi (CentOS 7, Ubuntu 16 sau mai noi)
<pre>
systemctl stop mysql / mariadb / mysqld
</pre>
<pre>
sudo mysqld_safe --skip-grant-tables &
</pre>
<pre>
mysql -u root
</pre>
<pre>
use mysql;
</pre>

MySQL 5.6 sau mai vechi:
<pre>
update user set password=PASSWORD("parolanoua") where User='root';
</pre>

MySQL 5.7 sau mai nou:
<pre>
update mysql.user set authentication_string=PASSWORD('parolanoua') where user='root';
</pre>

<pre>
flush privileges;
</pre>
<pre>
quit
</pre>
<pre>
mysqladmin -uroot -p shutdown
</pre>
<pre>
sudo /etc/init.d/mysql start
</pre>

**Kill toate procesele unui user**
<pre>select concat('KILL ',id,';') from information_schema.processlist where user='username';</pre>
Sau:
<pre>
select concat('KILL ',id,';') from information_schema.processlist where user='username' into outfile '/tmp/a.txt';
source /tmp/a.txt;
</pre>

Acelasi lucru se poate face pentru un DB specific:
<pre>
select concat('KILL ',id,';') from information_schema.processlist where db='dbname' into outfile '/tmp/a.txt';
source /tmp/a.txt;
</pre>
