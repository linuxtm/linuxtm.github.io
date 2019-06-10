---
title: Configurare backup-uri cu rsnapshot
author: linuxtm
layout: post
permalink: /configurare-backup-rsnapshot/
categories:
  - Tutoriale
tags:
  - comenzi linux
  - tutoriale linux
  - configurare backup
  - rsnapshot tutorial
  - backup rsnapshot
  - backupuri cu rsnapshot
  - rsnapshot centos7
  - tutorial backup server rsnapshot
  - rsnapshot notificatri mail
  - rsync backup mail
  - rsnapreport.pl send email
---

**1. Instalare dependinte**
<pre>
yum install -y rsnapshot mailx postfix wget
systemctl start postfix && systemctl enable postfix
wget -O /usr/local/bin/rsnapreport.pl https://raw.githubusercontent.com/rsnapshot/rsnapshot/master/utils/rsnapreport.pl && chmod +x /usr/local/bin/rsnapreport.pl
</pre>

**2. Configurare rsnapshot.conf**

<em>Nota: folositi tab-uri in loc de spatii in configul rsnapshot, altfel nu va functiona.</em>

Pentru a primi pe mail statisticile de la rsnapshot, trebuie decomentate urmatoarele comenzi in <em>/etc/rsnapshot.conf</em>
<ul>
<li>cmd_cp</li>
<li>cmd_rm</li>
<li>cmd_rsync</li>
<li>cmd_logger</li>
<li>cmd_du</li>
<li>cmd_ssh (daca backup-ul are loc pe un alt server)</li>
</ul>

<strong>Intervalul la care sa se efectueze backup-urile:</strong>
<pre>
#########################################
#     BACKUP LEVELS / INTERVALS         #
# Must be unique and in ascending order #
# e.g. alpha, beta, gamma, etc.         #
#########################################

interval        daily   7
interval        weekly  4
interval        monthly 12
</pre>

<strong>Nivelul de detalii dorit:</strong>
<pre>
# Verbose level, 1 through 5.
# 1     Quiet           Print fatal errors only
# 2     Default         Print errors and warnings only
# 3     Verbose         Show equivalent shell commands being executed
# 4     Extra Verbose   Show extra verbose information
# 5     Debug mode      Everything
#
verbose         4

# Same as "verbose" above, but controls the amount of data sent to the
# logfile, if one is being used. The default is 3.
#
loglevel        4
</pre>

<strong>Argumentele necesare pentru rsync:</strong>
<pre>
# Default rsync args. All rsync commands have at least these options set.
#
#rsync_short_args       -a
rsync_long_args --stats --delete --numeric-ids --relative --delete-excluded
</pre>

<strong>Locatiile de backup dorite:</strong>
<pre>
###############################
### BACKUP POINTS / SCRIPTS ###
###############################
#backup local
backup  /home/          home/
backup  /etc/           etc/
#backup local baza de date
backup_script   /usr/bin/mysqldump --single-transaction -A --routines --triggers -u root -p'parola'| gzip > database-`date +%y%m%d`.sql.gz     mysql/
#exemplu backup db remote
#backup_script   /usr/bin/ssh user@IP -p 22 "rm -f /backups/mysql-*.sql.gz;/usr/bin/mysqldump -A --routines --triggers --events -u root | gzip > /backups/mysql-`date +%y%m%d`.sql.
</pre>

**3. Testare email + config rsnapshot**

<pre>
echo "test" | mail -E -r "from@linuxtm.ro" -s "Daily Backup" to@linuxtm.ro
rsnapshot -t daily
</pre>

**4. Configurare cron**

Cronurile de mai jos vor face backup zilnic (ora 00:40), saptamanal (ora 02:10), si lunar (ora 04:10 , in prima zi a lunii)
<pre>
40 0 * * * root /usr/bin/rsnapshot daily 2>&1 | /usr/local/bin/rsnapreport.pl | mail -E -r from@linuxtm.ro -s "Daily Backup" to@linuxtm.ro
10 2 * * 1 root /usr/bin/rsnapshot weekly 2>&1 | /usr/local/bin/rsnapreport.pl | mail -E -r from@linuxtm.ro -s "Weekly Backup" to@linuxtm.ro
10 4 1 * * root /usr/bin/rsnapshot monthly 2>&1 | /usr/local/bin/rsnapreport.pl | mail -E -r from@linuxtm.ro -s "Monthly Backup" to@linuxtm.ro
</pre>

