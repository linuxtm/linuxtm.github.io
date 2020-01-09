---
title: Instalare pachete comune AMI Linux
author: linuxtm
layout: post
permalink: /instalare-pachete-ami-linux/
categories:
  - AWS
tags:
  - comenzi linux
  - tutoriale aws
  - aws cli comenzi
  - pachete comune ami linux
  - mysql client ami linux
  - install mysql ami linux
  - comenzi utile aws cli
  - aws linie comanda
  - tutoriale aws cli
  - tutoriale aws cloud
---

Instalare epel
<pre>sudo amazon-linux-extras install -y epel</pre>

Instalare client mysql
<pre>sudo yum install -y https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm && sudo yum install -y mysql-community-client</pre>

Redis-CLI
<pre>sudo yum install -y gcc
wget http://download.redis.io/redis-stable.tar.gz && tar xvzf redis-stable.tar.gz && cd redis-stable && make
sudo cp src/redis-cli /usr/bin/</pre>
