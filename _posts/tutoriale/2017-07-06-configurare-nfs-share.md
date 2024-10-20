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

```bash
yum install nfs-utils
```

Facem un director pe care il vom exporta pe clienti:
```bash
mkdir /nfsshare
```

Pornim serviciile si le configuram sa porneasca la boot:
```bash
systemctl enable rpcbind \
systemctl enable nfs-server \
systemctl enable nfs-lock \
systemctl enable nfs-idmap \
systemctl start rpcbind \
systemctl start nfs-server \
systemctl start nfs-lock \
systemctl start nfs-idmap
```

In continuare expunem in retea folderul NFS. Cu editorul preferat, deschidem <em>/etc/exports</em> si adaugam dupa cum urmeaza:

```bash
/storage 192.168.1.1(rw,insecure,nohide,no_root_squash,sync) 192.168.1.2(rw,insecure,nohide,no_root_squash,sync)
```

Mai sus am expus serverul NFS catre cei 2 clienti (192.168.1.1 si 192.168.1.2). 
Pentru ca share-ul sa functioneze, asigurati-va ca serverele sunt accesibile intre ele (ping).
Daca doriti sa expuneti serverul de NFS in retea spre orice IP, se poate folosi: "*" 

In continuare, pornim serviciul NFS:
```bash
systemctl restart nfs-server 
```

<strong>2. Instalarea pe client </strong>

Instalam nfs-utils:
```bash
yum install nfs-utils
```

Creem directorul unde vom monta NFS-ul:
```bash
mkdir /nfsshare
```

Pornim serviciile si le configuram sa porneasca la boot:
```bash
systemctl enable rpcbind \
systemctl enable nfs-server \
systemctl enable nfs-lock \
systemctl enable nfs-idmap \
systemctl start rpcbind \
systemctl start nfs-server \
systemctl start nfs-lock \
systemctl start nfs-idmap
```

In continuare montam NFS-ul pe clienti:
```bash
mount -t nfs 192.168.1.0:/nfsshare /nfsshare
```

Acum ar trebui sa avem un server de NFS functional, montat pe clienti.
Verificare o putem face ruland comanda: 
```bash
df -h
```
