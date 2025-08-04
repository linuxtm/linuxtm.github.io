---
title: Instalare Docker-CE pe Ubuntu 20 (Desktop)
author: linuxtm
layout: post
permalink: /instalare-docker-ce-ubuntu20-desktop/
categories:
  - Scripturi
tags:
  - comenzi linux
  - tutoriale linux
  - scripturi linux
  - script docker
  - script instalare docker
  - script docker ubuntu 20 desktop
  - script instalare docker ubuntu 20
---

Scriptul de mai jos va adauga repo-ul Docker, cheia repo-ului si va instala Docker pe Ubuntu 20.04.

One-Liner pentru usurinta:
```bash
wget https://raw.githubusercontent.com/linuxtm/linuxtm.github.io/master/scripturi/installDockerUbuntu20.sh && chmod +x installDockerUbuntu20.sh && ./installDockerUbuntu20.sh
```

Sau copy-paste:
```bash
#!/bin/bash
#More at https://linuxtm.ro
set -e
no=$(tput sgr0)
red=$(tput setaf 1)

sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
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
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo "Done."
echo -e "${red}In order for docker to work as a non-root user, please logout or restart your computer!${no}"
```

Instructiunile oficiale: <a href="https://docs.docker.com/engine/install/ubuntu/">https://docs.docker.com/engine/install/ubuntu/</a>

