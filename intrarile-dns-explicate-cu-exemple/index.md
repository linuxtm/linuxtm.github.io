---
title: DNS Explicat
author: linuxtm
layout: page
tags:
  - intrari dns
  - dns explicat
  - tipuri de dns records
  - exemple dns
  - exemple cname
  - dns explicat cu exemple
  - tipuri dns
  - cum functioneaza dns
---

DNS (Domain Name System), este un serviciu care traduce nume si adrese din internet.
Numele in internet sunt nume pe care noi le folosim pentru a ne referi la un anume host prin internet, de exemplu www.linuxtm.ro.
Adresele in internet sunt numerele folosite de routere pentru a transmite traffic prin Internet, adrese precum 176.223.207.45.

Ce sunt intrarile DNS ?
Intrarile DNS (DNS records) sau "Zone files" sunt folosite pentru traducerea URL-urilor in adrese IP. Localizate pe servere numite servere DNS, aceste intrari sunt de obicei conexiunea site-ului cu restul lumii. Cererile spre un site sunt trimise mai departe spre serverele DNS si apoi sunt directionate spre servere web, care servesc continutul site-ului, sau serverelor de mail care administreaza receptionarea de mail-uri.

Tipuri de intrari DNS (DNS Records)
<ul>
<li>A</li>
<li>AAAA</li>
<li>CNAME</li>
<li>MX</li>
<li>PTR</li>
<li>NS</li>
<li>SOA</li>
<li>SRV</li>
<li>TXT</li>
</ul>

Intrarile DNS de mai sus sunt folosite in toate configurarile DNS. Mai jos, le vom discuta pe fiecare in parte, cu exemple.

<strong>A Record</strong><br>
A record sau address record.

"Address record", aloca o adresa IP unui domeniu sau subdomeniu. Cand a fost gandit DNS-ul, a fost gandit in asa fel incat sa nu existe 2 intrari A record care duc la aceeasi adresa IP.

Presupunem ca avem linuxtm.ro, si vrem sa ii alocam ip-ul 10.0.0.1, atunci va trebui sa creem o intrare A record cu "www.linuxtm.ro" ca si Fully Qualified Domain Name si sa completam "10.0.0.1".

De acum inainte, toate cererile pentru www.linuxtm.ro vor fi trimise spre serverul cu aceasta adresa IP. Un A record, este de asemenea util in cazul in care avem mai diferite subdomenii pe diferite sisteme.

<em><strong>Exemplu de A Record</strong></em>
<pre>linuxtm.ro. IN A 192.168.1.1</pre>
Unde
<strong>IN</strong> indica Internetul
<strong>A</strong> indica Address record.

Exemplul de mai sus indica faptul ca adresa IP a domeniului linuxtm.ro este 192.168.1.1

<strong>AAAA Record</strong>

Adresa DNS obisnuita este definita in 32biti de catre adresele IPv4, iar fiindca acestea sunt pe terminate, s-a creat o noua adresa (IPv6) in 128biti.
O intrare de tip AAAA sau o adresa IPv6, traduce un hostname intr-o adresa IPv6 in 128biti. Cei 4 de "A" din numele intrarii servesc drept mnemonic si ne aminteste faptul ca o adresa IPv6 este de 4 ori mai mare decat o adresa IPv4. IPv6 este de asemenea structurat la fel ca si IPv4, doar ca este mult mai mare.

<em><strong>Exemplu de AAAA Record</strong></em>
<pre>linuxtm.ro AAAA 3ffe:1900:4545:2:02d0:09ff:fef7:6d2c</pre>
<strong>CNAME Record</strong>
Intrarile CNAME (sau canonical name record) fac un domeniu alias la un altul. Domeniul alias primeste toate subdomeniile si intrarile DNS ale domeniului original.

CNAME este folosit de obicei atunci cand vrem sa asociem un subdomeniu nou unei intrari A record deja existente. De exemplu, putem face "www.linuxtm.ro" in "linuxtm.ro", domeniu care ar trebui sa aiba deja alocata o adresa IP intr-un A record.

CNAME ne permite sa avem cate subdomenii dorim fara a fi nevoie sa specificam o adresa IP pentru fiecare intrare. Folositi CNAME daca aveti mai multe servicii care sunt directionate spre aceeasi adresa IP, astfel va trebui sa actualizati doar numele subdomeniului, fara a mai fi nevoie sa schimbati IP-ul.

<strong><em>Exemplu de CNAME Record</em></strong>
<pre>tutoriale.linuxtm.ro CNAME www.linuxtm.ro</pre>
Unde: 'www.linuxtm.ro' este un A record care intoarce o adresa IP, iar 'tutoriale.linuxtm.ro' directioneaza spre 'www.linuxtm.ro'.

De mentionat ar fi faptul ca CNAME nu poate face forward spre o anumita pagina web si nu trebuie folosit in intrarile MX (gen: mail.linuxtm.ro IN CNAME mail.linuxtm.com)

<strong>MX Record</strong>

O intrare MX (sau mail exchange record) specifica serverul de mail responsabil pentru acceptarea mailurilor pentru domeniul respectiv.

<em><strong>Exemplu de MX Record</strong></em>
<pre>linuxtm.ro. 14400 IN MX 0 linuxtm.ro.</pre>
Intrarea MX arata ca toate email-urile de la @linuxtm.ro ar trebui routate prin serverul de mail al "linuxtm.ro". Zona DNS arata ca linuxtm.ro este la adresa 176.223.207.45 , ceea ce inseamna ca email-urile pentru "test@linuxtm.ro" vor fi routate de catre serverul de mail localizat la adresa 176.223.207.45, iar aici se incheie treaba MX-ului, urmand ca serverul de mail de la adresa respectiva sa preieie mesajul si apoi sa-l distribuie la utilizatorul "test".

Este important ca in MX sa fie un punct dupa numele domeniului. In cazul in care punctul lipseste, routarea se face spre "linuxtm.ro.linuxtm.ro", Numarul 0 indica numarul de preferinta folosit de serverul de mail. Mail-ul este routat tot timpul spre serverul care are cel mai mic numar. Aceste valori preferentiale sunt utile in cazul in care avem mai multe servere de mail, si vrem sa stabilim prioritati: numarul cel mai mic avand cea mai mare prioritate. Daca avem un singur server de mail, se poate folosi "0" fara probeme.

<strong>PTR Record</strong>

O intrare PTR (sau pointer record) specifica o adresa IPv4 CNAME-ului acelui host. Configurarea uni PTR record pentru un hostname in domeniul <strong>in-addr.arpa</strong> ce corespunde unei adrese IP, implementeaza reverse DNS-ul pentru acea adresa. De exemplu www.linuxtm.ro are adresa IP 176.223.207.45m dar PTR-ul este 45.207.223.176.in-addr.arpa .

<em><strong>Exemple PTR Record</strong></em>
<pre>45.207.223.176.in-addr.arpa IN PTR linuxtm.ro</pre>
Dupa cum putem vedea, adresa IP este inversata si adaugata cu "in-addr.arpa".
PTR-ul este folosit in mare ca si masura de securitate si ca masura anti-spam, unde majoritatea serverelor web (sau email) verifica reverse DNS-ul (PTR) pentru a se asigura ca mail-ul provine intr-adevar de la host-ul de la care zice ca vine. Este recomandat sa avem tot timpul configurat PTR-ul daca avem un server de mail.

<strong>NS Record</strong>

Intrarile NS (sau name server record) aloca un nume de domeniu unei liste de servere autoritare DNS pentru acel domeniu. Nameserverele autoritare pentru un domeniu vor fi listate la <strong>Parent Server</strong>, iar acestea sunt numite "<strong>Delegation Records</strong>", acestea indicand delegarea domeniului la serverele autoritare.

NS-urile vor fi de asemenea listate la insusi  Serverul Autoritar al Nameserverelor, aceste intrari se numesc "<strong>Authoritative Records</strong>" (Intrari Autoritare).

Nameserverele care sunt configurate la Parent Server (la compania care a inregistrat domeniul) trebuie sa fie aceleasi ca si cele de pe Serverul Autoritar (pe serverul unde este configurata zona DNS).

<strong><em>Exemple de NS-uri cu sintaxa</em></strong>
<pre>linuxtm.ro. IN NS ns1.linuxtm.ro.</pre>
unde

<strong>IN</strong> indica internetul

<strong>NS</strong> indica tipul de intrare (name server)

In exemplul de mai sus, se arata ca <em>ns1.linuxtm.ro</em> este serverul autoritar pentru domeniul linuxtm.ro

<strong>SOA Record</strong>

SOA Record sau "start of authorithy" specifica serverul DNS care serveste informatia autoritara a unui domeniu de internet (.com, .ro, .net, etc), adresa de email a administratorului domeniului, serial number-ul si niste valori de timp referitor la reactualizarea zonei DNS.

SOA (State of Authority) Record este cea mai esentiala parte a zonei DNS, acesta fiind o forma prin care administratorul domeniului poate furniza informatii de baza despre domeniu, informatii precum: cat de des este actualizat, cand a fost actualizat ultima data, cand sa verifice din nou pentru informatii noi, care este adresa de email a administratorului s.a.m.d. O zona DNS poate contine doar un singur SOA Record.

Un SOA record optimizat si actualizat poate reduce utilizarea de banda intre nameservere, poate sa scurteze timpii de accesare a website-ului si se asigura ca site-ul este online chiar daca serverul DNS principal este cazut.

<em><strong>Exemple de SOA record cu sintaxa</strong></em>

Mai jos aveti un exmplu de SOA record. Retineti ca incepe cu paranteza deschisa "(" , aceasta trebuie sa fie pe aceeasi linie sau in caz contrar zona devine invalida.
<pre>; name TTL class rr Nameserver email-address
linuxtm.ro. 14400 IN SOA ns.linuxtm.ro. root.ns.linuxtm.ro. (
2004123001 ; Serial number
86000 ; Refresh rate in seconds
7200 ; Update Retry in seconds
3600000 ; Expiry in seconds
600 ; minimum in seconds )
</pre>
<strong>name</strong> - linuxtm.ro este numele principal in aceasta zona.

<strong>TTL</strong> - 14400 - TTL defineste durata in secunde pentru care intrarile DNS sa fie tinute in cache de catre clienti. Daca are valoarea 0, indica faptul ca zona DNS nu trebuie sa fie tinuta in cache. Se poate introduce orice valoare intre zero si 2147483647  (aproape 68 de ani!).

<strong>Class</strong> - IN - Clasa afiseaza tipul de intrare. IN inseamna Internet. Orice alte optiuni nu se mai folosesc in prezent. Atata timp cat zona DNS se afla pe internet, trebuie sa vedeti 'IN'.

<strong>Nameserver</strong> - ns.linuxtm.ro. - Nameserverul este serverul care tine fisierele aferente zonei DNS. Acesta poate fi un server extern, caz in care numele domeniului specificat trebuie urmat de un punct. In cazul in care este definit in fisierul acestei zone, atunci poate fi mentionat ca si 'ns'.

<strong>Email address</strong> - root.ns.linuxtm.ro. - Aceasta este adresa de mail a administratorului domeniului. Aici situatia se complica putin pentru ca oamenii de obicei se asteapta ca simbolul @ sa fie legat de o adresa de email. In acest caz insa, email-ul este trimis la <em>root@ns.linuxtm.ro</em>, dar este scris sub forma <em>root.ns.linuxtm.ro</em>  . De retinut este faptul ca trebuie pus punct dupa numele domeniului.

<strong>Serial number</strong> - 2004123001 - Serial number este un fel de sistem de revizuire a versiunilor zonei DNS. Acest numar este incremental, si se actualizeaza de fiecare data cand se efectueaza o modificare in zona DNS. Conventia standard este aceea de a folosi data actualizarii sub forma YYYYMMDDnn (an,luna,zi) , unde nn este numarul reviziei (asta in cazul in care se face mai multe modificari in zona dns in aceeasi zi). Astfel, daca prima actualizare facuta astazi are serial number-ul 2014270800 , urmatoarea va avea 2014270801.

<strong>Refresh</strong> - 86000 - Acesta valoare (exprimata in secunde) este durata in care zona DNS secundara (slave) verifica zona principala (master). Aceasta valoare determina cat de des se va prelua informatie din zona dns principala pentru a vedea daca serial numberu a crescut (astfel stie sa ceara o copie noua a zonei DNS). Valoarea poate fi trecuta sub forma '23:88M' , indicand 23 ore si 88 minute. De obicei valoarea este intre 6 si 24 ore.

<strong>Retry</strong> - 7200 - Presupunem ca o zona secundara a incercat sa contacteze zona principala si nu a reusit pentru ca a fost picata (offline). Valoarea de aici (in secunde) specifica timpul in care se va face o noua incercare. In general, aceasta valoare nu este foarte importanta si poate fi o fractiune din valoarea Refresh.

<strong>Expiry</strong> - 3600000 - Aceasta valoare (exprimata in secunde) este durata de timp in care zona DNS secundara va tine in cache zona valida in cazul in care nu se poate conecta la zona principala.Daca aceasta valoare este 2 saptamani, inseamna ca o zona dns secundara va putea furniza informatiile din cache timp de 2 saptamani, fara ca cineva sa observe vreo diferenta. Valoarea recomandata este intre 2 si 4 saptamani.

<strong>Minimum</strong> - 600 - Aceasta este valoarea implicita (exprimata in secunde) care stabileste durata de cache pentru zonele secundare. Aceasta este cea mai importanta valoare din SOA Record. Daca zona DNS se schimba constant, aceasta trebuie tinuta la o valoare mica, 1 zi sau chiar mai putin. Pe de alta parte, daca zona DNS este modificata mai rar, se poate pune intre 1 si 5 zile. Beneficiul unei valori mai mari este ca viteza site-ului va creste simtitor ca urmare a numarului scazut de interogari a zonei DNS. Serverele de cache din jurul lumii vor adauga in cache zona DNS si va imbunatati viteza site-ului.

<strong>SRV Record</strong>

Teoria din spatele SRV este aceea ca unui domeniu ( de exemplu, linuxtm.ro) ii se aloca un server web (http) care functioneaza prin tcp in cazul de fata, caz in care se va face o interogare a zonei DNS pentru a a afla hostname-ul domeniului - acesta fiind sau nu legat de numele domeniului (de exemplu: server1 , se poate pune orice hostname)

<strong><em>Exemple de SRV Record cu sintaxa</em></strong>

srvce.prot.name ttl class rr pri weight port target
_http._tcp.linuxtm.ro. IN SRV 0 5 80 www.linuxtm.ro.

<strong>srvce</strong>

Defineste simbolic numele serviciului precedat de ' _ ' (underscore) si este case-insensitive (nu tine cont de litera mare sau mica). Valori comune sunt:
<pre><strong>_http</strong> - server web
<strong>_ftp</strong> - serviciu de transfer fisiere
<strong>_ldap</strong> - serviciul LDAP
</pre>
<strong>prot</strong>

Defineste protocolul precedat de ' _ ' (underscore) si este case-insensitive (nu tine cont de litera mare sau mica). Valori comune sunt:
<pre><strong>_tcp</strong> - protocol TCP
<strong>_udp</strong> - protocol UDP</pre>
<strong>ttl</strong>

Parametru standard TTL (time to live)

<strong>pri</strong>

Prioritatea relativa a serviciului (intre 0 si 65535). Cel mai mic numar inseamna cea mai mare prioritate.

<strong>weight</strong>

Folosit pentru mai multe servicii care au aceeasi prioritata. Un intreg de 16 bits nesemnat intre 0 - 65535. Valoarea 0 (zero) indica faptul ca weight nu se aplica. Daca valoarea este 1 sau mai mare, se va livra de cele mai multe ori serviciul cu cel mai mare numar. De exemplu, avem <em>doua SRV records, ambele cu Priority = 0, una cu Weight = 1 si una cu Weight = 6</em>. Cea cu Weight = 6 va fi livrata de 6 ori din 7 de catre nameserver.

<strong>port</strong>

In mod normal portul este alocat serviciului insa nu este o necesitate. De exemplu, se poate configura _http pe portul 8888 si nu pe 80, cel standard.

<strong>target</strong>

Numele hostului care va oferi acest serviciu. Nu trebuie sa fie in aceeasi zona (a domeniului)

<strong>TXT Record</strong>

Un TXT record permite unui administrator sa insereze text arbitrar intr-o zona DNS. De exemplu, acest record este folosit pentru a defini SPF (Sender Policy Framework).

<strong><em>Exemple of TXT Record cu sintaxa</em></strong>

Domeniile care au configurat SPF trebuie sa publice cel putin doua directive: un identificator de versiune si un mecanism implicit.
<pre>linuxtm.ro. TXT "v=spf1 -all"</pre>
Acesta este cel mai eximplu SPF record posibil si inseama ca linuxtm.ro nu trimite niciodata email. Acest lucru face sens de exemplu daca domeniul este folosit doar pentru a gazdui o pagina web si nu foloseste email.

Serverele MX trimit mail, astfel ca ele trebuie desemnate.
<pre>linuxtm.ro. TXT "v=spf1 mx -all"</pre>
Sa pretindem ca linuxtm.ro are doua servere MX - mx01 si mx02, iar li se va permite ambelor sa trimita mail pentru linuxtm.ro . Daca sunt si alte servere catre trebuie sa trimita mail, si acestea trebuie mentionate:
<pre>linuxtm.ro. TXT "v=spf1 mx ptr -all"</pre>
Asta defineste ca toate hosturile ale caror PTR record potriveste cu linuxtm.ro sa poata trimite mail pentru linuxtm.ro
<pre>linuxtm.ro. TXT "v=spf1 a:linuxtm.ro mx ptr -all"</pre>
Adresa IP a linuxtm.ro nu apare in lista de servere MX, asa ca adaugam un mecanism "a" pentru a face potrivirea:
<pre>linuxtm.ro. TXT "v=spf1 a mx ptr -all"</pre>
Varianta de mai sus este o varianta mai scurta a aceluiasi lucru.

Fiecare server de mail ar trebui sa aiba si un SPF record configurat. Atunci cand serverul de mail creeaza mesaje bounce, ele vor fi trimise folosind un transmitator gol &lt;&gt;. Cand SPF MTA vede ca mesajul vine de la un astfel de trimitator, va face o interogare asupra numele domeniului folosind HELO. Intrarile de mai jos se ocupa de acest scenariu:
<pre>amx.mail.net. TXT "v=spf1 a -all"
mx.mail.net. TXT "v=spf1 a -all"
</pre>
Daca vreti sa verificati zone DNS, va recomand sa folositi:<a title="http://intodns.com/" href="http://intodns.com/" target="_blank"> http://intodns.com/</a>
