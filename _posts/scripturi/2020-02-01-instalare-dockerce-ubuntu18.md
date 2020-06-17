---
title: Instalare Docker-CE pe Ubuntu 18 (Desktop)
author: linuxtm
layout: post
permalink: /instalare-docker-ce-ubuntu18-desktop/
categories:
  - Scripturi
tags:
  - comenzi linux
  - tutoriale linux
  - scripturi linux
  - script docker
  - script instalare docker
  - script docker ubuntu 18 desktop
  - script instalare docker ubuntu 18
---

One-Liner pentru usurinta:
<pre>
wget https://raw.githubusercontent.com/linuxtm/linuxtm.github.io/master/scripturi/installDockerUbuntu18.sh && chmod +x installDockerUbuntu18.sh && ./installDockerUbuntu18.sh
</pre>

Sau copy-paste:
<pre>
#!/bin/bash
#More at https://linuxtm.ro
set -e
no=$(tput sgr0)
red=$(tput setaf 1)

sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install -y docker-ce

sudo usermod -aG docker $USER
sudo systemctl enable docker && sudo systemctl start docker

#Install docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo "Done."
echo -e "${red}In order for docker to work as a non-root user, please logout or restart your computer!${no}"
</pre>

Instructiunile oficiale: <a href="https://docs.docker.com/v17.09/engine/installation/linux/docker-ce/ubuntu/">https://docs.docker.com/v17.09/engine/installation/linux/docker-ce/ubuntu/</a>
