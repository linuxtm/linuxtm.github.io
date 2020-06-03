---
title: Toate serviciile AWS
author: linuxtm
layout: post
permalink: /servicii-aws/
categories:
  - AWS
tags:
  - comenzi linux
  - tutoriale aws
  - lista servicii aws
  - comenzi utile aws cli
  - aws linie comanda
  - toate serviciile oferite de aws
  - lista servicii amazon
  - tutoriale aws cli
  - tutoriale aws cloud
---

<br>
<strong><em>Compute</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>EC2</td>
      <td>Virtual Private Servers</td>
    </tr>
    <tr>
      <td>Lightsail</td>
      <td>Amazon’s hosting provider (vps, dns, storage)</td>
    </tr>
    <tr>
      <td>Lambda</td>
      <td>Functions you can run, written in Python, NodeJS, Go etc. Can run many in parallel.</td>
    </tr>
    <tr>
      <td>Batch</td>
      <td>Run software jobs in Docker containers on EC2 machines</td>
    </tr>
    <tr>
      <td>Elastic Beanstalk</td>
      <td>Run software on managed virtual machines</td>
    </tr>
    <tr>
      <td>Serverless Application Repository</td>
      <td>Repository of serverless applications that you can deploy (on lambda)</td>
    </tr>
    <tr>
      <td>AWS Outposts</td>
      <td>Run Amazon services in your own data center</td>
    </tr>
    <tr>
      <td>EC2 Image Builder</td>
      <td>Create EC2 (ami?) images automatically</td>
    </tr>
</table>

<br>
<strong><em>Storage</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>S3</td>
      <td>File storage. Not directly used for mounting, but you can directly download files from HTTP.</td>
    </tr>
    <tr>
      <td>EFS</td>
      <td>NFS. Mount network disks to your machines.</td>
    </tr>
    <tr>
      <td>FSx</td>
      <td>Windows / Lustre filesystems you can connect to your EC2 machines</td>
    </tr>
    <tr>
      <td>S3 Glacier</td>
      <td>Low cost storage system for backups and archives and such</td>
    </tr>
    <tr>
      <td>Storage Gateway</td>
      <td>iSCSI so you can connect S3 to your own (remote) machine.</td>
    </tr>
    <tr>
      <td>AWS Backup</td>
      <td>Automatically create backups of different AWS service (EC2, rds etc)</td>
    </tr>
</table>

<br>
<strong><em>Database</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>RDS</td>
      <td>Managed mysql, postgres databases etc.</td>
    </tr>
    <tr>
      <td>DynamoDB</td>
      <td>Large &amp; scalable non-relational database</td>
    </tr>
    <tr>
      <td>ElastiCache</td>
      <td>Managed memcache and redis machines</td>
    </tr>
    <tr>
      <td>Neptune</td>
      <td>Graph database</td>
    </tr>
    <tr>
      <td>Amazon Redshift</td>
      <td>Warehousing. Store lots of data that can be processed through streams.</td>
    </tr>
    <tr>
      <td>Amazon QLDB</td>
      <td>Database for immutable and cryptographically verifiable data (money transactions etc)</td>
    </tr>
    <tr>
      <td>Amazon DocumentDB</td>
      <td>MongoDB clone (but not really compatible anymore)</td>
    </tr>
    <tr>
      <td>Amazon Keyspaces</td>
      <td>Managed Apache Cassandra clone</td>
    </tr>
</table>

<br>
<strong><em>Migration & Transfer</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>AS Migration Hub</td>
      <td>Migrate things from your DC to AWS</td>
    </tr>
    <tr>
      <td>Application Discovery Service</td>
      <td>Discover services in your datacenter</td>
    </tr>
    <tr>
      <td>Database Migration Service</td>
      <td>Migrate databases to RDS while staying online (can convert structures as well)</td>
    </tr>
    <tr>
      <td>Server Migration Service</td>
      <td>Migrate virtual machines to amazon.</td>
    </tr>
    <tr>
      <td>AWS Transfer Family</td>
      <td>(s)FTP service with S3 backend. Upload to FTP, directly store on S3 bucket.</td>
    </tr>
    <tr>
      <td>Snowball</td>
      <td>Get a machine from AWS, plug in your DC, transfer data fast to AWS, return machine</td>
    </tr>
    <tr>
      <td>DataSync</td>
      <td>Sync data between your datacenter and AWS</td>
    </tr>
</table>

<br>
<strong><em>Networking & Content Delivery</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>VPC</td>
      <td>Create your own virtual private network within AWS.</td>
    </tr>
    <tr>
      <td>CloudFront</td>
      <td>Content Delivery Network.</td>
    </tr>
    <tr>
      <td>Route 53</td>
      <td>Manage domain names and records.</td>
    </tr>
    <tr>
      <td>API Gateway</td>
      <td>Create HTTP APIs and let them connect to different backends.</td>
    </tr>
    <tr>
      <td>Direct Connect</td>
      <td>Create a (physical) connection between you (or DC) to AWS.</td>
    </tr>
    <tr>
      <td>AWS App Mesh</td>
      <td>Automatically run Envoy as a sidecar for your containers (ECS or EKS).</td>
    </tr>
    <tr>
      <td>AWS Cloud Map</td>
      <td>Service discovery for your containers.</td>
    </tr>
    <tr>
      <td>Global Accelerator</td>
      <td>Run your app on edge locations so they are closer to your customers (CDN for apps).</td>
    </tr>
</table>

<br>
<strong><em>Developer Tools</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>CodeStar</td>
      <td>Quickly develop applications by using template code and codecommit, codebuild etc</td>
    </tr>
    <tr>
      <td>CodeCommit</td>
      <td>Amazon source repositories (git repo’s etc)</td>
    </tr>
    <tr>
      <td>CodeBuild</td>
      <td>CI service</td>
    </tr>
    <tr>
      <td>CodeDeploy</td>
      <td>Deployment service</td>
    </tr>
    <tr>
      <td>CodePipeline</td>
      <td>Code delivery with workflows</td>
    </tr>
    <tr>
      <td>Cloud9</td>
      <td>Online IDE</td>
    </tr>
    <tr>
      <td>X-Ray</td>
      <td>Allows tracing in your applications, supports Python, NodeJs, Go etc.</td>
    </tr>
</table>

<br>
<strong><em>Robotics</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>AWS RoboMaker</td>
      <td>Cloud solution for robotic developers to simulate, test and securely deploy robotic applications</td>
    </tr>
</table>

<br>
<strong><em>Containers</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Elastic Container Registry</td>
      <td>Store docker images like on DockerHub</td>
    </tr>
    <tr>
      <td>Elastic Container Service</td>
      <td>Run containers, either on your own EC2 machines, or on managed machines called Fargate.</td>
    </tr>
    <tr>
      <td>Elastic Kubernetes Service</td>
      <td>Kubernetes as a service</td>
    </tr>
</table>

<br>
<strong><em>Management & Governance</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>AWS Organizations</td>
      <td>Configure (sub)organisations and accounts</td>
    </tr>
    <tr>
      <td>CloudWatch</td>
      <td>Logging from various AWS components</td>
    </tr>
    <tr>
      <td>AWS Auto Scaling</td>
      <td>Scale resources based on your custom inputs and rules</td>
    </tr>
    <tr>
      <td>CloudFormation</td>
      <td>Templates to create and configure AWS components (think terraform/sls)</td>
    </tr>
    <tr>
      <td>CloudTrail</td>
      <td>Figure out who did what in your AWS services</td>
    </tr>
    <tr>
      <td>Config</td>
      <td>Audit the configurations of your AWS resources</td>
    </tr>
    <tr>
      <td>OpsWorks</td>
      <td>Use Ansible to automate stuff</td>
    </tr>
    <tr>
      <td>Service Catalog</td>
      <td>Manage list of items/codes etc you have in the cloud</td>
    </tr>
    <tr>
      <td>Systems Manager</td>
      <td>View data from your resources grouped in ways you like (like application specific etc)</td>
    </tr>
    <tr>
      <td>AWS AppConfig</td>
      <td>Store and publish application configuration data</td>
    </tr>
    <tr>
      <td>Trusted Advisor</td>
      <td>Checks your account for issues (costs, performance, security etc)</td>
    </tr>
    <tr>
      <td>Control Tower</td>
      <td>Manage multi-accounts</td>
    </tr>
    <tr>
      <td>AWS License Manager</td>
      <td>Manage licenses</td>
    </tr>
    <tr>
      <td>AWS Well-Architected Tool</td>
      <td>Generate questionnaires about your architecture to see if you follow best practices</td>
    </tr>
    <tr>
      <td>Personal Health Dashboard</td>
      <td>StatusPage for AWS</td>
    </tr>
    <tr>
      <td>AWS Chatbot</td>
      <td>Connect AWS to slack</td>
    </tr>
    <tr>
      <td>Launch Wizard</td>
      <td>Deploy MSSQL or SAP</td>
    </tr>
    <tr>
      <td>AWS Compute Optimizer</td>
      <td>Finds your resources and advices on how to save costs</td>
    </tr>
</table>

<br>
<strong><em>Media Services</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Elastic Transcoder</td>
      <td>Encode files from S3 into different other formats and store back at S3</td>
    </tr>
    <tr>
      <td>Kinesis Video Streams</td>
      <td>Capture media streams</td>
    </tr>
    <tr>
      <td>MediaConnect</td>
      <td>?</td>
    </tr>
    <tr>
      <td>MediaConvert</td>
      <td>Convert media into different formats</td>
    </tr>
    <tr>
      <td>MediaLive</td>
      <td>Share live video with many others</td>
    </tr>
    <tr>
      <td>MediaPackage</td>
      <td>?</td>
    </tr>
    <tr>
      <td>MediaStore</td>
      <td>?</td>
    </tr>
    <tr>
      <td>MediaTailor</td>
      <td>Insert advertisements into your broadcasts</td>
    </tr>
    <tr>
      <td>Elemental Appliances &amp; Software</td>
      <td>create videos on-premise. Basically a mix of all of the above services. Seems expensive. Probably is.</td>
    </tr>
</table>

<br>
<strong><em>Machine Learning</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Amazon SageMaker</td>
      <td>Machine learning tools</td>
    </tr>
    <tr>
      <td>Amazon CodeGuru</td>
      <td>Profile java code with machine learning</td>
    </tr>
    <tr>
      <td>Amazon Comprehend</td>
      <td>Understand and classify data like emails, tweets etc</td>
    </tr>
    <tr>
      <td>Amazon Forecast</td>
      <td>Create forecasts from data</td>
    </tr>
    <tr>
      <td>Amazon Fraud Detector</td>
      <td>in preview so no idea.</td>
    </tr>
    <tr>
      <td>Amazon Kendra</td>
      <td>Search service where you can ask questions</td>
    </tr>
    <tr>
      <td>Amazon Lex</td>
      <td>Create voice and chatbots</td>
    </tr>
    <tr>
      <td>Amazon Machine Learning</td>
      <td>Deprecated. Use SageMaker instead.</td>
    </tr>
    <tr>
      <td>Amazon Personalize</td>
      <td>Create personalized recommendations based on data (mahout??)</td>
    </tr>
    <tr>
      <td>Amazon Polly</td>
      <td>Convert text to speech in different languages</td>
    </tr>
    <tr>
      <td>Amazon Rekognition</td>
      <td>Recognize objects and people in images</td>
    </tr>
    <tr>
      <td>Amazon Textract</td>
      <td>Convert text found in images to text (OCR)</td>
    </tr>
    <tr>
      <td>Amazon Transcribe</td>
      <td>Convert audio to text</td>
    </tr>
    <tr>
      <td>Amazon Translate</td>
      <td>Translates text from one language to another</td>
    </tr>
    <tr>
      <td>AWS DeepLens</td>
      <td>A video camera that does machine learning</td>
    </tr>
    <tr>
      <td>AWS DeepRacer</td>
      <td>Some kind of game where you program a racecar to race against others.</td>
    </tr>
    <tr>
      <td>Amazon Augmented AI</td>
      <td>Let humans in the loop to make AI learn things better</td>
    </tr>
    <tr>
      <td>AWS DeepComposer</td>
      <td>Computer generated music. It’s as horrible as it sounds.</td>
    </tr>
</table>

<br>
<strong><em>Analytics</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Athena</td>
      <td>Query data stored in S3 buckets.</td>
    </tr>
    <tr>
      <td>EMR</td>
      <td>Elastic Map/Reduce</td>
    </tr>
    <tr>
      <td>CloudSearch</td>
      <td>AWS version of managed document search system (like elasticsearch)</td>
    </tr>
    <tr>
      <td>Elasticsearch Service</td>
      <td>Elasticsearch as a service</td>
    </tr>
    <tr>
      <td>Kinesis</td>
      <td>Collect massive amount of data so you can do analytics (like ELK?)</td>
    </tr>
    <tr>
      <td>QuickSight</td>
      <td>Business Intelligence service</td>
    </tr>
    <tr>
      <td>Data Pipeline</td>
      <td>Move and transform data to dynamodb, rds, S3 etc.</td>
    </tr>
    <tr>
      <td>AWS Data Exchange</td>
      <td>Find APIs which data you can consume, which can be very expensive</td>
    </tr>
    <tr>
      <td>AWS Glue</td>
      <td>ETL service. Enrich, validate data.</td>
    </tr>
    <tr>
      <td>AWS Lake Formation</td>
      <td>Create data lakes</td>
    </tr>
    <tr>
      <td>MSK</td>
      <td>Kafka as a service</td>
    </tr>
</table>

<br>
<strong><em>Security, Identity, &amp; Compliance</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>IAM</td>
      <td>AWS’s permission system that can control users and AWS services.</td>
    </tr>
    <tr>
      <td>Resource Access Manager</td>
      <td>Share certain AWS resources like Route53, licenses, EC2 with other accounts.</td>
    </tr>
    <tr>
      <td>Cognito</td>
      <td>User and password management system. Useful for managing users for your applications.</td>
    </tr>
    <tr>
      <td>Secrets Manager</td>
      <td>Secrets key/value store. Can automatically rotate secrets.</td>
    </tr>
    <tr>
      <td>GuardDuty</td>
      <td>Automatically scan your cloudtrail/vpc logs for threats.</td>
    </tr>
    <tr>
      <td>Inspector</td>
      <td>Automatically find (security) issues in your network and machines.</td>
    </tr>
    <tr>
      <td>Amazon Macie</td>
      <td>Analyzes data in your S3 buckets and check for PII data.</td>
    </tr>
    <tr>
      <td>AWS Single Sign-On</td>
      <td>Allow single-sign on to your applications.</td>
    </tr>
    <tr>
      <td>Certificate Manager</td>
      <td>Manage and even create (free) SSL certificates.</td>
    </tr>
    <tr>
      <td>Key Management Service</td>
      <td>Manage secret keys</td>
    </tr>
    <tr>
      <td>CloudHSM</td>
      <td>Hardware security modules. Allows you to generate and operate on cryptographic keys.</td>
    </tr>
    <tr>
      <td>Directory Service</td>
      <td>Active directory as a service</td>
    </tr>
    <tr>
      <td>WAF &amp; Shield</td>
      <td>Web Application Firewall (for loadbalancers, cloudfront, api gateway). Can setup your own rules or use predefined ones</td>
    </tr>
    <tr>
      <td>AWS Firewall Manager</td>
      <td>Firewall manager for different accounts in your organisation</td>
    </tr>
    <tr>
      <td>Artifact</td>
      <td>Documents for cloud compliance (things like 27001 certification etc)</td>
    </tr>
    <tr>
      <td>Security Hub</td>
      <td>Overall security checker that uses guardduty, inspector, macie etc</td>
    </tr>
    <tr>
      <td>Detective</td>
      <td>Log  security issues found (from security hub etc)</td>
    </tr>
</table>

<br>
<strong><em>Mobile</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>AWS Amplify</td>
      <td>Let AWS automatically generate frontend &amp; backend apps and deploy them automatically.</td>
    </tr>
    <tr>
      <td>Mobile Hub</td>
      <td>Part of AWS Amplify now.</td>
    </tr>
    <tr>
      <td>AWS AppSync</td>
      <td>Create API backends that you can connect to. Can be created through AWS Amplify as well.</td>
    </tr>
    <tr>
      <td>Device Farm</td>
      <td>AWS BrowserStack. Automatically test apps on many different mobile devices and browsers.</td>
    </tr>
</table>

<br>
<strong><em>Application Integration</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Step Functions</td>
      <td>State machines written in amazon’s own language</td>
    </tr>
    <tr>
      <td>Amazon AppFlow</td>
      <td>Automatically connects apps together (zapier?). For instance: slack to S3 buckets.</td>
    </tr>
    <tr>
      <td>Amazon EventBridge</td>
      <td>Some kind of eventbus system</td>
    </tr>
    <tr>
      <td>Amazon MQ</td>
      <td>ActiveMQ</td>
    </tr>
    <tr>
      <td>Simple Notification Service</td>
      <td>Notification system that can notify through email, api endpoints, sms etc.</td>
    </tr>
    <tr>
      <td>Simple Queue Service</td>
      <td>Message queue system</td>
    </tr>
    <tr>
      <td>SWF</td>
      <td>Create workflows.</td>
    </tr>
</table>

<br>
<strong><em>AWS Cost Management</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>AWS Cost Explorer</td>
      <td>Gives an overview and projection of your budgets</td>
    </tr>
    <tr>
      <td>AWS Budgets</td>
      <td>Create budgets for your AWS components</td>
    </tr>
    <tr>
      <td>AWS Marketplace Subscriptions</td>
      <td>Find (and buy) AMI’s with software installed</td>
    </tr>
</table>

<br>
<strong><em>Customer Engagement</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Amazon Connect</td>
      <td>AWS call center platform</td>
    </tr>
    <tr>
      <td>Pinpoint</td>
      <td>Create transactional emails, SMS or voice calls based on templates.</td>
    </tr>
    <tr>
      <td>Simple Email Service</td>
      <td>Send out emails. Email provider.</td>
    </tr>
</table>

<br>
<strong><em>Business Applications</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Alexa for Business</td>
      <td>Connect Alexa to your business needs.</td>
    </tr>
    <tr>
      <td>Amazon Chime</td>
      <td>AWS version of Zoom.</td>
    </tr>
    <tr>
      <td>WorkMail</td>
      <td>AWS version of Gmail / Calendar.</td>
    </tr>
</table>
<br>
<strong><em>End User Computing</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>WorkSpaces</td>
      <td>Virtual desktops from Windows or Linux.</td>
    </tr>
    <tr>
      <td>AppStream 2.0</td>
      <td>Stream applications running native onto your browser</td>
    </tr>
    <tr>
      <td>WorkDocs</td>
      <td>Store your documents and manage them online.</td>
    </tr>
    <tr>
      <td>WorkLink</td>
      <td>Connect mobile users to your intranet.</td>
    </tr>
</table>

<br>
<strong><em>Internet of Things</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>IoT Core</td>
      <td>Manage fleets of IOT devices through MQTT broker</td>
    </tr>
    <tr>
      <td>FreeRTOS</td>
      <td>RTOS operating system for microcontrollers to automatically connect to IOT-Core or greengrass.</td>
    </tr>
    <tr>
      <td>IoT 1-Click</td>
      <td>Manage 1-click buttons that can be connected to other systems like Lambda</td>
    </tr>
    <tr>
      <td>IoT Analytics</td>
      <td>Clean up and save messages from topics into a data-store for analytics</td>
    </tr>
    <tr>
      <td>IoT Device Defender</td>
      <td>Detect unwanted issues on your devices and take actions</td>
    </tr>
    <tr>
      <td>IoT Device Management</td>
      <td>Organize IoT devices into groups, schedule jobs on the devices and configure remote access</td>
    </tr>
    <tr>
      <td>IoT Events</td>
      <td>Monitor telemetry from devices and then trigger other AWS services or jobs on the devices themselves</td>
    </tr>
    <tr>
      <td>IoT Greengrass</td>
      <td>A message broker can buffer messages for groups of up to 200 devices which can communicate and process data locally if connectivity to IoT Core is intermittent.</td>
    </tr>
    <tr>
      <td>IoT SiteWise</td>
      <td>Collect, organize, analyze and visualize data from industrial equipment at scale</td>
    </tr>
    <tr>
      <td>IoT Things Graph</td>
      <td>Cloudformation-like designer for graphing how devices should communicate with other AWS services</td>
    </tr>
</table>

<br>
<strong><em>Game Development</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Amazon GameLift</td>
      <td>Deploy game servers with low latency on AWS</td>
    </tr>
</table>

<br>
<strong><em>Blockchain</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Amazon Managed Blockchain</td>
      <td>Block chains</td>
    </tr>
</table>

<br>
<strong><em>AR & VR</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Amazon Sumerian</td>
      <td>Create and run browser-based 3D, AR and VR applications.</td>
    </tr>
</table>

<br>
<strong><em>Satellite</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Ground Station</td>
      <td>Timeshare radios and large antennas pointed at space</td>
    </tr>
</table>

<br>
<strong><em>Quantum Technologies</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>Amazon Braket</td>
      <td>Some quantum thing. It’s in preview so I have no idea what it is.</td>
    </tr>
</table>

<br>
<strong><em>Customer Enablement</em></strong>
<br>
<table width="100%" border="0">
    <tr>
      <td>AWS IQ</td>
      <td>Job board: Hire AWS experts for whatever you need.</td>
    </tr>
    <tr>
      <td>Support</td>
      <td>AWS support center</td>
    </tr>
    <tr>
      <td>Managed Services</td>
      <td>Let AWS handle your AWS services for you.</td>
    </tr>
</table>
