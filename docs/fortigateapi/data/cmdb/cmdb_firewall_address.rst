cmdb/firewall/address
---------------------

FortiOS v6.4.14

.. code:: yaml

    allow-routing: disable
    associated-interface: ''
    cache-ttl: 0
    clearpass-spt: unknown
    color: 0
    comment: ''
    country: ''
    end-mac: 00:00:00:00:00:00
    fabric-object: disable
    filter: ''
    fsso-group: []
    interface: ''
    list: []
    name: ADDRESS
    obj-id: ''
    obj-type: ip
    q_origin_key: ADDRESS
    sdn: ''
    sdn-addr-type: private
    start-mac: 00:00:00:00:00:00
    sub-type: sdn
    subnet: 127.0.0.100 255.255.255.252
    tagging: []
    type: ipmask
    uuid: 6ba93d24-adf5-51ee-6165-a6c3cb19d248

FortiOS v7.0.7

.. code:: yaml

    allow-routing: disable
    associated-interface: ''
    cache-ttl: 0
    clearpass-spt: unknown
    color: 0
    comment: ''
    country: ''
    dirty: dirty
    fabric-object: disable
    filter: ''
    fsso-group: []
    interface: ''
    list: []
    macaddr: []
    name: ADDRESS
    node-ip-only: disable
    obj-id: ''
    obj-type: ip
    q_origin_key: ADDRESS
    sdn: ''
    sdn-addr-type: private
    sub-type: sdn
    subnet: 127.0.0.100 255.255.255.252
    tag-detection-level: ''
    tag-type: ''
    tagging: []
    type: ipmask
    uuid: 6da7800e-adf5-51ee-1fb0-e3982f975e93

Difference
..........

FortiOS v6.4.14

.. code:: yaml

    end-mac: 00:00:00:00:00:00
    start-mac: 00:00:00:00:00:00

FortiOS v7.0.7

.. code:: yaml

    dirty: dirty
    macaddr: []
    node-ip-only: disable
    tag-detection-level: ''
    tag-type: ''
