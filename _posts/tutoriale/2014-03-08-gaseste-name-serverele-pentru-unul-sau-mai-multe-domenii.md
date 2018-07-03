---
title: Gaseste name serverele pentru unul sau mai multe domenii
author: linuxtm
layout: post
permalink: /gaseste-name-serverele-pentru-unul-sau-mai-multe-domenii/
categories:
  - Tutoriale
tags:
  - bash
  - dig
  - scripting
  - scripturi
  - scripturi linux
---
In acest articol veti gasi un script care automatizeaza gasirea serverelor NS pentru unul sau mai multe domenii. Output-ul este exportat intr-un fisier de forma output.PID ( ex: output.3242 ). Scriptul primeste 1 argument care poate fi un nume de domeniu sau un fisier care contine mai multe nume de domenii.  
De retinut. In fisier trebuie trecut 1 domeniu per linie.  
Utilizarea scriptului este urmatoarea . findNS.sh domeniu.tld sau . findNS lista.txt

<pre>#!/bin/bash
#
# This script will find the nameservers allocated to one or more domains.
# Ca be used with one argument a domain name or a file containing domains.
# This script is released under CC BY-SA copyright terms.
#

if [ $# -lt 1 ] ; then
echo "Usage *script* domain.tld or file.txt"
exit 0;
fi

_dom_=$1
_file_=output.$$
_dig_=`hash dig`
_found_dig_=`$dig | grep "not found"`

if [ ! -z $_found_dig_ ] ; then
echo "In order to use this script please install dig"
exit 0;
fi

if [ -f $_dom_ ] ; then
_dom_to_check_=`cat $_dom_`
else
_dom_to_check_=$_dom_
fi

function checkNS () {
for i in $_dom_to_check_
do
echo $i &gt;&gt; $_file_
dig NS $i | grep -v ";" | grep -v '^[[:space:]]*$' | awk '{print $5}' &gt;&gt; $_file_
done
}

checkNS
echo "The generated file is $_file_"</pre>

De asemenea scriptul poate fi descarcat de pe site-ul kode.wlan0.ru din linia de comanda executand:

<pre>wget kode.wlan0.ru/x/findNS.sh</pre>
