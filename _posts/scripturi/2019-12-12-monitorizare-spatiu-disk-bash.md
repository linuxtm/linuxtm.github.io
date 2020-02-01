---
title: Script bash pentru monitorizare spatiu disk
author: linuxtm
layout: post
permalink: /script-monitorizare-spatiu-disk-bash/
categories:
  - Scripturi
tags:
  - comenzi linux
  - tutoriale linux
  - scripturi linux
  - script bash
  - monitorizare spatiu disk
  - script pentru monitorizare spatiu consumat
  - bash script monitor disk space azure vm
  - disk space alert bash
  - disk space monitoring script azure
  - script monitorizare spatiu disk
---

<pre>
#!/bin/bash
#More at https://linuxtm.ro
ROOT=$(df / | grep / | awk '{ print $5}' | sed 's/%//g')
DATADISK=$(df /var/www | grep / | awk '{ print $5}' | sed 's/%//g')
THRESHOLD=85

#Monitor root partition
if [ "$ROOT" -gt "$THRESHOLD" ] ; then
    mail -E -s 'Disk Space Alert' mail@example.com << EOF
Your root partition remaining free space is critically low. Used: $ROOT%
EOF
fi

#Monitor mounted disk
if [ "$DATADISK" -gt "$THRESHOLD" ] ; then
    mail -E -s 'Disk Space Alert' mail@example.com << EOF
Your datadisk partition remaining free space is critically low. Used: $DATADISK%
EOF
fi

</pre>
