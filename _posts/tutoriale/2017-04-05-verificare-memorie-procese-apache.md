---
title: Verificare utilizare memorie proces Apache
author: linuxtm
layout: post
permalink: /verificare-memorie-proces-apache/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - verificare memorie apache
  - memorie proces apache
  - cum aflu cata memorie foloseste un proces apache
  - memorie apache
  - optimizare memorie apache
  - afla cata memorie consuma un proces apache
---

Pentru a optimiza Apache-ul, trebuie sa tinem cont de memoria RAM totala disponibila pe server.
Astfel putem decide cata memorie vom permite Apache-ului sa folosesca - mai exact <i>nr de procese</i> x <i>consumul de memorie per process</i>

Putem sa aflam cata memorie consuma un proces apache folosind comenzile de mai jos.

Verificare utilizare memorie proces apache
<pre>
ps aux | grep 'httpd' | awk '{print $6/1024 " MB";}'
</pre>

Aceeasi comanda, insa acum calculeaza utilizarea memoriei in medie per proces.
<pre>
ps aux | grep 'httpd' | awk '{print $6/1024;}' | awk '{avg += ($1 - avg) / NR;} END {print avg " MB";}'
</pre>

Pentru optimizarea apache, se poate folosi scriptul <a href="https://github.com/richardforth/apache2buddy/blob/master/README.md">Apache2Buddy</a>, care ofera detalii amanuntite despre situatia apache-ului pe server in momentul testarii.
<pre>
curl -sL https://raw.githubusercontent.com/richardforth/apache2buddy/master/apache2buddy.pl | perl
</pre>

<strong>Optimizare apache</strong>

Ca si formula de calcul impartim totalul de RAM (minus 10% - lasam 10% ram liber pentru sistem si alte procese) la consumul mediu de memorie a proceselor apache. Astfel obtinem valorile <strong>MaxClients/ServerLimit</strong>.

Mai departe, calculam restul valorilor dupa cum urmeaza:
<pre>
<strong>StartServers</strong> 30% din MaxClients
<strong>MinSpareServers</strong> 5% din MaxClients
<strong>MaxSpareServers</strong> 10% din MaxClients
<strong>ServerLimit</strong> == MaxClients
<strong>MaxConnectionsPerChild</strong> 2000
</pre>
