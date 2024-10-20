---
title: Configurare environment user ssh
author: linuxtm
layout: post
permalink: /configurare-environment-ssh/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - configurare environment useri ssh
  - activare useri ssh
  - ssh user environment
  - mai multe persoane pe acelasi user ssh
  - mai multe chei ssh pe acelasi user
---

In cazul in care exista mai multe persoane care folosesc acelasi user, avem nevoie sa facem o distinctie intre ei.
Pentru a realiza acest lucru, trebuie sa activam environmentul ssh.

Folosind editorul preferat, modificam <em>/etc/profile</em> si adaugam:
```bash

if [ "$SSH_USER" != "" ]; then logger -ip authpriv.notice -t sshd "Accepted publickey for $SSH_USER";fi
```

Dupa care, modificam (sau adaugam) optiunea de mai jos in <em>/etc/ssh/sshd_config</em> apoi restart la serviciul ssh:
```bash
PermitUserEnvironment yes
```

Cu aceste setari active, putem adauga cheile ssh in <em>/home/user/.ssh/authorized_keys</em> sub forma: 
```bash
environment="SSH_USER=popescu.ion" ssh-rsa AAAAfgds...
````

Astfel, in loguri vom vedea exact ce persoane au intrat pe server folosind userul comun.
