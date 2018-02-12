---
title: Rezolvare problema chei ssh_host_rsa si dsa
author: linuxtm
layout: post
permalink: /rezolvare-problema-chei-ssh_host_rsa-si-dsa/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - problema chei ssh
  - problema chei ssh_host_rsa si dsa
  - problema cheie ssh
  - rezolvare problema cheie ssh
  - tutoriale linux
---
Daca din ceva motiv va lipsesc cheile **ssh\_host\_dsa_key** si **ssh\_host\_rsa_key** , mai jos aveti comenzile pe care trebuie sa le rulati pentru a reface cheile. Eroarea primita:

<pre><em>root@root:/# /etc/init.d/ssh restart
Could not load host key: /etc/ssh/ssh_host_rsa_key
Could not load host key: /etc/ssh/ssh_host_dsa_key</em>
</pre>

Generare cheie SSH\_HOST\_RSA_KEY , fara parola (dam enter la prompt)

<pre>ssh-keygen -t rsa1 -f /etc/ssh/ssh_host_rsa_key</pre>

Generare cheie SSH\_HOST\_DSA_KEY

<pre>ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key</pre>

Restartam serverul ssh si acum ar trebui sa functioneze corect.