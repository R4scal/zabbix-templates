#!/usr/bin/env python

import requests
import re
import json
import socket
from pyzabbix import ZabbixMetric, ZabbixSender


url = 'http://localhost:3333'
hostname = socket.getfqdn()

try:
    r = requests.get(url)
    t = re.search('\{[^\}]+\}', r.text)
    j = json.loads(t.group(0))
except ValueError, e:
    print(str(e))

data = {}
data['eth_hashrate'], data['eth_accepted'], data['eth_rejected'] = j['result'][2].split(';')
data['dcr_hashrate'], data['dcr_accepted'], data['dcr_rejected'] = j['result'][4].split(';')

#print j['result']
#print data

# Send metrics to zabbix trapper
packet = []
for (title, value) in data.items():
    #print value, title
    packet.append(ZabbixMetric(hostname, title, value))

print packet
result = ZabbixSender(use_config=True).send(packet)

print 1
