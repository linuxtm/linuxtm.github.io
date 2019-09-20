---
title: Script generare parola puternica bash
author: linuxtm
layout: post
permalink: /generare-parola-puternica-bash/
categories:
  - Scripturi
tags:
  - comenzi linux
  - tutoriale linux
  - scripturi linux
  - script bash
  - generare parola puternica bash
  - script generare parole
  - bash script generate password
  - bash script parola generata
---

<pre>
#!/bin/bash
# Generate password that has guaranteed 1 lowecase, 1 uppercase, 1 special character, minimum 13 characters

function generatePass {
choose() { echo ${1:RANDOM%${#1}:1} $RANDOM; }
{
    choose '!@#$&'
    choose '0123456789'
    choose 'abcdefghijklmnopqrstuvwxyz'
    choose 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in $( seq 1 $(( 8 + RANDOM % 8 )) )
    do
        choose '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    done

} | sort -R | awk '{printf "%s",$1}'
echo ""
}

generatePass
</pre>
