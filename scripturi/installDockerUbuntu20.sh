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
