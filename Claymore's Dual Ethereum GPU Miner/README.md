# Template for Claymore's Dual Ethereum GPU Miner 

## Prerequisites

*py-zabbix* and *requests* packages is needed.

```
$ sudo pip install py-zabbix requests
```

##  Install

1. Import template on zabbix server.
2. Deploy claymore.conf and zabbix_claymore.py at you agents.

## Supported items 

- [x] Ethereum Hashrate
- [x] Ethereum accepted shares
- [x] Ethereum rejected shares
- [x] Ethereum efficiency
- [x] Decred Hashrate
- [x] Decred accepted shares
- [x] Decred rejected shares
- [x] Decred efficiency

## Available triggers

- [x] Ethereum efficiency: large amount of rejected shares
- [x] Decred efficiency: large amount of rejected shares

