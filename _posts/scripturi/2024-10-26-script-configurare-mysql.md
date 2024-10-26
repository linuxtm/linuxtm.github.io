---
title: Script instalare si configurare MySQL 5.7
author: linuxtm
layout: post
permalink: /script-instalare-configurare-mysql57/
categories:
  - Scripturi
tags:
  - comenzi linux
  - tutoriale linux
  - scripturi linux
  - script instalare mysql
  - script configurare mysql
  - mysql initial setup script
  - mysql config script
---

Scriptul de mai jos instaleaza MySQL 5.7 si configureaza o baza de date initiala + user si parola.

```bash
#!/bin/bash
#More at https://linuxtm.ro
#Install MySQL 5.7 Community Edition and create a database
set -e

no=$(tput sgr0)
red=$(tput setaf 1)
green=$(tput setaf 2)

SETUP_DB_HOST=127.0.0.1
SETUP_DB_NAME=my-user
SETUP_DB_USER=pass

#CHECK FOR MYSQL
if ! [ -x "$(command -v mysqld)" ]; then
  echo "Installing MySQL 5.7 community..."
  yum localinstall -y https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
  #rm -f mysql57-community-release-el7-11.noarch.rpm
  yum install -y mysql-community-server
  echo "${green}Enabling MySQL...${no}"
  systemctl enable mysqld
  echo "${green}Starting MySQL...${no}"
  systemctl start mysqld && sleep 1
else
  echo "${green}MySQL already installed${no}, skipping..."
fi

function generatePass {
choose() { echo ${1:RANDOM%${#1}:1} $RANDOM; }
{
    choose '!@#$&'
    choose '0123456789'
    choose 'abcdefghijklmnopqrstuvwxyz'
    choose 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in $( seq 1 $(( 8 + RANDOM % 8 )) )
    do
        choose '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    done

} | sort -R | fold -w 15 | awk '{printf "%s",$1}'
echo ""
}


function setupDatabase {
  MYSQL_ROOT_PASS=$(generatePass)
  SETUP_DB_PASSWORD=$(generatePass)
  TEMPROOTDBPASS="`grep 'temporary.*root@localhost' /var/log/mysqld.log | tail -n 1 | sed 's/.*root@localhost: //'`"

  echo -e "Temporary password: $TEMPROOTDBPASS"
  echo -e "Rootpass: $MYSQL_ROOT_PASS"
  if [ -z "$TEMPROOTDBPASS" ]; then
    echo "Unable to get temporary MySQL file from log. Goodbye !"
    exit 1
  fi

  mysql -u root --password="$TEMPROOTDBPASS" --connect-expired-password <<-EOSQL
     ALTER USER 'root'@'localhost' IDENTIFIED BY '${MYSQL_ROOT_PASS}';
     FLUSH PRIVILEGES;
     DELETE FROM mysql.user WHERE User='';
     DROP DATABASE IF EXISTS test;
     DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
     DELETE FROM mysql.user where user != 'mysql.sys';
     CREATE DATABASE ${SETUP_DB_NAME};
     CREATE USER ${SETUP_DB_USER}@localhost IDENTIFIED BY '${SETUP_DB_PASSWORD}';
     GRANT ALL PRIVILEGES ON ${SETUP_DB_NAME}.* TO '${SETUP_DB_USER}'@'localhost';
EOSQL

  #GENERATE ~/root/.my.cnf file
  cat <<EOF > /root/.my.cnf
[client]
user=root
password="$MYSQL_ROOT_PASS"

[mysql]
user=root
password="$MYSQL_ROOT_PASS"

[mysqldump]
user=root
password="$MYSQL_ROOT_PASS"
EOF
}

setupDatabase

echo "MySQL root pass: ${green}$MYSQL_ROOT_PASS${no}"
echo "MySQL user pass: ${green}$SETUP_DB_PASSWORD${no}"
```