---
title: Comenzi uzuale
author: linuxtm
layout: page
tags:
- comenzi linux
- comenzi ubuntu
- cele mai folosite comenzi linux
- administrare linux
- comenzi uzuale linux
---
Pentru informatii suplimentare referitor la utilizarea comenzilor cititi descrierea acestora sau folositi <em>man comanda</em> in terminal pentru a afisa manualul de ajutor pentru comanda specificata.
Mai jos aveti cateva din comenzile folosite cel mai frecvent.
<br>
<br>
<strong><em>Administrare pachete</em></strong>
<br>
 
<table width="100%" border="0">
 <tr>
 <td>
 <strong>apt-get install <em>pachet</em></strong>
 </td>
 <td>
 cauta si instaleaza pachete software (Debian/Ubuntu)
 </td>
 </tr>
<tr>
<td>
<strong>apt-get update</strong>
</td>
<td>
cauta si face update pachetelor software (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>apt-get upgrade</strong>
</td>
<td>
instaleaza update-urile disponibile (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>apt-get dist-upgrade</strong>
</td>
<td>
instaleaza update-uri si rezolva dependinte (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>apt-get remove</strong>
</td>
<td>
sterge pachete software (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>apt-get autoremove</strong>
</td>
<td>
sterge pachete software de care nu mai este nevoie (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>apt-get --purge remove</strong>
</td>
<td>
sterge complet un pachet
</td>
</tr>
<tr>
<td>
<strong>apt-cache search <em>pachet</em></strong>
</td>
<td>
cauta pachete software disponibile in repository-urile instalate (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>apt-cache show <em>pachet</em></strong>
</td>
<td>
afiseaza informatii despre un pachet (Debian/Ubuntu)
</td>
</tr>
 <tr>
<td>
<strong>apt-cache showpkg <em>pachet</em></strong>
</td>
<td>
afiseaza dependintele si repository-ul din care provine un packet (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>dpkg -l</strong>
</td>
<td>
afiseaza toate pachetele instalate (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>dpkg -l | grep <em>pachet</em></strong>
</td>
<td>
cauta un anume pachet in pachetele instalate (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>dpkg -L <em>pachet</em></strong>
</td>
<td>
afiseaza unde este instalat pachetul specificat (ex: <em>dpkg -L apache2</em> (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>dpkg -s <em>pachet</em></strong>
</td>
<td>
afiseaza statusul unui pachet (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>dpkg --get-selections > 1.txt</strong>
</td>
<td>
scrie intr-un fisier toate pachetele instalate (Debian/Ubuntu)
</td>
</tr>
 <tr>
 <td>
 <strong>yum install <em>pachet</em></strong>
 </td>
 <td>
 instaleaza pachete software(Centos/RHEL)
 </td>
 </tr>
 <tr>
 <td>
 <strong>yum remove <em>pachet</em></strong>
 </td>
 <td>
 sterge pachete software(Centos/RHEL)
 </td>
 </tr>
 <tr>
 <td>
 <strong>yum update</strong>
 </td>
 <td>
 actualizeaza toate pachetele (se pot actualiza si doar anumite pachete, <em>yum update pachet </em>(Centos/RHEL)
 </td>
 </tr>
 <tr>
 <td>
 <strong>yum update --exclude=kernel*</strong>
 </td>
 <td>
 actualizeaza toate pachetele cu exceptia pachetelor care tin de Kernel (Centos/RHEL)
 </td>
 </tr>
 <tr>
 <td>
 <strong>yum list <em>pachet</em></strong>
 </td>
 <td>
 cauta anumite pachete (Centos/RHEL)
 </td>
 </tr>
 <tr>
 <td>
 <strong>yum search <em>pachet</em></strong>
 </td>
 <td>
cauta toate pachetele disponibile cu numele specificat (Centos/RHEL)
 </td>
 </tr>
 <tr>
 <td>
 <strong>yum info <em>pachet</em></strong>
 </td>
 <td>
afiseaza informatii despre pachetul specificat (Centos/RHEL)
 </td>
 </tr>
 <tr>
 <td>
 <strong>yum list installed</strong>
 </td>
 <td>
afiseaza pachetele software instalate (Centos/RHEL)
 </td>
 </tr>
 <tr>
 <td>
 <strong>yum check-update</strong>
 </td>
 <td>
verifica daca sunt update-uri disponibile (Centos/RHEL)
 </td>
 </tr>
 <tr>
 <td>
 <strong>yum repolist</strong>
 </td>
 <td>
afiseaza repo-urile (sursele) active pe sistem (Centos/RHEL)
 </td>
 </tr>
<tr>
<td>
<strong>rpm -ivh <em>fisier.rpm</em></strong>
</td>
<td>
Instaleaza pachet (Centos/RHEL)
</td>
</tr>
<tr>
<td>
<strong>rpm -Uvh <em>fisier.rpm</em></strong>
</td>
<td>
Face upgrade pachetului (Centos/RHEL)
</td>
</tr>
<tr>
<td>
<strong>rpm -ev <em>pachet</em></strong>
</td>
<td>
Sterge un pachet instalat (Centos/RHEL)
</td>
</tr>
<tr>
<td>
<strong>rpm -ev --nodeps <em>pachet</em></strong>
</td>
<td>
Sterge un pachet instalat fara sa verifice dependintele (Centos/RHEL)
</td>
</tr>
<tr>
<td>
<strong>rpm -qa <em>pachet</em></strong>
</td>
<td>
Afiseaza o lista cu toate pachetele instalate (Centos/RHEL)
</td>
</tr>
<tr>
<td>
<strong>rpm -qi <em>pachet</em></strong>
</td>
<td>
Afiseaza informatii despre un pachet - versiune si descriere scurta (Centos/RHEL)
</td>
</tr>
<tr>
<td>
<strong>rpm -qf <em>/cale/spre/fisier</em></strong>
</td>
<td>
Identifica pachetul din care a provenit fisierul (Centos/RHEL)
</td>
</tr>
<tr>
<td>
<strong>rpm -qc <em>nume pachet</em></strong>
</td>
<td>
Afiseaza o lista cu fisierele de configurare unui pachet (Centos/RHEL)
</td>
</tr>
<tr>
<td>
<strong>rpm -qcf <em>/cale/spre/fisier</em></strong>
</td>
<td>
Afiseaza o lista cu fisierele de configurare a unei comenzi (Centos/RHEL)
</td>
</tr>
<tr>
<td>
<strong>rpm -qa --last</strong>
</td>
<td>
Afiseaza o lista cu ultimele rpm-uri instalate (Centos/RHEL)
</td>
</tr>
<tr>
<td>
<strong>rpm -qpR <em>rpm</em></strong>
</td>
<td>
Afla dependintele unui .rpm (Centos/RHEL)
</td>
</tr>
<tr>
<td>
<strong>rpm -qR <em>pachet</em></strong>
</td>
<td>
Afla dependintele unui pachet (Centos/RHEL)
</td>
</tr>

</table>

 <br>
<strong><em>Administrare procese si servicii</em></strong>
<br>
 
<table width="100%" border="0">
<tr>
<td>
<strong>top</strong>
</td>
<td>
afiseaza procesele active (<strong>Shift+M</strong> &#8211; sorteaza dupa memoria utilizata, <strong>Shift+P</strong> dupa CPU)
</td>
</tr>
<tr>
<td>
<strong>kill <em>PID</em></strong>
</td>
<td>
termina un proces selectat (PID-ul este afisat in top)
</td>
</tr>
<tr>
<td>
<strong>kill -9 <em>PID</em></strong>
</td>
<td>
termina fortat un proces
</td>
</tr>
<tr>
<td>
<strong>killall <em>serviciu</em></strong>
</td>
<td>
termina toate procesele unui serviciu (ex: <em>killall httpd</em> sau <em>killall /etc/php/php-fpm</em>)
</td>
</tr>
<tr>
<td>
<strong>pkill <em>serviciu</em></strong>
</td>
<td>
la fel ca si <em>killall</em>, termina procese dupa numele acestora (se poate folosi oricare)
</td>
</tr>
<tr>
<td>
<strong>service <em>nume</em> start/stop</strong>
</td>
<td>
porneste/opreste un serviciu (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>systemctl start/stop <em>serviciu</em></strong>
</td>
<td>
porneste/opreste un serviciu (Centos7/RHEL7)
</td>
</tr>
<tr>
<td>
<strong>systemctl restart <em>serviciu</em></strong>
</td>
<td>
reporneste un serviciu (Centos7/RHEL7)
</td>
</tr>
<tr>
<td>
<strong>service <em>nume</em> restart</strong>
</td>
<td>
restarteaza un serviciu (Debian/Ubuntu)
</td>
</tr>
<tr>
<td>
<strong>ps aux</strong>
</td>
<td>
afiseaza toate procesele care ruleaza si locatia acestora + detalii (user, pid, etc)
</td>
</tr>
<tr>
<td>
<strong>ps aux | grep <em>proces</em></strong>
</td>
<td>
afiseaza doar un anumit proces (ex: <em>ps aux | grep apache</em> )
</td>
</tr>
<tr>
<td>
<strong>lsof | grep <em>user</em></strong>
</td>
<td>
afiseaza toate procesele rulate de un anumit utilizator
</td>
</tr>
<tr>
<td>
<strong>lsof -n | grep IP</strong>
</td>
<td>
afiseaza ce procese fac conexiuni spre IP-ul destinatie (de ex: script ce floodeaza)
</td>
</tr>
<tr>
<td>
<strong>lsof -p PID</strong>
</td>
<td>
afiseaza fisierele folosite de procesul respectiv
</td>
</tr>
<tr>
<td>
<strong>Ctrl+C</strong>
</td>
<td>
termina sarcina curenta
</td>
</tr>
</table>

 
<br>
<strong>Nota: </strong>pentru start/stop/restart serviciu se poate utiliza si: <em>/etc/init.d/serviciu optiune</em> (exceptie Centos7/RHEL7).
<br>
<br>
<strong><em>Administrare fisiere si navigare</em></strong>
<br>
 
<table width="100%" border="0">
<tr>
<td>
<strong>cat <em>fisier</em></strong>
</td>
<td>
afiseaza continutul unui fisier (ex: <em>cat /etc/passwd</em> )
</td>
</tr>
<tr>
<td>
<strong>cp <em>sursa/dest</em> </strong>
</td>
<td>
copiaza fisiere sau directoare (ex: <em>cp /home/user/fisier /home/user2/fisier</em>
</td>
</tr>
<tr>
<td>
<strong>cp -r <em>sursa/dest</em> </strong>
</td>
<td>
copiaza recursiv fisiere (ex: <em>cp -r /home/u1/* /home/u2/</em> &#8211; copiaza toate fisierele din u1 in u2 )
</td>
</tr>
<tr>
<td>
<strong>cp <em>fisier1 fisier2</em> </strong>
</td>
<td>
copiaza fisier1 in fisier2 (ex: <em>cp fisier.txt fisier2.txt</em> )
</td>
</tr>
<tr>
<td>
<strong>mv <em>fisier</em> </strong>
</td>
<td>
muta/redenumeste fisiere (se foloseste la fel ca si <strong>cp</strong>. ex: <em>mv fisier.txt fisier2.txt</em> )
</td>
</tr>
<tr>
<td>
<strong>rm <em>fisier</em></strong>
</td>
<td>
sterge fisiere sau directoare (ex: <em>rm /var/log/auth.log</em> )
</td>
</tr>
<tr>
<td>
<strong>rm -rf <em>fisier</em></strong>
</td>
<td>
sterge fortat fisiere/directoare (ex: <em>rm -rf /var/log/*</em> &#8211; sterge tot din directorul log)
</td>
</tr>
<tr>
<td>
<strong>rm -rf <em>*test*</em></strong>
</td>
<td>
sterge fortat (din directorul curent) toate fisierele/directoarele care contin cuvantul &#8216;test&#8217;
</td>
</tr>
<tr>
<td>
<strong>rmdir <em>director</em></strong>
</td>
<td>
sterge directoare goale (care nu contin niciun fisier)
</td>
</tr>
<tr>
<td>
<strong>ls</strong>
</td>
<td>
afiseaza continutul unui director (ex: <em>ls /var/log</em> )
</td>
</tr>
<tr>
<td>
<strong>ls -l</strong>
</td>
<td>
afiseaza continutul directorului curent cu permisiunile acestuia
</td>
</tr>
<tr>
<td>
<strong>ll</strong>
</td>
<td>
afiseaza continutul directorului curent (alternativa mai simpla pentru <em>ls -l</em>)
</td>
</tr>
<tr>
<td>
<strong>ln -s <em>sursa/dest</em></strong>
</td>
<td>
creaza link-uri simbolice (ex: <em>ln -s /home/user/fisier1 /home/fisier1</em>
</td>
</tr>
<tr>
<td>
<strong>chmod <em>optiune</em></strong>
</td>
<td>
schimba permisiunile unui fisier / director (ex: <em>chmod 755 /home/user/public_html</em> )
</td>
</tr>
<tr>
<td>
<strong>chown <em>optiune</em></strong>
</td>
<td>
schimba proprietarul unor fisiere/directoare (ex: <em>chown user fisier.txt</em> )
</td>
</tr>
<tr>
<td>
<strong>cd <em>locatie</em></strong>
</td>
<td>
navigheaza spre un director dat (ex: <em>cd /var/log/apache/</em> )
</td>
</tr>
<tr>
<td>
<strong>cd ..</strong>
</td>
<td>
navigheaza un director inapoi (ex: <em>cd ../../../</em> &#8211; navigheaza 3 directoare inapoi )
</td>
</tr>
<tr>
<td>
<strong> > <em>fisier</em></strong>
</td>
<td>
sterge continutul unui fisier (ex: <em>> /var/log/auth.log</em> )
</td>
</tr>
<tr>
<td>
<strong>wc -l <em>fisier</em></strong>
</td>
<td>
afiseaza numarul de linii dintr-un fisier
</td>
</tr>
<tr>
<td>
<strong>tail <em>-x fisier</em></strong>
</td>
<td>
afiseaza ultimele x randuri din fisier (ex: <em>tail -10 /var/log/auth.log</em> )
</td>
</tr>
<tr>
<td>
<strong>tail -f <em>fisier</em></strong>
</td>
<td>
afiseaza continut pe masura ce sunt adaugate linii in fisier
</td>
</tr>
<tr>
<td>
<strong>mkdir <em>nume</em></strong>
</td>
<td>
creaza un director (ex: <em>mkdir documente</em> )
</td>
</tr>
<tr>
<td>
<strong>mkdir -p {test/1,test/2}</strong>
</td>
<td>
creaza folderul <em>test</em> si in interiorul lui folderul <em>1</em> si <em>2</em>
</td>
</tr>

<tr>
<td>
<strong>pwd</strong>
</td>
<td>
afiseaza directorul curent (in care ne aflam)
</td>
</tr>
<tr>
<td>
<strong>touch</strong>
</td>
<td>
creaza un fisier gol (ex: <em>touch index.html</em> )
</td>
</tr>
<tr>
<td>
<strong>tar -zcvf </strong>
</td>
<td>
arhiveaza un director intreg (ex: <em>tar -zcvf nume.tar.gz /home/user/director</em> )
</td>
</tr>
<tr>
<td>
<strong>tar -zxvf</strong>
</td>
<td>
dezarhiveaza o arhiva (ex: <em>tar -zxvf arhiva.tar.gz -C /root</em> dezarhiveaza in directorul /root)
</td>
</tr>
<tr>
<td>
<strong>find / -name nume</strong>
</td>
<td>
cauta fisiere (ex: <em>find /home -name text</em> cauta in /home fisierele numite text)
</td>
</tr>
<tr>
<td>
<strong>locate <em>nume</em></strong>
</td>
<td>
localizeaza fisiere (ex: <em>locate mysql</em> )
</td>
</tr>
</table>
 
<br>
<strong><em>Monitorizare, informatii despre sistem si resurse</em></strong>
<br>
 
<table width="100%" border="0">
<tr>
<td>
<strong>free -m</strong>
</td>
<td>
afiseaza memoria ram libera (nota: memoria libera este cea afisata pe randul: <em><strong>-/+ buffers/cache:</strong></em> )
</td>
</tr>
<tr>
<td>
<strong>vmstat</strong>
</td>
<td>
afiseaza activitatea sistemului, hardware si informatii despre sistem
</td>
</tr>
<tr>
<td>
<strong>df -h</strong>
</td>
<td>
afiseaza spatiul utilizat pe disk intr-un format uman (poate fi citit usor)
</td>
</tr>
<tr>
<td>
<strong>du -hs</strong>
</td>
<td>
afiseaza spatiul total utilizat de directorul curent
</td>
</tr>
<tr>
<td>
<strong>du -hs *</strong>
</td>
<td>
afiseaza spatiul utilizat de fiecare fisier din directorul curent
</td>
</tr>
<tr>
<td>
<strong>w</strong>
</td>
<td>
afiseaza utilizatorii logati si procesele acestora (ex: <em>w user</em> )
</td>
</tr>
<tr>
<td>
<strong>uptime</strong>
</td>
<td>
afiseaza uptime-ul serverului (de cand este pornit)
</td>
</tr>
<tr>
<td>
<strong>uname -a</strong>
</td>
<td>
afiseaza informatii despre sistem, informatii despre kernel
</td>
</tr>
<tr>
<td>
<strong>who</strong>
</td>
<td>
afiseaza toti userii logati
</td>
</tr>
<tr>
<td>
<strong>whoami</strong>
</td>
<td>
afiseaza userul cu care esti logat
</td>
</tr>
<tr>
<td>
<strong>cat /proc/cpuinfo</strong>
</td>
<td>
afiseaza informatii despre procesor
</td>
</tr>
<tr>
<td>
<strong>cat /proc/mounts</strong>
</td>
<td>
afiseaza toate fisierele de sisteme montate
</td>
</tr>
</table>
 
<br>
<strong><em>Retea si DNS</em></strong>
<br>
 
<table width="100%" border="0">
<tr>
<td>
<strong>ping</strong>
</td>
<td>
foloseste protocolul ICMP pentru a comunica cu un host (verifica daca acesta raspunde la cereri ICMP)
</td>
</tr>
<tr>
<td>
<strong>mtr</strong>
</td>
<td>
monitorizeaza pachetele trimise catre un host (ex: <em>mtr linuxtm.ro</em> )
</td>
</tr>
<tr>
<td>
<strong>traceroute</strong>
</td>
<td>
afiseaza informatii despre toate hop-urile prin care trec pachetele pana la un host (ex: <em>traceroute linuxtm.ro</em> )
</td>
</tr>
<tr>
<td>
<strong>dig</strong>
</td>
<td>
interogheaza nameserverele unui host (ex: <em>dig linuxtm.ro</em> )
</td>
</tr>
<tr>
<td>
<strong>whois</strong>
</td>
<td>
afiseaza informatii despre un host (ex: <em>whois linuxtm.ro</em> )
</td>
</tr>
<tr>
<td>
<strong>netstat -ant</strong>
</td>
<td>
afiseaza toate conexiunile (active si inactive) cu hostname-urile rezolvate (afiseaza IP-urile)
</td>
</tr>
<tr>
<td>
<strong>netstat -ap</strong>
</td>
<td>
afiseaza toate conexiunile (active si inactive) si procesele aferente
</td>
</tr>
<tr>
<td>
<strong>ifconfig</strong>
</td>
<td>
afiseaza configuratia interfetei de retea (afiseaza si IP-urile alocate)
</td>
</tr>
<tr>
<td>
<strong>tcpdump -nn</strong>
</td>
<td>
afiseaza tot traficul si rezolva hostname-urile (afiseaza IP-urile)
</td>
</tr>
</table>
 
