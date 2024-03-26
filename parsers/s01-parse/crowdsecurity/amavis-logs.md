This parser detects logs generated when a message is blocked by amavis:

```
Feb 23 04:55:57 xyz amavis[4051607]: (4051607-09) Blocked INFECTED (Porcupine.Phishing.55542.UNOFFICIAL) {DiscardedInbound,Quarantined}, [192.168.0.1]:1434 [192.168.0.1] <someone1@something1.com> -> <someon2@something2.com>, quarantine: 2/virus-26W2lJY63nCZ, Queue-ID: 83B741009CD35, Message-ID: <20240223075525.8CD9941B67@xxx.xxx.shop>, mail_id: 26W2lJY63nCZ, Hits: -, size: 28646, 104 ms
```

