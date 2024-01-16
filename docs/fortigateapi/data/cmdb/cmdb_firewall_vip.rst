cmdb/firewall/vip
-----------------

FortiOS v6.4.14

.. code:: yaml

    arp-reply: enable
    color: 0
    comment: ''
    dns-mapping-ttl: 0
    extaddr: []
    extintf: INTERFACE_NAME
    extip: 10.0.0.1-10.0.0.254
    extport: 0-65535
    gratuitous-arp-interval: 0
    http-cookie-age: 60
    http-cookie-domain: ''
    http-cookie-domain-from-host: disable
    http-cookie-generation: 0
    http-cookie-path: ''
    http-cookie-share: same-ip
    http-ip-header: disable
    http-ip-header-name: ''
    http-multiplex: disable
    http-redirect: disable
    https-cookie-secure: disable
    id: 0
    ldb-method: static
    mapped-addr: ''
    mappedip:
    - q_origin_key: 1.1.1.1-1.1.1.254
      range: 1.1.1.1-1.1.1.254
    mappedport: 0-65535
    max-embryonic-connections: 1000
    monitor: []
    name: NAT_NAME
    nat-source-vip: disable
    outlook-web-access: disable
    persistence: none
    portforward: disable
    portmapping-type: 1-to-1
    protocol: tcp
    q_origin_key: NAT_NAME
    realservers: []
    server-type: ''
    service: []
    src-filter: []
    srcintf-filter: []
    ssl-algorithm: high
    ssl-certificate: ''
    ssl-cipher-suites: []
    ssl-client-fallback: enable
    ssl-client-rekey-count: 0
    ssl-client-renegotiation: secure
    ssl-client-session-state-max: 1000
    ssl-client-session-state-timeout: 30
    ssl-client-session-state-type: both
    ssl-dh-bits: '2048'
    ssl-hpkp: disable
    ssl-hpkp-age: 5184000
    ssl-hpkp-backup: ''
    ssl-hpkp-include-subdomains: disable
    ssl-hpkp-primary: ''
    ssl-hpkp-report-uri: ''
    ssl-hsts: disable
    ssl-hsts-age: 5184000
    ssl-hsts-include-subdomains: disable
    ssl-http-location-conversion: disable
    ssl-http-match-host: enable
    ssl-max-version: tls-1.3
    ssl-min-version: tls-1.1
    ssl-mode: half
    ssl-pfs: require
    ssl-send-empty-frags: enable
    ssl-server-algorithm: client
    ssl-server-cipher-suites: []
    ssl-server-max-version: client
    ssl-server-min-version: client
    ssl-server-session-state-max: 100
    ssl-server-session-state-timeout: 60
    ssl-server-session-state-type: both
    type: static-nat
    uuid: c7630e8a-8d8e-51ec-f838-2959a52d61c7
    weblogic-server: disable
    websphere-server: disable