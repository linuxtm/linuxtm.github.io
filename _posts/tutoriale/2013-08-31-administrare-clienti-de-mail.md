---
title: Administrare clienti de mail
author: linuxtm
layout: post
permalink: /administrare-clienti-de-mail/
categories:
  - Tutoriale
tags:
  - Administrare clienti de mail linux
  - comenzi exim
  - comenzi linux
  - comenzi linux exim
  - comenzi ssh exim
  - tutoriale linux
  - verificare coada de mesaje exim
  - verificare coada de mesaje postfix
  - verificare coada de mesaje sendmail
---
***Exim***

<table width="547" border="0">
  <tr>
    <td>
      <strong>exim -bpc</strong>
    </td>
    
    <td>
      afiseaza numarul de mesaje din coada (queue)
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>exim -bp</strong>
    </td>
    
    <td>
      afiseaza o lista cu mesajele din coada
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>exim -Mvl id</strong>
    </td>
    
    <td>
      afiseaza log-ul pentru un anumit mail (mail id)
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>exim -Mvh id</strong>
    </td>
    
    <td>
      afiseaza headerul unui mail
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>exim -Mvb id </strong>
    </td>
    
    <td>
      afiseaza body-ul unui mail
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>exim -Mrm id</strong>
    </td>
    
    <td>
      sterge un mail din coada
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>exim -qff</strong>
    </td>
    
    <td>
      sterge din coada de mesaje mesajele Frozen
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>exiwhat</strong>
    </td>
    
    <td>
      arata ce face exim-ul in momentul de fata
    </td>
  </tr>
  
  <tr>
    <td>
      <strong> exiqgrep -f [user]@domeniu</strong>
    </td>
    
    <td>
      cauta in coada de mesaje doar un anumit sender
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>exim -bp | exiqgrep -i | xargs exim -Mrm</strong>
    </td>
    
    <td>
      goleste toata coada de mesaje
    </td>
  </tr>
</table>

***Sendmail***

<table width="547" border="0">
  <tr>
    <td>
      <strong>mailq</strong>
    </td>
    
    <td>
      afiseaza o lista a mesajelor din coada
    </td>
  </tr>
  
  <tr>
    <td>
      <strong>mailq|grep ^[a-z0-9]|wc -l</strong>
    </td>
    
    <td>
      afiseaza nr total de mesaje din coada (fara a mai afisa lista)
    </td>
  </tr>
</table>

***Postfix</em>**</p> 

<table width="547" border="0">
  <tr>
    <td>
      <strong>find /var/spool/postfix/{deferred,active,maildrop}/ -type f | wc -l</strong>
    </td>
    
    <td>
      verifica coada de mesaje
    </td>
  </tr>
  
  <tr>
    <td>
      <strong> </strong>
    </td>
    
    <td>
    </td>
  </tr>
</table>