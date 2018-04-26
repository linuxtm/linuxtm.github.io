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

***Comenzi uzuale MySQL*** 

<pre>CREATE DATABASE dbname;</pre>
<pre>GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';</pre>
<pre>CREATE USER 'user'@'localhost' IDENTIFIED BY 'somepass'; </pre>
<pre>GRANT ALL PRIVILEGES ON dbname.* TO 'user'@'localhost';</pre>
<pre>GRANT ALL PRIVILEGES ON `dbname`.* TO 'user'@'127.2.1.%';</pre>
<pre>UPDATE mysql.user SET PASSWORD=PASSWORD('somepass') WHERE USER='user';</pre>
<pre>SELECT user, host FROM mysql.user;</pre>
<pre>DROP user 'user'@'host';</pre>
<pre>SELECT * FROM `table` ORDER BY id DESC LIMIT 10;</pre>
<pre>DELETE FROM mysql.user WHERE USER='user' AND HOST='localhost';</pre>
<pre>mysqldump -u root -p dbname > dbname.sql</pre>
<pre>mysqldump --routines --triggers --events -u root dbname > dbname.sql</pre>
<pre>mysql -u root -p dbname < dbname.sql</pre>

***Replication dump***
<pre>mysqldump --master-data --single-transaction -A > alldbs.sql --routines --triggers --events</pre>

***Restore din backup***
<pre>
mysqldump dbname > dbname-today.sql
mysql
drop database dbname;
create database dbname;
exit
cd /backup/path
mysql dbname &lt; dbname.create 
mysql dbname &lt; dbname.sql
</pre>

***Recuperare parola root***
<pre>
sudo /etc/init.d/mysql stop
sudo mysqld_safe --skip-grant-tables &
mysql -u root
use mysql;
update user set password=PASSWORD("parolanoua") where User='root';
flush privileges;
quit
mysqladmin -uroot -p shutdown
sudo /etc/init.d/mysql start
</pre>

***Kill toate procesele unui user***
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
