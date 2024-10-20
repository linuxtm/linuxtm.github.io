---
title: 'Problema autentificare webmail cPanel'
author: linuxtm
layout: post
permalink: /problema-autentificare-webmail-cpanel/
categories:
  - Tutoriale
tags:
  - 'dovecot: auth: Error: Cpanel::MailAuth: Failed to lookup domain owner of'
  - eroare dovecot
  - eroare webmail cpanel
  - problema autentificare webmail cpanel
  - 'webmail cpanel failed to lookup domain owner of'
  - outook cere parola
  - thunderbird cere parola
---

Problema se manifesta dupa cum urmeaza: dupa ce va autentificati in webmail, apare mesajul "Login successfull" si sunteti directionati spre pagina de selectare a interfetei dorite (Horde, Roundcube, etc), iar dupa ce dati click pe una din optiuni, sunteti redirectionati la o pagina conform careia userul sau parola sunt incorecte.

Daca verificam */var/log/maillog* , observam urmatoarea eroare:
*dovecot: auth: Error: Cpanel::MailAuth: Failed to lookup domain owner of domeniu.ro*

Verificam cine detine domeniul (ownerul) in cauza, rezultatul va fi gol:
```bash
/scripts/whoowns linuxtm.ro
```


Problema in acest caz este generata de hostname-ul serverului, acesta fiind cel mai probabil identic cu numele domeniului. De exemplu, domeniul linuxtm.ro nu poate avea ca si hostname "linuxtm.ro", trebuie sa fie configurat ca si un subdomeniu sub forma "ceva.linuxtm.ro". Cele mai comune optiuni sunt "vps, server, host" (ex: vps.linuxtm.ro )

Pentru a rezolva problema, trebuie schimbat hostname-ul cu unul valid sub forma prezentata mai sus. Dupa schimbarea hostname-ului, rulam urmatoarea comanda:

```bash
/scripts/updateuserdomains --force
```

Acum daca verificam owner-ul domeniului, ar trebui sa obtinem:
```bash
root@srv [~]# /scripts/whoowns linuxtm.ro
linuxtm

```

Dupa completarea acestor pasi ar trebui sa va puteti autentifica in Webmail. 
<p>Nota: problema de asemenea se manifesta si in clientii de mail (Outlook, Thunderbird, etc) prin solicitarea parolei in mod repetat.</p>