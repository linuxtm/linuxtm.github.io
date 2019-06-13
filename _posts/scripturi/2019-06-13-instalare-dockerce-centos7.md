---
title: Instalare docker-ce Centos7
author: linuxtm
layout: post
permalink: /instalare-dockerce-centos7/
categories:
  - Scripturi
tags:
  - comenzi linux
  - tutoriale linux
  - scripturi linux
  - script docker
  - script instalare docker
  - script centos7
---

<pre>
#!/bin/bash
set -e

yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager -y --add-repo https://download.docker.com/linux/centos/docker-ce.repo

yum install -y docker-ce docker-ce-cli containerd.io
systemctl start docker
systemctl enable docker

#Install docker-compose
curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
</pre>

Instructiunile oficiale: <a href="https://docs.docker.com/install/linux/docker-ce/centos/">https://docs.docker.com/install/linux/docker-ce/centos/</a>
