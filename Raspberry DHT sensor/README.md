# Template for Raspberry Pi temperature and humidity monitoring

## Prerequisites

*py-zabbix* and *adafruit_python_dht* packages is needed.

```
$ sudo pip install adafruit_python_dht py-zabbix
```

It is also necessary to add the zabbix user to the gpio group

```
sudo usermod -a -G gpio zabbix
```

### Settings

```python
sensor = Adafruit_DHT.AM2302
pin = 4
hostname = socket.getfqdn()
```

##  Install

1. Import template on zabbix server.
2. Deploy dht.conf and zabbix_dht.py at you agents.

## Monitoring

- [x] Temperature
- [x] Humidity

