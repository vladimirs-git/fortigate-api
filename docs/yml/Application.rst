Application.yml
---------------

FortiOS v6.4

.. code:: yaml

    app-replacemsg: enable
    comment: Monitor all applications.
    control-default-network-services: disable
    deep-app-inspection: enable
    default-network-services: []
    enforce-default-app-port: disable
    entries:
    - action: pass
      application: []
      behavior: all
      category: []
      exclusion: []
      id: 1
      log: enable
      log-packet: disable
      parameters: []
      per-ip-shaper: ''
      popularity: 1 2 3 4 5
      protocols: all
      q_origin_key: 1
      quarantine: none
      quarantine-expiry: 5m
      quarantine-log: enable
      rate-count: 0
      rate-duration: 60
      rate-mode: continuous
      rate-track: none
      risk: []
      session-ttl: 0
      shaper: ''
      shaper-reverse: ''
      technology: all
      vendor: all
    extended-log: disable
    force-inclusion-ssl-di-sigs: disable
    name: default
    options: allow-dns
    other-application-action: pass
    other-application-log: disable
    p2p-black-list: ''
    q_origin_key: default
    replacemsg-group: ''
    unknown-application-action: pass
    unknown-application-log: disable
