---
title: Script instalare Magento2 + dependinte
author: linuxtm
layout: post
permalink: /script-instalare-automata-magento2-si-dependinte/
categories:
  - Scripturi
tags:
  - comenzi linux
  - tutoriale linux
  - scripturi linux
  - script instalare magento
  - script magento dependinte
  - magento2 install script
  - instalare automata magento2 dependinte
  - script dependinte magentgo2
  - script instalare magento2
---

Scriptul de mai jos este testat si functioneaza pe CentOS7, poate fi modificat sa functioneze cu versiuni mai noi sau chiar si cu alte distributii. 
Face urmatoarele:
- dezactiveaza selinux
- instaleaza dependintele necesare (nginx, php, redis, mysql) 
- instaleaza Magento2 
- configureaza MySQL (user/pass/db) 
- configureaza un vhost in Nginx pentru Magento

```bash
#!/bin/bash
set -e

no=$(tput sgr0)
red=$(tput setaf 1)
green=$(tput setaf 2)
DISTRO=$(awk -F= '/^NAME/{print $2}' /etc/os-release)

#Check Linux distribution, must be CentOS
if [[ $DISTRO != *CentOS* ]]; then
  echo "This script only works on Centos 7. Goodbye !"
  exit 1
fi

#Check for SELinux...duh !
if sestatus | grep -q enabled ;then
        echo "SELinux is on !"
        echo "Disabling SELinux..."
        setenforce 0
        sed -i -e 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
        echo "SELinux is now disabled."
else
        echo "SELinux is off, good for you !"
fi

echo "Checking prerequisites..."

#CHECK FOR PHP
if ! [ -x "$(command -v php)" ]; then
  echo "PHP ${red}not present${no} , let's install it."
  read -p "Please specify one of these versions: ${green}71${no} , ${green}72${no} or ${green}73${no} : " V
  #Force version
  if [[ $V != @(71|72|73) ]] ; then
    echo "Plese write one of the green values: ${green}71${no} / ${green}72${no} / ${green}73${no}"
    exit 1
  fi

  yum localinstall -y https://centos7.iuscommunity.org/ius-release.rpm

  #If php 7.1, enable IUS Archive
  if [ $V == 71 ] ; then
    yum-config-manager enable ius-archive
  fi

  #If php 7.3, remove "u" from package name (duh, stupid naming convention)
  if [ $V == 73 ] ; then
    yum install -y php${V}-bcmath \
                   php${V}-cli \
                   php${V}-common \
                   php${V}-fpm \
                   php${V}-gd \
                   php${V}-intl \
                   php${V}-json \
                   php${V}-mbstring \
                   php${V}-mysqlnd \
                   php${V}-pdo \
                   php${V}-pecl-igbinary \
                   php${V}-pecl-redis \
                   php${V}-process \
                   php${V}-soap \
                   php${V}-xml
    echo "Enabling PHP-FPM to start at boot..."
    systemctl enable php-fpm
    echo "Starting PHP-FPM ..."
    systemctl start php-fpm
    exit 1
  fi

  yum install -y php${V}u-bcmath \
	         php${V}u-cli \
	         php${V}u-common \
    	         php${V}u-fpm \
	         php${V}u-gd \
	         php${V}u-intl \
	         php${V}u-json \
	         php${V}u-mbstring \
	         php${V}u-mysqlnd \
	         php${V}u-pdo \
	         php${V}u-pecl-igbinary \
	         php${V}u-pecl-redis \
	         php${V}u-process \
	         php${V}u-soap \
	         php${V}u-xml
  echo "Enabling PHP-FPM to start at boot..."
  systemctl enable php-fpm
  echo "Starting PHP-FPM ..."
  systemctl start php-fpm
else
  echo "${green}PHP already installed${no}, skipping..."
fi

#CHECK FOR COMPOSER
if ! [ -x "$(command -v composer)" ]; then
  EXPECTED_SIGNATURE="$(wget -q -O - https://composer.github.io/installer.sig)"
  php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
  ACTUAL_SIGNATURE="$(php -r "echo hash_file('sha384', 'composer-setup.php');")"

  if [ "$EXPECTED_SIGNATURE" != "$ACTUAL_SIGNATURE" ]
  then
    >&2 echo 'ERROR: Invalid installer signature'
    rm composer-setup.php
    exit 1
  fi

  php composer-setup.php --quiet
  mv composer.phar /usr/local/bin/composer
  chmod +x /usr/local/bin/composer
  rm composer-setup.php
else
  echo "${green}Composer already installed${no}, skipping..."
fi

#CHECK FOR NGINX
if ! [ -x "$(command -v nginx)" ]; then
  yum install -y nginx
  echo "${green}Enabling Nginx...${no}"
  systemctl enable nginx
  echo "${green}Starting Nginx...${no}"
  systemctl start nginx
else
  echo "${green}Nginx already installed${no}, skipping..."
fi

#CHECK FOR REDIS
if ! [ -x "$(command -v redis-server)" ]; then
  yum install -y redis
  echo "${green}Enabling Redis...${no}"
  systemctl enable redis
  echo "${green}Starting Redis...${no}"
  systemctl start redis
else
  echo "${green}Redis already installed${no}, skipping..."
fi

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


PHP_BIN=$(command -v php)
COMPOSER_BIN=$(command -v composer)
NGINX_BIN=$(command -v nginx)
REDIS_BIN=$(command -v redis-server)
MYSQL_BIN=$(command -v mysqld)

echo -e "\n"
echo "Let's configure some variables."
echo -e "${red}ATTENTION !${no} Some of the variables have a ${green}default${no} value. \nIf you like that default, just hit ${green}Enter${no}."
echo -e "\n"

#Set / ask for variables
read -p "Installation directory (default ${green}/var/www/html${no}): " M2SETUP_SITEDIR
M2SETUP_SITEDIR=${M2SETUP_SITEDIR:-/var/www/html}
#read -p "Website domain - ${red}do not include http://${no} (${red}no default${no}): " M2SETUP_DOMAIN

M2SETUP_DOMAIN=${M2SETUP_DOMAIN:-autodevops.evozon.com}
while  [ -z "$M2SETUP_DOMAIN" ]; do
  echo "Domain cannot be empty !"
  read -p "Website domain - ${red}do not include http://${no} (${red}no default${no}): " M2SETUP_DOMAIN
done

read -p "Working directory - ${red}must be 1 level higher than Installation directory${no} (default ${green}/var/www${no}): " M2SETUP_WORKDIR
M2SETUP_WORKDIR=${M2SETUP_WORKDIR:-/var/www}

read -p "repo.magento.com username (${red}no default${no}): " COMPOSER_USER
COMPOSER_USER=${COMPOSER_USER:-your-user-here} #CHANGE ME

while [ -z "$COMPOSER_USER" ]; do
  echo "Composer user cannot be empty !"
  read -p "repo.magento.com username (${red}no default${no}): " COMPOSER_USER
done

read -p "repo.magento.com password (${red}no default${no}): " COMPOSER_PASS
COMPOSER_PASS=${COMPOSER_PASS:-your-pass-here} #CHANGE ME

while [ -z "$COMPOSER_PASS" ]; do
  echo "Composer password cannot be empty !"
  read -p "repo.magento.com password (${red}no default${no}): " COMPOSER_PASS
done

read -p "Magento version (default ${green}2.3.1${no}): " M2SETUP_VERSION
M2SETUP_VERSION=${M2SETUP_VERSION:-2.3.1} #CHANGE ME
read -p "Magento Edition (community / enterprise), default ${green}community${no} : " M2SETUP_EDITION
M2SETUP_EDITION=${M2SETUP_EDITION:-community}
read -p "Sample data (true / false), default ${green}true${no} : " M2SETUP_USE_SAMPLE_DATA
M2SETUP_USE_SAMPLE_DATA=${M2SETUP_USE_SAMPLE_DATA:-true}

#SERVICES VARIABLES
read -p "PHP-FPM host (default ${green}127.0.0.1${no}): " PHP_HOST
PHP_HOST=${PHP_HOST:-127.0.0.1}
read -p "PHP-FPM port (default ${green}9000${no}): " PHP_PORT
PHP_PORT=${PHP_PORT:-9000}
read -p "Redis host (default ${green}127.0.0.1${no}): " REDIS_HOST
REDIS_HOST=${REDIS_HOST:-127.0.0.1}
read -p "Redis port (default ${green}6379${no}): " REDIS_PORT
REDIS_PORT=${REDIS_PORT:-9000}

M2SETUP_DB_HOST=127.0.0.1
M2SETUP_DB_NAME=magento
M2SETUP_DB_USER=magento
M2SETUP_BASE_URL="http://${M2SETUP_DOMAIN}"
M2SETUP_BACKEND_FRONTNAME=admin
M2SETUP_ADMIN_FIRSTNAME=Admin
M2SETUP_ADMIN_LASTNAME=User
M2SETUP_ADMIN_EMAIL=admin@email.com
M2SETUP_ADMIN_USER=admin
M2SETUP_ADMIN_PASSWORD=Admin123admin
M2SETUP_CURRENCY=USD
M2SETUP_LANGUAGE=en_US
M2SETUP_TIMEZONE=America/New_York

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
  M2SETUP_DB_PASSWORD=$(generatePass)
  TEMPROOTDBPASS="`grep 'temporary.*root@localhost' /var/log/mysqld.log | tail -n 1 | sed 's/.*root@localhost: //'`"

  echo -e "Temporary MySQL password: $TEMPROOTDBPASS"
  echo -e "MySQL Root password: $MYSQL_ROOT_PASS"
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
     CREATE DATABASE ${M2SETUP_DB_NAME};
     CREATE USER ${M2SETUP_DB_USER}@localhost IDENTIFIED BY '${M2SETUP_DB_PASSWORD}';
     GRANT ALL PRIVILEGES ON ${M2SETUP_DB_NAME}.* TO '${M2SETUP_DB_USER}'@'localhost';
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


function generateAuthJSON {
  cat <<EOF > $M2SETUP_WORKDIR/.composer/auth.json
{
    "http-basic": {
        "repo.magento.com": {
            "username": "${COMPOSER_USER}",
            "password": "${COMPOSER_PASS}"
        }
    }
}
EOF
}



function generateNginxConf {
  cat <<EOF > /etc/nginx/conf.d/$M2SETUP_DOMAIN.conf
upstream fastcgi_backend {
  server ${PHP_HOST}:${PHP_PORT};
}

server {
  listen 80;
  server_name $M2SETUP_DOMAIN;

  root $M2SETUP_SITEDIR/pub;
  set \$MAGE_MODE APP_MAGE_MODE;

  index index.php;
  autoindex off;
  charset off;

  add_header 'X-Content-Type-Options' 'nosniff';
  add_header 'X-XSS-Protection' '1; mode=block';

  location /setup {
    root $M2SETUP_SITEDIR;

    location ~ ^/setup/index.php {
      fastcgi_pass   fastcgi_backend;
      fastcgi_index  index.php;
      fastcgi_param  SCRIPT_FILENAME  \$document_root\$fastcgi_script_name;
      include    fastcgi_params;
    }

    location ~ ^/setup/(?!pub/). {
      deny all;
    }

    location ~ ^/setup/pub/ {
      add_header X-Frame-Options "SAMEORIGIN";
    }
  }

  location /update {
    root $M2SETUP_SITEDIR;

    location ~ ^/update/index.php {
      fastcgi_split_path_info ^(/update/index.php)(/.+)$;
      fastcgi_pass   fastcgi_backend;
      fastcgi_index  index.php;
      fastcgi_param  SCRIPT_FILENAME  \$document_root\$fastcgi_script_name;
      fastcgi_param  PATH_INFO    \$fastcgi_path_info;
      include    fastcgi_params;
    }

    # deny everything but index.php
    location ~ ^/update/(?!pub/). {
      deny all;
    }

    location ~ ^/update/pub/ {
      add_header X-Frame-Options "SAMEORIGIN";
    }
  }

  location / {
    try_files \$uri \$uri/ /index.php?\$args;
  }

  location /pub {
    location ~ ^/pub/media/(downloadable|customer|import|theme_customization/.*\.xml) {
      deny all;
    }

    alias $M2SETUP_SITEDIR/pub;
    add_header X-Frame-Options "SAMEORIGIN";
  }

  location /static/ {
    if (\$MAGE_MODE = "production") {
      expires max;
    }

    # remove signature of static files used to overcome browser cache
    location ~ ^/static/version {
      rewrite ^/static/(version\d*/)?(.*)$ /static/\$2 last;
    }

    location ~* \.(ico|jpg|jpeg|png|gif|svg|js|css|swf|eot|ttf|otf|woff|woff2)$ {
      add_header Cache-Control "public";
      add_header X-Frame-Options "SAMEORIGIN";
      expires +1y;

      if (!-f \$request_filename) {
        rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=\$2 last;
      }
    }

    location ~* \.(zip|gz|gzip|bz2|csv|xml)$ {
      add_header Cache-Control "no-store";
      add_header X-Frame-Options "SAMEORIGIN";
      expires off;

      if (!-f \$request_filename) {
         rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=\$2 last;
      }
    }

    if (!-f \$request_filename) {
      rewrite ^/static/(version\d*/)?(.*)$ /static.php?resource=\$2 last;
    }

    add_header X-Frame-Options "SAMEORIGIN";
  }

  location /media/ {
    try_files \$uri \$uri/ /get.php?\$args;

    location ~ ^/media/theme_customization/.*\.xml {
      deny all;
    }

    location ~* \.(ico|jpg|jpeg|png|gif|svg|js|css|swf|eot|ttf|otf|woff|woff2)$ {
      add_header Cache-Control "public";
      add_header X-Frame-Options "SAMEORIGIN";
      expires +1y;
      try_files \$uri \$uri/ /get.php?\$args;
    }

    location ~* \.(zip|gz|gzip|bz2|csv|xml)$ {
      add_header Cache-Control "no-store";
      add_header X-Frame-Options "SAMEORIGIN";
      expires off;
      try_files \$uri \$uri/ /get.php?\$args;
    }

    add_header X-Frame-Options "SAMEORIGIN";
  }

  location /media/customer/ {
    deny all;
  }

  location /media/downloadable/ {
    deny all;
  }

  location /media/import/ {
    deny all;
  }

  location ~ /media/theme_customization/.*\.xml$ {
    deny all;
  }

  location /errors/ {
    try_files \$uri =404;
  }

  location ~ ^/errors/.*\.(xml|phtml)$ {
    deny all;
  }

  location ~ (index|get|static|report|404|503)\.php$ {
    try_files \$uri =404;
    fastcgi_pass   fastcgi_backend;

    fastcgi_param  PHP_FLAG  "session.auto_start=off \n suhosin.session.cryptua=off";
    fastcgi_param  PHP_VALUE "memory_limit=3G \n max_execution_time=600";
    fastcgi_read_timeout 600s;
    fastcgi_connect_timeout 600s;
    fastcgi_param  MAGE_MODE \$MAGE_MODE;

    fastcgi_index  index.php;
    fastcgi_param  SCRIPT_FILENAME  \$document_root\$fastcgi_script_name;
    include    fastcgi_params;
  }
}
EOF
}

#CONFIGURE MYSQL
if [ ! -z "$MYSQL_BIN" ]; then
  setupDatabase #call function
fi

echo "MySQL magento pass: $M2SETUP_DB_PASSWORD"

#GENERATE NGINX CONFIG
if  [ ! -z  "$M2SETUP_DOMAIN" ]; then
  echo "Generating nginx config..."
  generateNginxConf # call function
  echo "VHOST config file: ${green}/etc/nginx/conf.d/$M2SETUP_DOMAIN.conf${no}"
fi

#Increase php memory limit
sed -i -e 's/memory_limit = 128M/memory_limit = 2G/g' /etc/php.ini
systemctl reload php-fpm && systemctl reload nginx


#INSTALL MAGENTO
mkdir -p $M2SETUP_WORKDIR/.composer
export COMPOSER_HOME=$M2SETUP_WORKDIR/.composer #IMPORTANT TO USE auth.json file
export COMPOSER_MEMORY_LIMIT=-1
mkdir -p $M2SETUP_SITEDIR && cd $M2SETUP_WORKDIR
echo "Generating auth.json..."
generateAuthJSON #call function
chown -R php-fpm:php-fpm $M2SETUP_WORKDIR

cd $M2SETUP_SITEDIR
echo "Starting Magento install..."
su -c "$PHP_BIN $COMPOSER_BIN create-project --repository-url=https://repo.magento.com/ magento/project-$M2SETUP_EDITION-edition=$M2SETUP_VERSION ." -s /bin/bash php-fpm
ln -s $M2SETUP_WORKDIR/.composer ./var/composer_home
chmod +x $M2SETUP_SITEDIR/bin/magento

if [ "$M2SETUP_USE_SAMPLE_DATA" = true ]; then
  echo "Installing composer dependencies..."
  su -c "$PHP_BIN $COMPOSER_BIN update" -s /bin/bash php-fpm
  su -c "$PHP_BIN $M2SETUP_SITEDIR/bin/magento sampledata:deploy" -s /bin/bash php-fpm
  M2SETUP_USE_SAMPLE_DATA_STRING="--use-sample-data"
else
  M2SETUP_USE_SAMPLE_DATA_STRING=""
fi

echo "Running Magento 2 setup script..."
su -c "${PHP_BIN} ${M2SETUP_SITEDIR}/bin/magento setup:install \
    --db-host=${M2SETUP_DB_HOST} \
    --db-name=${M2SETUP_DB_NAME} \
    --db-user=${M2SETUP_DB_USER} \
    --db-password=${M2SETUP_DB_PASSWORD} \
    --base-url=${M2SETUP_BASE_URL} \
    --admin-firstname=${M2SETUP_ADMIN_FIRSTNAME} \
    --admin-lastname=${M2SETUP_ADMIN_LASTNAME} \
    --admin-email=${M2SETUP_ADMIN_EMAIL} \
    --admin-user=${M2SETUP_ADMIN_USER} \
    --admin-password=${M2SETUP_ADMIN_PASSWORD} \
    --backend-frontname=${M2SETUP_BACKEND_FRONTNAME} \
    ${M2SETUP_USE_SAMPLE_DATA_STRING}" -s /bin/bash php-fpm


#SETUP CRONS
echo "* * * * * php-fpm $PHP_BIN $M2SETUP_SITEDIR/bin/magento cron:run" >> /etc/crontab
echo "Here's your crontab:"
cat /etc/crontab

#FINISH
echo -e "\n"
echo "Installation summary"
echo "Domain: ${green}$M2SETUP_BASE_URL ${no}"
echo "Admin user: ${green}$M2SETUP_ADMIN_USER${no}"
echo "Admin pass: ${green}$M2SETUP_ADMIN_PASSWORD${no}"
echo "Admin email: ${green}$M2SETUP_ADMIN_EMAIL${no}"
echo "Currency: ${green}$M2SETUP_CURRENCY${no}"
echo "Timezone: ${green}$M2SETUP_TIMEZONE${no}"
echo "Backend frontname: ${green}$M2SETUP_BACKEND_FRONTNAME${no}"
echo "Magento database: ${green}$M2SETUP_DB_NAME${no}"
echo "MySQL Magento username: ${green}$M2SETUP_DB_USER${no}"
echo "MySQL Magento password: ${green}$M2SETUP_DB_PASSWORD${no}"
echo "MySQL root pass (also saved in /root/.my.cnf): ${green}$MYSQL_ROOT_PASS${no}"
echo "Nginx config: ${green}/etc/nginx/conf.d/$M2SETUP_DOMAIN.conf${no}"
echo "${red}Don't forget to check the firewall (80 , 443, etc) !${no}
```