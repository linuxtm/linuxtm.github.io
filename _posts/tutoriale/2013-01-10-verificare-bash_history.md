---
title: Verificare .bash_history
author: linuxtm
layout: post
permalink: /verificare-bash_history/
Sidebar_value:
  - on
Nav_value:
  - on
wpsd_autopost:
  - 1
categories:
  - Tutoriale
tags:
  - comanda verificare bash_history
  - comenzi linux
  - cum verific istoric comenzi linux
  - verificare bash_history
---
Pentru afisearea istoricului comenzilor se ruleaza:

```bash
history
```

Output-ul fiind afisat sub forma:

*245 ls  
246 cd public_html/  
247 ls  
248 nano /etc/httpd/conf/httpd.conf  
249 ls*

O alta varianta (se poate rula din orice director) ar fi:

```bash
cat /root/.bash_history
```

Pentru afisarea mai multor comenzi se ruleaza:

```bash
more /root/.bash_history
```

Pentru a gasi o comanda anume printre comenzilie rulate anterior, trebuie facut un pipe la history prin grep:

```bash
history | grep -i primele litere din comanda
```

Pentru detalii suplimentare vezi comanda history [aici.][1]

 [1]: http://linuxtm.ro/history/