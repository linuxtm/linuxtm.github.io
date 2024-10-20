---
title: Instalare Java 8 pe Centos 7 (64biti)
author: linuxtm
layout: post
permalink: /instalare-java8-centos7/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - instalare java 8 centos 7
  - instalare java8 rpm
  - java8 rpm centos
  - tutoriale linux
---
Se poate instala ruland comenzile de mai jos.
```bash
wget --no-cookies \
--no-check-certificate \
--header "Cookie: oraclelicense=accept-securebackup-cookie" \
"http://download.oracle.com/otn-pub/java/jdk/8u73-b02/jdk-8u73-linux-x64.rpm" \
-O jdk-8u73-linux-x64.rpm
````
Dupa ce downloadam rpm-ul, rulam:
```bash
rpm -Uvh jdk-8u73-linux-x64.rpm
```
Verificam versiunea de java:
```bash
java -version
```
<em>
<br>java version "1.8.0_73" 
<br>Java(TM) SE Runtime Environment (build 1.8.0_73-b02) 
<br>Java HotSpot(TM) 64-Bit Server VM (build 25.73-b02, mixed mode)
</em>
