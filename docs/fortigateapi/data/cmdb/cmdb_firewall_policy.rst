cmdb/firewall/policy
--------------------

FortiOS v6.4.14

.. code:: yaml

    action: accept
    anti-replay: enable
    application-list: ''
    auth-cert: ''
    auth-path: disable
    auth-redirect-addr: ''
    auto-asic-offload: enable
    av-profile: ''
    block-notification: disable
    captive-portal-exempt: disable
    capture-packet: disable
    cifs-profile: ''
    comments: ''
    custom-log-fields: []
    decrypted-traffic-mirror: ''
    delay-tcp-npu-session: disable
    diffserv-forward: disable
    diffserv-reverse: disable
    diffservcode-forward: '000000'
    diffservcode-rev: '000000'
    disclaimer: disable
    dlp-sensor: ''
    dnsfilter-profile: ''
    dsri: disable
    dstaddr:
    - name: all
      q_origin_key: all
    dstaddr-negate: disable
    dstaddr6: []
    dstintf:
    - name: any
      q_origin_key: any
    dynamic-shaping: disable
    email-collect: disable
    emailfilter-profile: ''
    file-filter-profile: ''
    firewall-session-dirty: check-all
    fixedport: disable
    fsso-agent-for-ntlm: ''
    fsso-groups: []
    geoip-anycast: disable
    geoip-match: physical-location
    global-label: ''
    groups: []
    http-policy-redirect: disable
    icap-profile: ''
    identity-based-route: ''
    inbound: disable
    inspection-mode: flow
    internet-service: disable
    internet-service-custom: []
    internet-service-custom-group: []
    internet-service-group: []
    internet-service-name: []
    internet-service-negate: disable
    internet-service-src: disable
    internet-service-src-custom: []
    internet-service-src-custom-group: []
    internet-service-src-group: []
    internet-service-src-name: []
    internet-service-src-negate: disable
    ippool: disable
    ips-sensor: ''
    label: ''
    logtraffic: utm
    logtraffic-start: disable
    match-vip: disable
    match-vip-only: disable
    name: POLICY
    nat: disable
    natinbound: disable
    natip: 0.0.0.0 0.0.0.0
    natoutbound: disable
    np-acceleration: enable
    ntlm: disable
    ntlm-enabled-browsers: []
    ntlm-guest: disable
    outbound: enable
    per-ip-shaper: ''
    permit-any-host: disable
    permit-stun-host: disable
    policyid: 3
    poolname: []
    poolname6: []
    profile-group: ''
    profile-protocol-options: default
    profile-type: single
    q_origin_key: 3
    radius-mac-auth-bypass: disable
    redirect-url: ''
    replacemsg-override-group: ''
    reputation-direction: destination
    reputation-minimum: 0
    rtp-addr: []
    rtp-nat: disable
    schedule: always
    schedule-timeout: disable
    send-deny-packet: disable
    service:
    - name: ALL
      q_origin_key: ALL
    service-negate: disable
    session-ttl: '0'
    src-vendor-mac: []
    srcaddr:
    - name: all
      q_origin_key: all
    srcaddr-negate: disable
    srcaddr6: []
    srcintf:
    - name: any
      q_origin_key: any
    ssh-filter-profile: ''
    ssh-policy-redirect: disable
    ssl-ssh-profile: no-inspection
    status: enable
    tcp-mss-receiver: 0
    tcp-mss-sender: 0
    tcp-session-without-syn: disable
    timeout-send-rst: disable
    tos: '0x00'
    tos-mask: '0x00'
    tos-negate: disable
    traffic-shaper: ''
    traffic-shaper-reverse: ''
    users: []
    utm-status: disable
    uuid: 44b851f6-adf9-51ee-9a39-6e863945a797
    vlan-cos-fwd: 255
    vlan-cos-rev: 255
    vlan-filter: ''
    voip-profile: ''
    vpntunnel: ''
    waf-profile: ''
    wccp: disable
    webfilter-profile: ''
    webproxy-forward-server: ''
    webproxy-profile: ''

FortiOS v7.0.7

.. code:: yaml

    action: accept
    anti-replay: enable
    application-list: ''
    auth-cert: ''
    auth-path: disable
    auth-redirect-addr: ''
    auto-asic-offload: enable
    av-profile: ''
    block-notification: disable
    captive-portal-exempt: disable
    capture-packet: disable
    cifs-profile: ''
    comments: ''
    custom-log-fields: []
    decrypted-traffic-mirror: ''
    delay-tcp-npu-session: disable
    diffserv-forward: disable
    diffserv-reverse: disable
    diffservcode-forward: '000000'
    diffservcode-rev: '000000'
    disclaimer: disable
    dlp-sensor: ''
    dnsfilter-profile: ''
    dsri: disable
    dstaddr:
    - name: all
      q_origin_key: all
    dstaddr-negate: disable
    dstaddr6: []
    dstintf:
    - name: any
      q_origin_key: any
    dynamic-shaping: disable
    email-collect: disable
    emailfilter-profile: ''
    fec: disable
    file-filter-profile: ''
    firewall-session-dirty: check-all
    fixedport: disable
    fsso-agent-for-ntlm: ''
    fsso-groups: []
    geoip-anycast: disable
    geoip-match: physical-location
    global-label: ''
    groups: []
    http-policy-redirect: disable
    icap-profile: ''
    identity-based-route: ''
    inbound: disable
    inspection-mode: flow
    internet-service: disable
    internet-service-custom: []
    internet-service-custom-group: []
    internet-service-group: []
    internet-service-name: []
    internet-service-negate: disable
    internet-service-src: disable
    internet-service-src-custom: []
    internet-service-src-custom-group: []
    internet-service-src-group: []
    internet-service-src-name: []
    internet-service-src-negate: disable
    ippool: disable
    ips-sensor: ''
    label: ''
    logtraffic: utm
    logtraffic-start: disable
    match-vip: disable
    match-vip-only: disable
    name: POLICY
    nat: disable
    nat46: disable
    nat64: disable
    natinbound: disable
    natip: 0.0.0.0 0.0.0.0
    natoutbound: disable
    np-acceleration: enable
    ntlm: disable
    ntlm-enabled-browsers: []
    ntlm-guest: disable
    outbound: enable
    passive-wan-health-measurement: disable
    per-ip-shaper: ''
    permit-any-host: disable
    permit-stun-host: disable
    policyid: 51
    poolname: []
    poolname6: []
    profile-group: ''
    profile-protocol-options: default
    profile-type: single
    q_origin_key: 51
    radius-mac-auth-bypass: disable
    redirect-url: ''
    replacemsg-override-group: ''
    reputation-direction: destination
    reputation-minimum: 0
    rtp-addr: []
    rtp-nat: disable
    schedule: always
    schedule-timeout: disable
    sctp-filter-profile: ''
    send-deny-packet: disable
    service:
    - name: ALL
      q_origin_key: ALL
    service-negate: disable
    session-ttl: '0'
    sgt: []
    sgt-check: disable
    src-vendor-mac: []
    srcaddr:
    - name: all
      q_origin_key: all
    srcaddr-negate: disable
    srcaddr6: []
    srcintf:
    - name: any
      q_origin_key: any
    ssh-filter-profile: ''
    ssh-policy-redirect: disable
    ssl-ssh-profile: no-inspection
    status: enable
    tcp-mss-receiver: 0
    tcp-mss-sender: 0
    tcp-session-without-syn: disable
    timeout-send-rst: disable
    tos: '0x00'
    tos-mask: '0x00'
    tos-negate: disable
    traffic-shaper: ''
    traffic-shaper-reverse: ''
    users: []
    utm-status: disable
    uuid: 4775025e-adf9-51ee-71e3-81a673c03771
    uuid-idx: 1019
    videofilter-profile: ''
    vlan-cos-fwd: 255
    vlan-cos-rev: 255
    vlan-filter: ''
    voip-profile: ''
    vpntunnel: ''
    waf-profile: ''
    wccp: disable
    webfilter-profile: ''
    webproxy-forward-server: ''
    webproxy-profile: ''
    ztna-ems-tag: []
    ztna-geo-tag: []
    ztna-status: disable

Difference
..........

FortiOS v6.4.14

.. code:: yaml

    {}

FortiOS v7.0.7

.. code:: yaml

    fec: disable
    nat46: disable
    nat64: disable
    passive-wan-health-measurement: disable
    sctp-filter-profile: ''
    sgt: []
    sgt-check: disable
    uuid-idx: 1019
    videofilter-profile: ''
    ztna-ems-tag: []
    ztna-geo-tag: []
    ztna-status: disable
