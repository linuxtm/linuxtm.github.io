---
title: 'Stergere din loguri a CRON[PID]: pam_unix(cron:session)'
author: linuxtm
layout: post
permalink: /stergere-din-loguri-a-cronpid-pam_unixcronsession/
categories:
  - Tutoriale
tags:
  - 'pam_unix(cron:session): session closed for user root'
  - 'pam_unix(cron:session): session opened for user root'
  - stergere cron din loguri
  - stergere cron ssh din log
  - 'Stergere din loguri a CRON[PID]: pam_unix(cron:session)'
---
Daca si pe voi va &#8220;deranjeaza&#8221; astfel de mesaje in log, ati nimerit bine:

*Dec 17 08:11:01 backup CRON[17586]: pam_unix(cron:session): session opened for user root by (uid=0)  
Dec 17 08:11:01 backup CRON[17586]: pam_unix(cron:session): session closed for user root  
Dec 17 08:12:01 backup CRON[17593]: pam_unix(cron:session): session opened for user root by (uid=0)*

Mergem in directorul **/etc/pam.d** si deschidem fisierul **common-session-noninteractive** cu editorul preferat, dupa care cautam linia urmatoare:

```bash
session required pam_unix.so
```

Deasupra acestei linii, adaugam urmatoarele:

```bash
session [success=1 default=ignore] pam_succeed_if.so service in cron quiet use_uid
```

Salvam fisierul si iesim, dupa care restartam crond:

```bash
service cron restart
```

Explicatie:  
Inainte de a va impacienta, trebuie sa stiti ca mesajele respective sunt normale. Acestea sunt generate de cron-ul care se autentifica in sistem si verifica fisierele de configurare sa vada daca s-a schimbat ceva. Devreme ce cron poate rula in fiecare minut, probabil veti vedea multe astfel de mesaje in log. Prima linie este generata de fiecare data cand cronul incepe (session open) iar a 2-a cand se inchide (session closed).