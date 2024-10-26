---
title: Script instalare Magento2 in AWS
author: linuxtm
layout: post
permalink: /script-instalare-magento2-aws/
categories:
  - Scripturi
tags:
  - comenzi linux
  - tutoriale linux
  - scripturi linux
  - script instalare magento
  - script magento aws
  - magento2 aws install script
  - instalare automata magento2 in aws
---

```bash
#!/bin/bash
#This script will install Magento 2 in AWS.
#When the script finishes, you will get a summary of the installation (usernames, passwords, etc).
#
#Prerequisites:
#Custom AMI based on AMI2 with php-fpm and nginx installed
#AWS services created via CloudFormation template (RDS, ElastiCache, ElasticSearch)

set -e

no=$(tput sgr0)
red=$(tput setaf 1)
green=$(tput setaf 2)

#Set / ask for variables
PHP_BIN=$(command -v php)
COMPOSER_BIN=$(command -v composer)

#User configured in /etc/php-fpm.d/www.conf
PHPFPMUSER=nginx

M2SETUP_WORKDIR=/var/www
M2SETUP_SITEDIR=/var/www/html
MAGENTOBIN=$M2SETUP_SITEDIR/bin/magento

############################# MODIFY VARIABLES #############################

#Do not include :6379 on REDIS_HOST
REDIS_HOST=
#Include trailing slash / for ELASTICSEARCH_HOST
ELASTICSEARCH_HOST=

M2SETUP_DOMAIN=
M2SETUP_DB_HOST=
M2SETUP_DB_NAME=
M2SETUP_DB_USER=
M2SETUP_DB_PASSWORD=
M2SETUP_VERSION=
M2SETUP_USE_SAMPLE_DATA=false

ELASTICSEARCH_PORT=443
COMPOSER_USER=
COMPOSER_PASS=

#MAGENTO VARIABLES
M2SETUP_EDITION=community
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

########################### END MODIFY VARIABLES ###########################


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

#INSTALL MAGENTO
mkdir -p $M2SETUP_WORKDIR/.composer
export COMPOSER_HOME=$M2SETUP_WORKDIR/.composer #IMPORTANT TO USE auth.json file
export COMPOSER_MEMORY_LIMIT=-1
mkdir -p $M2SETUP_SITEDIR && cd $M2SETUP_WORKDIR

echo "Generating auth.json..."
generateAuthJSON #call function
chown -R $PHPFPMUSER:$PHPFPMUSER $M2SETUP_WORKDIR

cd $M2SETUP_SITEDIR
echo "Starting Magento install..."
su -c "$PHP_BIN $COMPOSER_BIN create-project --repository-url=https://repo.magento.com/ magento/project-$M2SETUP_EDITION-edition=$M2SETUP_VERSION ." -s /bin/bash $PHPFPMUSER
ln -s $M2SETUP_WORKDIR/.composer ./var/composer_home
chmod +x $MAGENTOBIN

if [ "$M2SETUP_USE_SAMPLE_DATA" = true ]; then
  echo "Installing composer dependencies..."
  su -c "$PHP_BIN $COMPOSER_BIN update" -s /bin/bash $PHPFPMUSER
  su -c "$PHP_BIN $M2SETUP_SITEDIR/bin/magento sampledata:deploy" -s /bin/bash $PHPFPMUSER
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
    ${M2SETUP_USE_SAMPLE_DATA_STRING}" -s /bin/bash $PHPFPMUSER

echo "Configuring ElasticSearch..."
su -c "$PHP_BIN $MAGENTOBIN config:set catalog/search/engine elasticsearch6" -s /bin/bash $PHPFPMUSER
su -c "$PHP_BIN $MAGENTOBIN config:set catalog/search/elasticsearch6_server_hostname $ELASTICSEARCH_HOST" -s /bin/bash $PHPFPMUSER
su -c "$PHP_BIN $MAGENTOBIN config:set catalog/search/elasticsearch6_server_port $ELASTICSEARCH_PORT" -s /bin/bash $PHPFPMUSER

#SHOW SUMMARY
echo -e "\n"
echo "Installation summary"
echo "Domain: ${green}$M2SETUP_BASE_URL ${no}"
echo "Admin user: ${green}$M2SETUP_ADMIN_USER${no}"
echo "Admin pass: ${green}$M2SETUP_ADMIN_PASSWORD${no}"
echo "Admin email: ${green}$M2SETUP_ADMIN_EMAIL${no}"
echo "Currency: ${green}$M2SETUP_CURRENCY${no}"
echo "Timezone: ${green}$M2SETUP_TIMEZONE${no}"
echo "Backend frontname: ${green}$M2SETUP_BACKEND_FRONTNAME${no}"
```