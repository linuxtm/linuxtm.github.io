---
title: Adauga automat vhost-uri cu SSL
author: linuxtm
layout: post
permalink: /adauga-automat-vhost-uri-cu-ssl/
categories:
  - Tutoriale
tags:
  - apache
  - automatizare
  - scripturi bash
  - scripturi linux
  - vhost
  - vhost-ssl
---
Daca data trecuta am prezentat un script care [adauga automat vhost-uri][1], de data asta va prezint scriptul care adauga automat vhosturi si genereaza certificat SSL self signed. Aceast script este util in cazul in care serverul tau nu are panou de control gen cPanel, DirectAdmin, Plesk, etc. Scriptul se executa in acelasi fel ca cel care adauga doar vhost-uri, adica prin executarea comenzii: . vhost-ssl.sh domeniu.tld sau . vhost-ssl.sh subdomeniu.domeniu.tld

```bash
#!/bin/bash   

vhost=$1  
if [[ -z &#8220;$vhost&#8221; ]]; then  
echo &#8220;Usage bash vhost.sh domain.tld or sub.domain.tld&#8221;  
exit 1;  
else  
echo &#8220;Your domain is $vhost&#8221;  
fi

echo &#8220;Please enter the IP address on which the SSL cert will be installed&#8221;  
echo &#8220;if none entered, the script will configure the vhost with the default&#8221;  
echo &#8220;IP address on which the apache webserver is running!&#8221;  
read -p &#8220;Enter IP address or hit Enter to contiune > &#8221; IP

if [[ $IP < 1 ]] ; then  
host=&#8221;*&#8221;  
else  
host=$IP  
fi

mkdir /var/www/$vhost  
mkdir /var/www/$vhost/htdocs  
mkdir /var/www/$vhost/cgi-bin  
mkdir /var/www/$vhost/logs  
mkdir /var/www/$vhost/ssl-cert  
a2enmod ssl  
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /var/www/$vhost/ssl-cert/$vhost.key -out /var/www/$vhost/ssl-cert/$vhost.crt

if [ ! -f /etc/apache2/conf.d/virtual.conf ]; then  
mkdir /var/www/default  
touch /etc/apache2/conf.d/virtual.conf  
echo &#8220;#&#8221; > /etc/apache2/conf.d/virtual.conf  
echo &#8220;# We&#8217;re running multiple virtual hosts.&#8221; >> /etc/apache2/conf.d/virtual.conf  
echo &#8220;#&#8221; >> /etc/apache2/conf.d/virtual.conf  
echo &#8220;<VirtualHost *:80>&#8221; >> /etc/apache2/conf.d/virtual.conf  
echo -e &#8220;\tServerAdmin root@localhost&#8221; >> /etc/apache2/conf.d/virtual.conf  
echo -e &#8220;\tDocumentRoot /var/www/default&#8221; >> /etc/apache2/conf.d/virtual.conf  
echo &#8220;</VirtualHost>&#8221; >> /etc/apache2/conf.d/virtual.conf  
fi

echo &#8220;#&#8221; >> /etc/apache2/sites-available/$vhost  
echo &#8220;# $vhost (/etc/apache2/sites-available/$vhost)&#8221; >> /etc/apache2/sites-available/$vhost  
echo &#8220;#&#8221; >> /etc/apache2/sites-available/$vhost  
echo &#8220;<IfModule mod_ssl.c>&#8221; >> /etc/apache2/sites-available/$vhost  
echo &#8220;<VirtualHost $host:443>&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tServerAdmin admin@$vhost&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tServerName $vhost:443&#8243; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tServerAlias www.$vhost:443&#8243; >> /etc/apache2/sites-available/$vhost  
echo &#8220;&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t# Indexes + Directory Root.&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tDirectoryIndex index.php index.html&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tDocumentRoot /var/www/$vhost/htdocs/&#8221; >> /etc/apache2/sites-available/$vhost  
echo &#8220;&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t# CGI Directory&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tScriptAlias /cgi-bin/ /var/www/$vhost/cgi-bin/&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t<Location /cgi-bin>&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t\tOptions +ExecCGI&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t</Location>&#8221; >> /etc/apache2/sites-available/$vhost  
echo &#8220;&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t# Logfiles&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tErrorLog /var/www/$vhost/logs/error.log&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tCustomLog /var/www/$vhost/logs/access.log combined&#8221; >> /etc/apache2/sites-available/$vhost  
echo &#8220;&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t<FilesMatch \&#8221;\.(cgi|shtml|phtml|php)$\&#8221;>&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t\tSSLOptions +StdEnvVars&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t</FilesMatch>&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t<Directory /usr/lib/cgi-bin>&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t\tSSLOptions +StdEnvVars&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t</Directory>&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tBrowserMatch \&#8221;MSIE [2-6]\&#8221; \\&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t\tnokeepalive ssl-unclean-shutdown \\&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\t\tdowngrade-1.0 force-response-1.0&#8243; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tBrowserMatch \&#8221;MSIE [17-9]\&#8221; ssl-unclean-shutdown&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tSSLEngine on&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tSSLCertificateFile /var/www/$vhost/ssl-cert/$vhost.crt&#8221; >> /etc/apache2/sites-available/$vhost  
echo -e &#8220;\tSSLCertificateKeyFile /var/www/$vhost/ssl-cert/$vhost.key&#8221; >> /etc/apache2/sites-available/$vhost  
echo &#8220;</VirtualHost>&#8221; >> /etc/apache2/sites-available/$vhost  
echo &#8220;</IfModule>&#8221; >> /etc/apache2/sites-available/$vhost

#generating a new index file  
echo &#8220;<html xmlns=\&#8221;http://www.w3.org/1999/xhtml\&#8221; xml:lang=\&#8221;en\&#8221; lang=\&#8221;en\&#8221;><head>&#8221; > /var/www/$vhost/htdocs/index.html  
echo &#8220;<title>$vhost &mdash; Coming Soon</title>&#8221; >> /var/www/$vhost/htdocs/index.html  
echo &#8220;<meta http-equiv=\&#8221;Content-Type\&#8221; content=\&#8221;text/html; charset=UTF-8\&#8221;/>&#8221; >> /var/www/$vhost/htdocs/index.html  
echo &#8220;<meta name=\&#8221;description\&#8221; content=\&#8221;This is a default index page for a new domain.\&#8221;/>&#8221; >> /var/www/$vhost/htdocs/index.html  
echo &#8220;<style type=\&#8221;text/css\&#8221;>&#8221; >> /var/www/$vhost/htdocs/index.html  
echo &#8220;<center>h1 {font-size:64px; color:#555555; margin: 70px 0 50px 0;}<center>&#8221; >> /var/www/$vhost/htdocs/index.html  
echo &#8220;</style>&#8221; >> /var/www/$vhost/htdocs/index.html  
echo &#8220;</head>&#8221; >> /var/www/$vhost/htdocs/index.html  
echo &#8220;<body>&#8221; >> /var/www/$vhost/htdocs/index.html  
echo &#8220;<h1>$vhost</h1>&#8221; >> /var/www/$vhost/htdocs/index.html  
echo &#8220;</body>&#8221; >> /var/www/$vhost/htdocs/index.html  
echo &#8220;</html>&#8221; >> /var/www/$vhost/htdocs/index.html

a2ensite $vhost  
/etc/init.d/apache2 reload  
echo &#8220;Your website $vhost is up and running&#8221;
```
