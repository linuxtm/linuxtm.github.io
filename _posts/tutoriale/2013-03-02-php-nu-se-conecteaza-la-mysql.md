---
title: PHP nu se conecteaza la MySQL
author: linuxtm
layout: post
permalink: /php-nu-se-conecteaza-la-mysql/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - php nu se conecteaza la mysql
  - tutoriale linux
---
Daca ati instalat web serverul Apache si aveti MySQL-ul configurat, totul functioneaza normal mai putin faptul ca nu va puteti conecta la la o baza de date MySQL (desi va puteti conecta la serverul MySQL), atunci va lipseste modulul MySQL pentru PHP(4 sau 5).  
Fara *php-mysql*, scripturile PHP nu se vor putea conecta la bazele de date din serverul MySQL.  
Solutia este instalarea acestui modul dupa cum urmeaza:

Debian / Ubuntu

```bash
apt-get install php5-mysql
```

Fedora / CentOS / RHEL 5

```bash
yum install php-mysql
```

RHEL

```bash
up2date php-mysql
```

Nota: Dupa instalare, trebuie restartat webserverul: *service httpd restart*