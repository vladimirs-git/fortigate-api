cmdb/system.snmp/community
--------------------------

FortiOS v6.4.14

.. code:: yaml

    events: cpu-high mem-low log-full intf-ip vpn-tun-up vpn-tun-down ha-switch ha-hb-failure
      ips-signature ips-anomaly av-virus av-oversize av-pattern av-fragmented fm-if-change
      bgp-established bgp-backward-transition ha-member-up ha-member-down ent-conf-change
      av-conserve av-bypass av-oversize-passed av-oversize-blocked ips-pkg-update ips-fail-open
      power-supply-failure faz-disconnect wc-ap-up wc-ap-down fswctl-session-up fswctl-session-down
      load-balance-real-server-down per-cpu-high dhcp
    hosts:
    - ha-direct: enable
      host-type: query
      id: 1
      ip: 10.0.0.0 255.255.255.0
      q_origin_key: 1
      source-ip: 0.0.0.0
    - ha-direct: enable
      host-type: query
      id: 2
      ip: 10.0.1.0 255.255.255.0
      q_origin_key: 2
      source-ip: 0.0.0.0
    hosts6: []
    id: 1
    name: SNMP_COMMUNITY_NAME
    q_origin_key: 1
    query-v1-port: 161
    query-v1-status: disable
    query-v2c-port: 161
    query-v2c-status: enable
    status: enable
    trap-v1-lport: 162
    trap-v1-rport: 162
    trap-v1-status: disable
    trap-v2c-lport: 162
    trap-v2c-rport: 162
    trap-v2c-status: disable
