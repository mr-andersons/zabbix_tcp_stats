# TCP stats monitoring.

Monitor all tcp stats and by specific service from /etc/services **using ss and zabbix-sender**

#### For example:
Coppy `tcp_stats.conf` to `/etc/zabbix/zabbix_agentd.d/tcp_stats.conf`
and `template_tcp_stats/*` to `/etc/zabbix/scripts/template_tcp_stats/`
Or just add UserParameter with correct paths.
```
UserParameter=tcp.discovery, python {path to tcp_services_discovery.py} http mysql
UserParameter=tcp.all-data[*], python {path to tcp_stats.py} $1 | /usr/bin/zabbix_sender -c {path to zabbix_agentd.conf} -i -  > /dev/null  2>&1
```

Add as many services from `/etc/services` to `/etc/zabbix/zabbix_agentd.d/tcp_stats.conf`, for example, http, ssh, mysql:
`UserParameter=tcp.discovery, python /etc/zabbix/scripts/template_tcp_stats/tcp_services_discovery.py http ssh mysql`

Each service will have its own graph in zabbix
