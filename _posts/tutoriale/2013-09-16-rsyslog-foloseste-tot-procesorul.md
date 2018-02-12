---
title: Rsyslog foloseste tot procesorul
author: linuxtm
layout: post
permalink: /rsyslog-foloseste-tot-procesorul/
categories:
  - Tutoriale
tags:
  - milioane de erori in rsyslog
  - rezolvare erori rsyslog
  - rezolvare problema cpu rsyslog
  - rezolvare probleme rsyslog
  - rsyslog cpu
  - rsyslog foloseste 100% procesor
  - rsyslog foloseste mult procesor
  - Rsyslog foloseste tot procesorul
---
In cazul in care rsyslog foloseste mult procesor (100% sau mai mult) in OpenVZ, trebuie comentata linia de mai jos pentru ca, kernelul vps-urilor nu ruleaza in interiorul acestora iar rsyslog incearca fara nici un motiv, in mod constant sa citeasca */proc/kmsg* producand astfel milioane de erori intr-un timp foarte scurt (de unde si consumul ridicat de CPU).

*/var/log/syslog* va arata ceva de genul:

<pre>Sep 16 21:47:38 server kernel: Cannot read proc file system: 1 - Operation not permitted.
Sep 16 21:48:08 server kernel: last message repeated 6125550 times
Sep 16 21:49:08 server kernel: last message repeated 13230238 times
Sep 16 21:50:08 server kernel: last message repeated 11995373 times
</pre>

Pentru a rezolva problema trebuie comentata urmatoarea linie in /etc/rsyslogd.conf

<pre>$ModLoad imklog   # provides kernel logging support (previously done by rklogd)</pre>

Comentata:

<pre>#$ModLoad imklog   # provides kernel logging support (previously done by rklogd)</pre>