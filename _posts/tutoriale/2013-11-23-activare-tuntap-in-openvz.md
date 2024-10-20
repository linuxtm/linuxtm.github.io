---
title: Activare TUN/TAP in OpenVZ
author: linuxtm
layout: post
permalink: /activare-tuntap-in-openvz/
categories:
  - Tutoriale
tags:
  - Activare TUN/TAP in OpenVZ
  - cum activez tun/tap in openvz
  - openvz tun/tap
  - tun/tap openvz
  - verificare tun/tap
  - verificare tun/tap openvz
---
OpenVZ suporta VPN-uri intr-un container (VPS) prin intermediul TUN/TAP. In exemplul de fata, activam TUN/TAP pentru VPS-ul cu id-ul 101.

101 - ID-ul VPS-ului. Inlocuiti 101 cu CTID-ul VPS-ului.

Ne asiguram ca modulul tun este activ pe nod:

```bash
lsmod | grep tun
```

Daca nu este listat, il incarcam cu urmatoarea comanda:

```bash
modprobe tun
```
```bash
lsmod | grep tun
```
*tun               82432  6*

Rulam urmatoarele comenzi pe nod:

```bash
vzctl set 101 --devnodes net/tun:rw --save
vzctl set 101 --devices c:10:200:rw --save  
vzctl set 101 --capability net_admin:on --save
vzctl exec 101 mkdir -p /dev/net
vzctl exec 101 chmod 600 /dev/net/tun 
```

Verificam daca TUN/TAP este activ sau nu :

```bash
vzctl enter 101
```

In VPS rulam: 

```bash
cat /dev/net/tun
```
*cat: /dev/net/tun: File descriptor in bad state*

Daca primiti rezultatul de mai sus, inseamna ca TUN/TAP e activat pentru VPS.

*cat: /dev/net/tun: No such device*

Daca primiti asta, TUN/TAP nu este activ pentru VPS,incercati sa-l activati din nou, eventual restartati VPS-ul.