
Scenarios Taxonomy
==================
  

|Name|Label|Description|Behaviors|Mitre ATT&CK|CVES|Spoofable|Confidence|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|crowdsecurity/CVE-2019-18935|Telerik Cve-2019-18935 Exploitation Attempts|Detect Telerik CVE-2019-18935 exploitation attempts||||0|0|
|crowdsecurity/CVE-2021-4034|Cve-2021-4034 Exploits|Detect CVE-2021-4034 exploits||||0|0|
|crowdsecurity/CVE-2022-26134|Cve-2022-26134 Exploits|Detect CVE-2022-26134 exploits||||0|0|
|crowdsecurity/CVE-2022-35914|Cve-2022-35914 Exploits|Detect CVE-2022-35914 exploits||||0|0|
|crowdsecurity/CVE-2022-37042|Cve-2022-37042 Exploits|Detect CVE-2022-37042 exploits||||0|0|
|crowdsecurity/fortinet-cve-2022-40684|Cve-2022-40684 Exploitation Attempts|Detect cve-2022-40684 exploitation attempts||||0|0|
|crowdsecurity/CVE-2022-41082|Cve-2022-41082 Exploits|Detect CVE-2022-41082 exploits||||0|0|
|crowdsecurity/CVE-2022-41697|Cve-2022-41697 Enumeration|Detect CVE-2022-41697 enumeration||||0|0|
|crowdsecurity/CVE-2022-42889|Cve-2022-42889 Exploits (text4shell)|Detect CVE-2022-42889 exploits (Text4Shell)||||0|0|
|crowdsecurity/CVE-2022-44877|Cve-2022-44877 Exploits|Detect CVE-2022-44877 exploits||||0|0|
|crowdsecurity/CVE-2022-46169-bf|Cve-2022-46169 Brute Forcing|Detect CVE-2022-46169 brute forcing||||0|0|
|crowdsecurity/CVE-2022-46169-cmd|Cve-2022-46169 CMD Injection|Detect CVE-2022-46169 cmd injection||||0|0|
|crowdsecurity/CVE-2023-23397|Cve-2023-23397 From Sysmon Events|Detect CVE-2023-23397 from sysmon events||||0|0|
|crowdsecurity/apache_log4j2_cve-2021-44228|Log4j CVE-2021-44228|Detect cve-2021-44228 exploitation attemps|http:exploit|TA0043:T1595
TA0001:T1190|CVE-2021-44228|0|3|
|crowdsecurity/asterisk_bf|Asterisk User Bruteforce|Detect asterisk user bruteforce||||0|0|
|crowdsecurity/asterisk_user_enum|Asterisk User Enum Bruteforce|Detect asterisk user enum bruteforce||||0|0|
|crowdsecurity/auditd-base64-exec-behavior|Post-exploitation Behaviour : Base64 + Interpreter (perl/bash/python)|Detect post-exploitation behaviour : base64 + interpreter (perl/bash/python)||||0|0|
|crowdsecurity/auditd-postexploit-exec-from-net|Post-exploitation Behaviour : Curl/wget AND Exec|Detect post-exploitation behaviour : curl/wget and exec||||0|0|
|crowdsecurity/auditd-postexploit-pkill|Post-exploitation Behaviour : Pkill ExeCVE Bursts|Detect post-exploitation behaviour : pkill execve bursts||||0|0|
|crowdsecurity/auditd-postexploit-rm|Post-exploitation Behaviour : RM ExeCVE Bursts|Detect post-exploitation behaviour : rm execve bursts||||0|0|
|crowdsecurity/auditd-sus-exec|Post-exploitation Behaviour : Exec From Suspicious Locations|Detect post-exploitation behaviour : exec from suspicious locations||||0|0|
|crowdsecurity/aws-cis-benchmark-cloudtrail-config-change|AWS Cloudtrail Configuration Change|Detect AWS CloudTrail configuration change||||0|0|
|crowdsecurity/aws-cis-benchmark-config-config-change|AWS Config Configuration Change|Detect AWS Config configuration change||||0|0|
|crowdsecurity/aws-cis-benchmark-console-auth-fail|AWS Console Authentication Failure|Detect AWS console authentication failure||||0|0|
|crowdsecurity/aws-cis-benchmark-iam-policy-change|AWS IAM Policy Change|Detect AWS IAM policy change||||0|0|
|crowdsecurity/aws-cis-benchmark-kms-deletion|AWS KMS KEY Deletion|Detect AWS KMS key deletion||||0|0|
|crowdsecurity/aws-cis-benchmark-login-no-mfa|Login Without MFA TO THE AWS Console|Detect login without MFA to the AWS console||||0|0|
|crowdsecurity/aws-cis-benchmark-nacl-change|AWS Nacl Change|Detect AWS NACL change||||0|0|
|crowdsecurity/aws-cis-benchmark-ngw-change|AWS Network Gateway Change|Detect AWS Network Gateway change||||0|0|
|crowdsecurity/aws-cis-benchmark-root-usage|AWS Root Account Usage|Detect AWS root account usage||||0|0|
|crowdsecurity/aws-cis-benchmark-route-table-change|AWS Route Table Change|Detect AWS route table change||||0|0|
|crowdsecurity/aws-cis-benchmark-s3-policy-change|AWS S3 Bucket Policy Change|Detect AWS S3 bucket policy change||||0|0|
|crowdsecurity/aws-cis-benchmark-security-group-change|AWS Security Group Change|Detect AWS Security Group change||||0|0|
|crowdsecurity/aws-cis-benchmark-unauthorized-call|AWS API Unauthorized Calls|Detect AWS API unauthorized calls||||0|0|
|crowdsecurity/aws-cis-benchmark-vpc-change|AWS VPC Change|Detect AWS VPC change||||0|0|
|crowdsecurity/ban-defcon-drop_range|BAN A Range IF More Than 5 IPS From IT ARE Banned AT A Time|Ban a range if more than 5 ips from it are banned at a time||||0|0|
|crowdsecurity/cpanel-bf-attempt|Bruteforce Attempt ON Cpanel Login|Detect bruteforce attempt on cpanel login||||0|0|
|crowdsecurity/cpanel-bf|Bruteforce ON Cpanel Login|Detect bruteforce on cpanel login||||0|0|
|crowdsecurity/dovecot-spam|Errors ON Dovecot|detect errors on dovecot||||0|0|
|crowdsecurity/endlessh-bf|SSH Bruteforce Caught BY Endlessh|Detect SSH bruteforce caught by Endlessh||||0|0|
|crowdsecurity/exchange-bf|Exchange Bruteforce (smtp,imap,pop3)|Detect exchange bruteforce (SMTP,IMAP,POP3)||||0|0|
|crowdsecurity/exim-bf|Exim Brute Force|Detect Exim brute force||||0|0|
|crowdsecurity/exim-user-bf|Exim User Email Brute Force|Detect Exim user email brute force||||0|0|
|crowdsecurity/exim-spam|Spam ON Exim|detect spam on Exim||||0|0|
|crowdsecurity/f5-big-ip-cve-2020-5902|Cve-2020-5902 Exploitation Attemps|Detect cve-2020-5902 exploitation attemps||||0|0|
|crowdsecurity/fortinet-cve-2018-13379|Cve-2018-13379 Exploitation Attemps|Detect cve-2018-13379 exploitation attemps||||0|0|
|crowdsecurity/freeswitch-acl-reject|Freeswitch ACL Rejects|Detect freeswitch acl rejects||||0|0|
|crowdsecurity/freeswitch-bf|Freeswitch Auth Bruteforce|Detect freeswitch auth bruteforce||||0|0|
|crowdsecurity/freeswitch-slow-bf|Freeswitch Auth Bruteforce|Detect freeswitch auth bruteforce||||0|0|
|crowdsecurity/freeswitch-user-enumeration|Freeswitch User Enumeration|Detect freeswitch user enumeration||||0|0|
|crowdsecurity/grafana-cve-2021-43798|Cve-2021-43798 Exploitation Attemps|Detect cve-2021-43798 exploitation attemps||||0|0|
|crowdsecurity/home-assistant-bf|Home Assistant Bruteforce|Detect Home Assistant bruteforce||||0|0|
|crowdsecurity/http-apiscp-bf|Apiscp Dashboard Bruteforce|detect apisCP dashboard bruteforce|http:bruteforce|||0|0|
|crowdsecurity/http-backdoors-attempts|Attempt TO Common Backdoors|Detect attempt to common backdoors||||0|0|
|crowdsecurity/http-bad-user-agent|BAD User-agents|Detect bad user-agents||||0|0|
|crowdsecurity/http-bf-wordpress_bf|Wordpress Bruteforce|detect wordpress bruteforce|http:bruteforce|||0|0|
|crowdsecurity/http-bf-wordpress_bf_xmlrpc|Wordpress Bruteforce ON Xmlrpc|detect wordpress bruteforce on xmlrpc|http:bruteforce|||0|0|
|crowdsecurity/http-crawl-non_statics|Aggressive Crawl From Single IP|Detect aggressive crawl from single ip|http:crawl|||0|0|
|crowdsecurity/http-cve-2021-41773|Cve-2021-41773|cve-2021-41773||||0|0|
|crowdsecurity/http-cve-2021-42013|Cve-2021-42013|cve-2021-42013||||0|0|
|crowdsecurity/http-generic-bf|Generic Http Brute Force|Detect generic http brute force||||0|0|
|LePresidente/http-generic-401-bf|Generic 401 Authorization Error Brute Force|Detect generic 401 Authorization error brute force||||0|0|
|LePresidente/http-generic-403-bf|Generic 403 Forbidden (authorization) Error Brute Force|Detect generic 403 Forbidden (Authorization) error brute force||||0|0|
|crowdsecurity/http-magento-bf|Magento Bruteforce|detect Magento bruteforce|http:bruteforce|||0|0|
|crowdsecurity/http-magento-ccs-by-as|Distributed Credit Card Stuffing From Same AS|Detect distributed credit card stuffing from same AS|http:scan|||0|0|
|crowdsecurity/http-magento-ccs-by-country|Distributed Credit Card Stuffing From Same Country|Detect distributed credit card stuffing from same country|http:scan|||0|0|
|crowdsecurity/http-magento-ccs|Credit Card Stuffing From A Single IP|Detect credit card stuffing from a single IP|http:scan|||0|0|
|crowdsecurity/http-open-proxy|Scan FOR Open Proxy|Detect scan for open proxy|http:scan|||0|0|
|crowdsecurity/http-path-traversal-probing|Path Traversal Attempt|Detect path traversal attempt|http:scan|||0|0|
|crowdsecurity/http-probing|Site Scanning/probing From A Single IP|Detect site scanning/probing from a single ip|http:scan|||0|0|
|crowdsecurity/http-sensitive-files|Attempt TO Access TO Sensitive Files (.log, .DB ..) OR Folders (.git)|Detect attempt to access to sensitive files (.log, .db ..) or folders (.git)||||0|0|
|crowdsecurity/http-sqli-probbing-detection|A Scenario That Detects SQL Injection Probing With Minimal False Positives|A scenario that detects SQL injection probing with minimal false positives||||0|0|
|crowdsecurity/http-wordpress_user-enum|Wordpress Probing : Authors Enumeration|detect wordpress probing : authors enumeration|http:bruteforce|||0|0|
|crowdsecurity/http-wordpress_wpconfig|Wordpress Probing : Variations Around Wp-config.php BY Wpscan|detect wordpress probing : variations around wp-config.php by wpscan|http:bruteforce|||0|0|
|crowdsecurity/http-xss-probbing|A Scenario That Detects XSS Probing With Minimal False Positives|A scenario that detects XSS probing with minimal false positives||||0|0|
|crowdsecurity/iptables-scan-multi_ports|BAN IPS That ARE Scanning US|ban IPs that are scanning us|tcp:scan|||0|0|
|crowdsecurity/jira_cve-2021-26086|Atlassian Jira Cve-2021-26086 Exploitation Attemps|Detect Atlassian Jira CVE-2021-26086 exploitation attemps||||0|0|
|crowdsecurity/k8s-audit-anonymous-access|Allowed Anonymous Access TO THE K8S API|Detect allowed anonymous access to the K8S API||||0|0|
|crowdsecurity/k8s-audit-api-server-bruteforce|Bruteforce Attempts Against K8S API Server|Detect bruteforce attempts against K8S API server||||0|0|
|crowdsecurity/k8s-audit-pod-exec|Execution (via Kubectl Exec) IN Pods|Detect execution (via kubectl exec) in pods||||0|0|
|crowdsecurity/k8s-audit-pod-host-network|Pods Started With Host Networking|Detect pods started with host networking||||0|0|
|crowdsecurity/k8s-audit-pod-host-path-volume|Pods Mounting A Sensitive Host Folder|Detect pods mounting a sensitive host folder||||0|0|
|crowdsecurity/k8s-audit-privileged-pod-creation|Privileged POD Creation|Detect privileged pod creation||||0|0|
|crowdsecurity/k8s-audit-service-account-access-denied|Unauthorized Requests From Service Accounts|Detect unauthorized requests from service accounts||||0|0|
|crowdsecurity/kasm-bruteforce|Kasm Login Bruteforce|Detect kasm login bruteforce||||0|0|
|crowdsecurity/litespeed-admin-bf|Bruteforce Against Litespeed Admin UI|Detect bruteforce against litespeed admin UI||||0|0|
|crowdsecurity/mariadb-bf|Mariadb Bruteforce|Detect mariadb bruteforce||||0|0|
|crowdsecurity/modsecurity|WEB Exploitation VIA Modsecurity|Web exploitation via modsecurity||||0|0|
|crowdsecurity/mssql-bf|Mssql Bruteforce|Detect mssql bruteforce||||0|0|
|crowdsecurity/mysql-bf|Mysql Bruteforce|Detect mysql bruteforce||||0|0|
|crowdsecurity/naxsi-exploit-vpatch|Custom Blacklist Triggered IN Naxsi|Detect custom blacklist triggered in naxsi|http:scan|||0|0|
|crowdsecurity/nextcloud-bf|Nextcloud Bruteforce|Detect Nextcloud bruteforce||||0|0|
|crowdsecurity/nextcloud-bf_user_enum|Nextcloud User Enum Bruteforce|Detect Nextcloud user enum bruteforce||||0|0|
|crowdsecurity/nextcloud-bf_domain_error|Nextcloud Domain Error|Detect Nextcloud domain error||||0|0|
|crowdsecurity/nginx-req-limit-exceeded|Detects IPS Which Violate Nginx's User SET Request Limit.|Detects IPs which violate nginx's user set request limit.||||0|0|
|crowdsecurity/odoo-bf|Bruteforce ON Odoo WEB Interface|Detect bruteforce on odoo web interface||||0|0|
|crowdsecurity/odoo_user-enum|Odoo User Enum|Detect odoo user enum||||0|0|
|crowdsecurity/opnsense-web-bf|Bruteforce ON Opnsense WEB Interface|Detect bruteforce on opnsense web interface||||0|0|
|crowdsecurity/pgsql-bf|Pgsql Bruteforce|Detect PgSQL bruteforce||||0|0|
|crowdsecurity/pgsql-user-enum|Postgresql User Enumeration|Detect postgresql user enumeration||||0|0|
|crowdsecurity/postfix-spam|Spammers|Detect spammers||||0|0|
|crowdsecurity/postscreen-rbl|Spammers|Detect spammers||||0|0|
|crowdsecurity/proftpd-bf|Proftpd Bruteforce|Detect proftpd bruteforce|ftp:bruteforce|||0|0|
|crowdsecurity/proftpd-bf_user-enum|Proftpd User Enum Bruteforce|Detect proftpd user enum bruteforce|ftp:bruteforce|||0|0|
|crowdsecurity/pulse-secure-sslvpn-cve-2019-11510|Cve-2019-11510 Exploitation Attemps|Detect cve-2019-11510 exploitation attemps||||0|0|
|crowdsecurity/smb-bf|SMB Bruteforce|Detect smb bruteforce|smb:bruteforce|||0|0|
|crowdsecurity/spring4shell_cve-2022-22965|Cve-2022-22965 Probing|Detect cve-2022-22965 probing||||0|0|
|crowdsecurity/ssh-bf|SSH Bruteforce|Detect ssh bruteforce|ssh:bruteforce|TA0006:T1110||0|3|
|crowdsecurity/ssh-bf_user-enum|SSH User Enum Bruteforce|Detect ssh user enum bruteforce|ssh:bruteforce|||0|0|
|crowdsecurity/ssh-slow-bf|Slow SSH Bruteforce|Detect slow ssh bruteforce|ssh:bruteforce|||0|0|
|crowdsecurity/ssh-slow-bf_user-enum|Slow SSH User Enum Bruteforce|Detect slow ssh user enum bruteforce|ssh:bruteforce|||0|0|
|crowdsecurity/suricata-major-severity|Exploit Attempts VIA Emerging Threat Rules|Detect exploit attempts via emerging threat rules||||0|0|
|crowdsecurity/suricata-high-medium-severity|Exploit Attempts VIA Emerging Threat Rules|Detect exploit attempts via emerging threat rules||||0|0|
|crowdsecurity/synology-dsm-bf|Synology DSM WEB Auth Bruteforce|Detect Synology DSM web auth bruteforce||||0|0|
|crowdsecurity/teamspeak3-bf|Teamspeak3 Server Bruteforce|detect teamspeak3 server bruteforce||||0|0|
|crowdsecurity/telnet-bf|Telnet Bruteforce|detect telnet bruteforce|telnet:bruteforce|||0|0|
|crowdsecurity/thehive-bf|Bruteforce ON Thehive WEB Interface|Detect bruteforce on Thehive web interface||||0|0|
|crowdsecurity/thinkphp-cve-2018-20062|Thinkphp Cve-2018-20062 Exploitation Attemps|Detect ThinkPHP CVE-2018-20062 exploitation attemps||||0|0|
|crowdsecurity/vmware-cve-2022-22954|Vmware Cve-2022-22954 Exploitation Attempts|Detect Vmware CVE-2022-22954 exploitation attempts||||0|0|
|crowdsecurity/vmware-vcenter-vmsa-2021-0027|Vmsa-2021-0027 Exploitation Attemps|Detect VMSA-2021-0027 exploitation attemps||||0|0|
|crowdsecurity/vsftpd-bf|FTP Bruteforce (vsftpd)|Detect FTP bruteforce (vsftpd)|ftp:bruteforce|||0|0|
|crowdsecurity/CVE-2022-30190-msdt|CVE-2022-30190|Detect CVE-2022-30190 from sysmon events|windows:rce|TA0002:T1059
TA0002:T1203|CVE-2022-30190|0|3|
|crowdsecurity/windows-bf|Windows Auth Bruteforce|Detect windows auth bruteforce|windows:bruteforce|||0|0|
