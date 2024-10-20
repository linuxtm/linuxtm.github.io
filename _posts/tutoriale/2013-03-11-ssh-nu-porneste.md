---
title: SSH nu porneste
author: linuxtm
layout: post
permalink: /ssh-nu-porneste/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - eroare restart ssh
  - nu pot porni ssh
  - nu pot restarta ssh
  - ssh nu functioneaza
  - ssh nu porneste
  - sshd/var/run/sshd must be owned by root and not group or world-writable
  - tutoriale linux
---
*/etc/init.d/ssh start  
Error:  
Starting OpenBSD Secure Shell server: sshd/var/run/sshd must be owned by root and not group or world-writable.*

Eroarea de mai sus inseamna ca au fost modificate permisiunile pentru /var/run/sshd , deci SSH nu functioneaza.  
Se poate rezolva ruland cele doua comenzi de mai jos:

```bash
rm -rf /var/run/sshd
```

```bash
invoke-rc.d ssh restart
```