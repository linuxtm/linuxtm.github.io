---
title: Export zona DNS din Route53 intr-un fisier
author: linuxtm
layout: post
permalink: /aws-export-route53/
categories:
  - AWS
tags:
  - comenzi linux
  - tutoriale aws
  - aws cli route53
  - aws export dns zone cli
  - export zona dns din route53 amazon
  - comenzi utile aws cli
  - aws linie comanda
  - tutoriale aws cli
  - tutoriale aws cloud
---

Scriptul de mai jos ia ca argument regiunea AWS in care se afla zona DNS in AWS si o exporta intr-un fisier.

Nota: Este necesar sa aveti utilitarul ***jq*** instalat, folosit pentru parsarea outpt-ului json.

```bash
#!/bin/bash
zonename=$1
hostedzoneid=$(aws route53 list-hosted-zones --output json | jq -r ".HostedZones[] | select(.Name == \"$zonename.\") | .Id" | cut -d'/' -f3)
aws route53 list-resource-record-sets --hosted-zone-id $hostedzoneid --output json | jq -jr '.ResourceRecordSets[] | "\(.Name) \t\(.TTL) \t\(.Type) \t\(.ResourceRecords[]?.Value)\n"'
```
