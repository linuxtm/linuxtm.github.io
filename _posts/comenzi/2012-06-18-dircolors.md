---
title: dircolors
author: linuxtm
layout: post
permalink: /dircolors/
categories:
  - Comenzi
tags:
  - comanda culori foldere linux
  - comanda dircolors
  - comenzi linux
  - comenzi linux a-z
  - comenzi linux de la a la z
  - culori foldere linux
  - explicatie comenzi linux
  - index comenzi linux
  - lista comenzi linux
  - toate comenzile linux
---
Seteaza culori pentru &#8216;ls&#8217;

Sintaxa

eval \`dircolors [optiuni]&#8230; [fisier]\`

Daca fisierul este specificat, &#8216;dircolors&#8217; il citeste pentru a determina ce culori sa foloseasca pentru fiecare tip de fisier si pentru extensiile acestora.  
Altfel , este utilizata o baza de date precompilata. Pentru detalii despre formatul acestor fisiere, rulam \`dircolors &#8211;print-database&#8217;.

Rezultatul este o comanda shell pentru a seta variabila de mediu \`LS_COLORS&#8217;. Se poate specifica sintaxa de shell pentru a fi utilizata in linia de comanda, sau \`dircolors&#8217; o va ghici din valoarea variabilei de mediu \`SHELL&#8217;.

Optiuni

-b  
&#8211;sh  
&#8211;bourne-shell  
Afiseaza comenzi din Bourne shell. Este rezultatul implicit daca variabila \`SHELL&#8217; este setata si nu se termina cu \`csh&#8217; or \`tcsh&#8217;.

-c  
&#8211;csh  
&#8211;c-shell  
Afiseaza comenzi din C shell. Acesta este implicit daca \`SHELL&#8217; se termina cu \`csh&#8217; or \`tcsh&#8217;.

-p  
&#8211;print-database  
Afiseaza configurarea bazei de date (precompilata) a culorilor. Acest rezultat este in sine un fisier de configurare valid, si e destul de descriptiv in ceea ce priveste posibilitatile.