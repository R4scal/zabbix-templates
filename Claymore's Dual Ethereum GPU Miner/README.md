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

## Donations

If you find this useful and/or you would like to see additional extensions, feel free to donate some crypto:

- BTC: 34avFpVSPcFcfm3vwYgRBrVw9e9A3zu5t3
- ETH: 0x9Abafc1645831406BE9A23db09e3CB56A59466e5
- SC: 3098a29a6a810ae762044420bc402323c2d82a0b2f66ada9f4521e1c8561f459ea22548a9eaf

