---
title: Verificare certificat SSL + cheie privata din CLI
author: linuxtm
layout: post
permalink: /chown-symlinks/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - verificare ssl din terminal
  - verificare crt si key ssl
  - cum verific ssl din terminal
  - verificare potrivire crt si key ssl
  - ssl cert cli
---

Putem verifica daca avem cheia potrivita pentru certificatul nostru prin obtinerea SHA-ului si compararea acestuia (trebuie sa fie identic):

<pre>openssl pkey -in cheie.txt -pubout -outform pem | sha256sum</pre>
<pre>openssl x509 -in certificat.crt -pubkey -noout -outform pem | sha256sum</pre>

Bonus, daca avem certificate pentru Apache insa avem nevoie de certificat pentru Nginx, putem concatena certificatul si bundle-ul astfel:

<pre>cat certificat.crt certificat.ca-bundle >> certificatNginx.crt</pre>
