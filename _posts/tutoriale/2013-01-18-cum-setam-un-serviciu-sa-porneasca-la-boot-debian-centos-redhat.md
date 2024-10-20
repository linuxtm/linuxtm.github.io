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

```bash 
update-rc.d nume_serviciu defaults
``` 

Pentru CentOS si RedHat se ruleaza ca si root:

```bash
chkconfig nume_serviciu on
``` 

Daca pe CentOS / RedHat primiti urmatoarea eroare de la Apache:

<em>Apache: service httpd does not support chkconfig</em>

Trebuie adaugat in /etc/init.d/httpd urmatoarele:

```bash 
# Startup script for the Apache Web Server
#
# chkconfig: - 85 15
# description: Apache is a World Wide Web server. It is used to serve
# HTML files and CGI.
# processname: httpd
# pidfile: /usr/local/apache/logs/httpd.pid
# config: /usr/local/apache/conf/httpd.conf 
``` 

Pentru a preveni un serviciu sa porneasca la boot, pe distributii bazate pe Debian se ruleaza:

```bash
update-rc.d nume_serviciu disable
``` 

Pentru celelalte distributii este evident (in loc de &#8220;on&#8221; punem &#8220;off&#8221;).