# Template for monitoring Logstash

##  Install

1. Install plugins for logstash
```bash
bin/logstash-plugin install logstash-input-heartbeat
bin/logstash-plugin install logstash-output-zabbix
```
2. Create config for zabbix.
```
input {
  heartbeat {
    message   => "epoch"
    interval  => 30
    add_field => { "zabbix_host" => "your_server_name" "zabbix_key" => "logstash.heartbeat" }
    tags      => [ "heartbeat" ]
  }
}

filter { }

output {
  if "heartbeat" in [tags] {
    zabbix {
      zabbix_server_host => "your_zabbix_server_or_proxy"
      zabbix_host        => "zabbix_host"
      zabbix_key         => "zabbix_key"
      zabbix_value       => "clock"
    }
  }
}
```
3. Import template on zabbix server.
4. Assign template with you server.

## Monitoring

- [x] Alarm if no heartbeats for 1 minute
