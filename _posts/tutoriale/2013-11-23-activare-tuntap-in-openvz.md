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

101 &#8211; ID-ul VPS-ului. Inlocuiti 101 cu CTID-ul VPS-ului.

Ne asiguram ca modulul tun este activ pe nod:

<pre>[root@srv/]#  lsmod | grep tun</pre>

Daca nu este listat, il incarcam cu urmatoarea comanda:

<pre>[root@srv/]# modprobe tun
[root@srv/]# lsmod | grep tun
tun               82432  6</pre>

Rulam urmatoarele comenzi pe nod:

<pre>[root@srv/]#  vzctl set 101 --devnodes net/tun:rw --save
[root@srv/]#  vzctl set 101 --devices c:10:200:rw --save  
[root@srv/]#  vzctl set 101 --capability net_admin:on --save
[root@srv/]#  vzctl exec 101 mkdir -p /dev/net
[root@srv/]#  vzctl exec 101 chmod 600 /dev/net/tun 
</pre>

Verificam daca TUN/TAP este activ sau nu :

<pre>[root@srv/]# vzctl enter 101</pre>

In VPS rulam: 

<pre>[root@vps/]# cat /dev/net/tun</pre>

<pre>cat: /dev/net/tun: File descriptor in bad state</pre>

Daca primiti rezultatul de mai sus, inseamna ca TUN/TAP e activat pentru VPS.

<pre>cat: /dev/net/tun: No such device</pre>

Daca primiti asta, TUN/TAP nu este activ pentru VPS,incercati sa-l activati din nou, eventual restartati VPS-ul.