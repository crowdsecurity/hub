# Zabbix bruteforce detection
Detect unsucessful login attempts into Zabbix GUI by counting POST action at index.php. Tested with Zabbix 6.2.7.

Requests and responses:
  - POST /zabbix/index.php 200 : Return to login page after unsuccesful attempt.
  - POST /zabbix/index.php 302 : Redirect toward zabbix.php after a sucessful login.
