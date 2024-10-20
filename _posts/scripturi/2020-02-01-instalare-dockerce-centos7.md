---
title: Instalare Docker-CE pe Centos 7
author: linuxtm
layout: post
permalink: /instalare-docker-ce-centos7/
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

One-Liner pentru usurinta:
```bash
wget https://raw.githubusercontent.com/linuxtm/linuxtm.github.io/master/scripturi/installDockerCentos7.sh && chmod +x installDockerCentos7.sh && ./installDockerCentos7.sh
````


Sau copy-paste:
```bash
#!/bin/bash
#More at https://linuxtm.ro
set -e

yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager -y --add-repo https://download.docker.com/linux/centos/docker-ce.repo

yum install -y docker-ce docker-ce-cli containerd.io
systemctl start docker
systemctl enable docker

#Install docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

Instructiunile oficiale: <a href="https://docs.docker.com/engine/install/centos/">https://docs.docker.com/engine/install/centos/</a>
