Scenario to detect exploitation attempts of [CVE-2022-39290](https://github.com/ZoneMinder/zoneminder/security/advisories/GHSA-xgv6-qv6c-399q).
Basically do not allow any GET request to have action=. This is for ZM versions __BEFORE__ 1.36.27, 1.37.24

```
 GET /zm/index.php?view=options&tab=users&action=delete&markUids%5B%5D=13&deleteBtn=Delete HTTP/1.1
 Host: 10.0.10.107
 User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
 Accept-Language: en-US,en;q=0.5
 Accept-Encoding: gzip, deflate
 Origin: http://10.0.10.107
 Connection: close
 Referer: http://10.0.10.107/zm/index.php?view=options&tab=users
 Cookie: zmSkin=classic; zmCSS=base; zmLogsTable.bs.table.sortOrder=desc; zmLogsTable.bs.table.sortName=Message; zmLogsTable.bs.table.pageNumber=1; ZMSESSID=24u3uv4ed55n04f73slbu95pm9
 Upgrade-Insecure-Requests: 1
```

:warning: Crowdsec is not a WAF and, as such, bypass to those signatures are likely :warning:





