DhcpServer.yml
--------------

FortiOS v6.4

.. code:: yaml

    auto-configuration: enable
    auto-managed-status: enable
    conflicted-ip-timeout: 1800
    ddns-auth: disable
    ddns-key: '''ENC PShBOAJA41afiCalhWIZ3x6Pvojb8CetiWTCc6uc5PUWoLUuqhUQQFSewDkIO3pBknwII+OgYEU+hSMmPo67SuaXUcKOCAyEo1FN0C9GwRVX5pv7Oe+MYorUr8w='''
    ddns-keyname: ''
    ddns-server-ip: 0.0.0.0
    ddns-ttl: 300
    ddns-update: disable
    ddns-update-override: disable
    ddns-zone: ''
    default-gateway: 10.0.0.1
    dhcp-settings-from-fortiipam: disable
    dns-server1: 0.0.0.0
    dns-server2: 0.0.0.0
    dns-server3: 0.0.0.0
    dns-server4: 0.0.0.0
    dns-service: default
    domain: ''
    exclude-range: []
    filename: ''
    forticlient-on-net-status: enable
    id: 1
    interface: vlan.123
    ip-mode: range
    ip-range:
    - end-ip: 10.0.0.254
      id: 1
      q_origin_key: 1
      start-ip: 10.0.0.2
    ipsec-lease-hold: 60
    lease-time: 604800
    mac-acl-default-action: assign
    netmask: 255.255.255.0
    next-server: 0.0.0.0
    ntp-server1: 0.0.0.0
    ntp-server2: 0.0.0.0
    ntp-server3: 0.0.0.0
    ntp-service: specify
    options: []
    q_origin_key: 1
    reserved-address: []
    server-type: regular
    status: enable
    tftp-server: []
    timezone: '00'
    timezone-option: disable
    vci-match: disable
    vci-string: []
    wifi-ac-service: specify
    wifi-ac1: 0.0.0.0
    wifi-ac2: 0.0.0.0
    wifi-ac3: 0.0.0.0
    wins-server1: 0.0.0.0
    wins-server2: 0.0.0.0
