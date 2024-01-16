cmdb/firewall.service/group
---------------------------

FortiOS v6.4.14

.. code:: yaml

    color: 0
    comment: ''
    fabric-object: disable
    member:
    - name: DNS
      q_origin_key: DNS
    - name: IMAP
      q_origin_key: IMAP
    - name: IMAPS
      q_origin_key: IMAPS
    - name: POP3
      q_origin_key: POP3
    - name: POP3S
      q_origin_key: POP3S
    - name: SMTP
      q_origin_key: SMTP
    - name: SMTPS
      q_origin_key: SMTPS
    name: Email Access
    proxy: disable
    q_origin_key: Email Access
