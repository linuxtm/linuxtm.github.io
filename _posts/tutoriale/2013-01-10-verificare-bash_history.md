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

<pre>history</pre>

Output-ul fiind afisat sub forma:

*245 ls  
246 cd public_html/  
247 ls  
248 nano /etc/httpd/conf/httpd.conf  
249 ls*

O alta varianta (se poate rula din orice director) ar fi:

<pre>cat /root/.bash_history</pre>

Pentru afisarea mai multor comenzi se ruleaza:

<pre>more /root/.bash_history</pre>

Pentru a gasi o comanda anume printre comenzilie rulate anterior, trebuie facut un pipe la history prin grep:

<pre>history | grep -i primele litere din comanda</pre>

Pentru detalii suplimentare vezi comanda history [aici.][1]

 [1]: http://linuxtm.ro/history/