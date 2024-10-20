---
title: 'Eroare conectare SSH: Could not load host key: /etc/ssh/ssh_host_rsa_key'
author: linuxtm
layout: post
permalink: /eroare-conectare-ssh-could-not-load-host-key-etcsshssh_host_rsa_key/
categories:
  - Tutoriale
tags:
  - 'Could not load host key: /etc/ssh/ssh_host_rsa_key'
  - eroare conectare ssh
  - eroare ssh
  - 'fix Could not load host key: /etc/ssh/ssh_host_rsa_key'
---
In */var/log/auth.log* , observam urmatoarea eroare: 

*error: Could not load host key: /etc/ssh/ssh_host_rsa_key
error: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
error: @         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
error: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
error: Permissions 0777 for '/etc/ssh/ssh_host_dsa_key' are too open.
error: It is recommended that your private key files are NOT accessible by others.
error: This private key will be ignored.
error: bad permissions: ignore key: /etc/ssh/ssh_host_dsa_key
error: Could not load host key: /etc/ssh/ssh_host_dsa_key
fatal: /var/run/sshd must be owned by root and not group or world-writable.*

Eroarea este destul de explicativa, iar aceasta se poate rezolva prin schimbarea permisiunilor, ruland urmatoarele comenzi:

```bash
chmod 600 /var/run/sshd
```

```bash
chmod 600 /etc/ssh/ssh_host_*
```