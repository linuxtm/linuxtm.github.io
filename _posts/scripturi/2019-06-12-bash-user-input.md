---
title: Bash user input
author: linuxtm
layout: post
permalink: /bash-user-input/
categories:
  - Scripturi
tags:
  - comenzi linux
  - tutoriale linux
  - scripturi linux
  - script bash
  - bash script user input
  - bash cere user input
---

<pre>
#!/bin/bash
#Require user input (select 1 or 2 on keyboard)

echo "Continue ?"
select yn in "Yes" "No"; do
    case $yn in
        Yes )

echo "The script has continued"
echo "some command 1"
echo "some command 2"
break;;

        No ) exit;;
    esac
done
</pre>
