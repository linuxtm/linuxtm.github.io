---
title: Cum setam un serviciu sa porneasca la boot ? Debian, CentOS, RedHat
author: linuxtm
layout: post
permalink: /cum-setam-un-serviciu-sa-porneasca-la-boot-debian-centos-redhat/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - cum pornesc automat ssh
  - cum pornesc httpd la boot
  - cum pornesc mysql la boot
  - cum pornim servicii automat la boot
  - cum previn un serviciu sa booteze
  - 'eroare apache: service httpd does not support chkconfig'
  - 'fix apache: service httpd does not support chkconfig'
  - index comenzi linux
  - prevenire boot serviciu linux
  - serviciu nu porneste la boot
  - tutoriale linux
---
Pentru distributii bazate pe Debian, se ruleaza urmatoarea comanda ca si root:

<pre>update-rc.d nume_serviciu defaults</pre>

Pentru CentOS si RedHat se ruleaza ca si root:

<pre>chkconfig nume_serviciu on</pre>

Daca pe CentOS / RedHat primiti urmatoarea eroare de la Apache:

<pre>Apache: service httpd does not support chkconfig</pre>

Trebuie adaugat in /etc/init.d/httpd urmatoarele:

<pre># Startup script for the Apache Web Server
#
# chkconfig: - 85 15
# description: Apache is a World Wide Web server. It is used to serve
# HTML files and CGI.
# processname: httpd
# pidfile: /usr/local/apache/logs/httpd.pid
# config: /usr/local/apache/conf/httpd.conf</pre>

Pentru a preveni un serviciu sa porneasca la boot, pe distributii bazate pe Debian se ruleaza:

<pre>update-rc.d nume_serviciu disable</pre>

Pentru celelalte distributii este evident (in loc de &#8220;on&#8221; punem &#8220;off&#8221;).