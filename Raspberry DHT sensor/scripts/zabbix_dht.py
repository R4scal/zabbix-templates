#!/usr/bin/python

import socket
import Adafruit_DHT
from pyzabbix import ZabbixMetric, ZabbixSender

# Vars
sensor = Adafruit_DHT.AM2302
pin = 4
hostname = socket.getfqdn()

# Read data from sensor
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Send metrics to zabbix trapper
packet = [
  ZabbixMetric(hostname, 'dht[temperature]', temperature),
  ZabbixMetric(hostname, 'dht[humidity]', humidity),
]
result = ZabbixSender(use_config=True).send(packet)

print 1

