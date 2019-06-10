---
title: Configurare server NFS pe Centos 7
author: linuxtm
layout: post
permalink: /configurare-server-nfs-centos7/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - configurare share nfs
  - nfs share tutorial
  - configurare share retea
  - share nfs retea tutorial
  - share nfs centos7
  - server nfs centos7
---

In acest tutorial vom crea un share NFS (Centos 7) pe care il vom monta pe 2 servere diferite.
Serverul de NFS va avea IP-ul: 192.168.1.0
Clientii vor avea IP-urile: 192.168.1.1 si 192.168.1.2


<strong>1. Instalarea pe server </strong>

Incepem cu instalarea nfs-utils:

<pre>
yum install nfs-utils
</pre>

Facem un director pe care il vom exporta pe clienti:
<pre>
mkdir /nfsshare
</pre>

Pornim serviciile si le configuram sa porneasca la boot:
<pre>
systemctl enable rpcbind \
systemctl enable nfs-server \
systemctl enable nfs-lock \
systemctl enable nfs-idmap \
systemctl start rpcbind \
systemctl start nfs-server \
systemctl start nfs-lock \
systemctl start nfs-idmap
</pre>

In continuare expunem in retea folderul NFS. Cu editorul preferat, deschidem <em>/etc/exports</em> si adaugam dupa cum urmeaza:

<pre>
/storage 192.168.1.1(rw,insecure,nohide,no_root_squash,sync) 192.168.1.2(rw,insecure,nohide,no_root_squash,sync)
</pre>

Mai sus am expus serverul NFS catre cei 2 clienti (192.168.1.1 si 192.168.1.2). 
Pentru ca share-ul sa functioneze, asigurati-va ca serverele sunt accesibile intre ele (ping).
Daca doriti sa expuneti serverul de NFS in retea spre orice IP, se poate folosi: "*" 

In continuare, pornim serviciul NFS:
<pre>
systemctl restart nfs-server 
</pre>

<strong>2. Instalarea pe client </strong>

Instalam nfs-utils:
<pre>
yum install nfs-utils
</pre>

Creem directorul unde vom monta NFS-ul:
<pre>
mkdir /nfsshare
</pre>

Pornim serviciile si le configuram sa porneasca la boot:
<pre>
systemctl enable rpcbind \
systemctl enable nfs-server \
systemctl enable nfs-lock \
systemctl enable nfs-idmap \
systemctl start rpcbind \
systemctl start nfs-server \
systemctl start nfs-lock \
systemctl start nfs-idmap
</pre>

In continuare montam NFS-ul pe clienti:
<pre>
mount -t nfs 192.168.1.0:/nfsshare /nfsshare
</pre>

Acum ar trebui sa avem un server de NFS functional, montat pe clienti.
Verificare o putem face ruland comanda: 
<pre>
df -h
</pre>

