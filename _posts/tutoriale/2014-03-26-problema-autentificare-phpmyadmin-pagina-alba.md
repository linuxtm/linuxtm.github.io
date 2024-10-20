---
title: 'Problema autentificare phpMyAdmin &#8211; pagina alba'
author: linuxtm
layout: post
permalink: /problema-autentificare-phpmyadmin-pagina-alba/
categories:
  - Tutoriale
tags:
  - AuthenticationCpanel.class.php
  - nu ma pot loga in phpmyadmin
  - pagina alba phpmyadmin
  - problema phpmyadmin
  - tutoriale linux
---
Daca incercati sa va autentificati in phpMyAdmin si dupa introducerea detaliilor de logare va afiseaza o pagina alba, indiferent de ce faceti, puteti incerca urmatoarele:

1. Verificati logurile

```bash
tail -f /usr/local/cpanel/logs/error_log
```

2. Daca nu aveti nimic util in log, incercati sa activati &#8220;**display_errors**&#8221; in *php.ini*.

3. In cazul de fata, logul afisa urmatoarea eroare:

*PHP Fatal error: Call to undefined function PMA\_generate\_common_url() in /usr/local/cpanel/base/3rdparty/phpMyAdmin/libraries/plugins/auth/AuthenticationCpanel.class.php on line 611*

3. Problema s-a rezolvat prin schimbarea parolei contului de cPanel (se poate schimba inapoi la parola originala dupa prima schimbare). Inainte de a schimba parola, trebuie sa dati logout din cPanel.

Daca problema nu se rezolva dupa schimbarea parolei, se poate incerca un update la phpMyAdmin:

```bash
/usr/local/cpanel/bin/updatephpmyadmin --force
```