---
title: Instalare PHP 7.1 , 7.2 sau 7.3 pentru Magento2
author: linuxtm
layout: post
permalink: /instalare-php7-magento2-centos7/
categories:
  - Scripturi
tags:
  - comenzi linux
  - tutoriale linux
  - scripturi linux
  - script bash
  - instalare php7 centos7
  - php7 magento2 ius repo
  - install php7 from ius repo
---

Scriptul de mai jos instaleaza PHP 7.1, 7.2 sau 7.3 din IUS repository cu toate extensiile de php necesare pentru Magento2.
Functioneaza doar pe CentOS 7.

<pre>
#!/bin/bash
set -e

no=$(tput sgr0)
red=$(tput setaf 1)
green=$(tput setaf 2)
DISTRO=$(awk -F= '/^NAME/{print $2}' /etc/os-release)

#Check distro, must be Centos
if [[ $DISTRO != *CentOS* ]]; then
  echo "This script only works on Centos 7. Goodbye !"
  exit 1
fi

#Check if php binary exists
if ! [ -x "$(command -v php)" ]; then
  echo "PHP ${red}not present${no} , let's install it."
  read -p "Please specify one of these versions: ${green}71${no} , ${green}72${no} or ${green}73${no} : " V
  #Force version
  if [[ $V != @(71|72|73) ]] ; then
    echo "Plese write one of the green values: ${green}71${no} / ${green}72${no} / ${green}73${no}"
    exit 1
  fi

  yum install -y https://centos7.iuscommunity.org/ius-release.rpm

  #If php 7.1, enable IUS Archive
  if [ $V == 71 ] ; then
    yum-config-manager enable ius-archive
  fi

  #If php 7.3, remove "u" from package name
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
    echo "${green}Enabling PHP-FPM...${no}"
    systemctl enable php-fpm
    echo "${green}Starting PHP-FPM...${no}"
    systemctl start php-fpm
    systemctl status php-fpm
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
 echo "${green}Enabling PHP-FPM...${no}"
  systemctl enable php-fpm
  echo "${green}Starting PHP-FPM...${no}"
  systemctl start php-fpm
  systemctl status php-fpm
else
  echo "${green}PHP already installed. Goodbye !${no}"
  php -v
  exit 1
fi
</pre>
