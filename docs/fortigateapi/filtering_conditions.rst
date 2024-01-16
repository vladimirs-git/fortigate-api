Filtering conditions
--------------------

========  =====================================================
Operator  Description
========  =====================================================
==        Case insensitive match with pattern.
!=        Does not match with pattern (case insensitive).
=@        Pattern found in object value (case insensitive).
!@        Pattern not found in object value (case insensitive).
<=        Value must be less than or equal to pattern.
<         Value must be less than pattern.
.>=       Value must be greater than or equal to pattern.
.>        Value must be greater than pattern.
========  =====================================================


Usage
.....

.. code:: python

    """Filtering conditions api/v2/cmdb/firewall/address

    - Create addresses: `ADDRESS_0`, `ADDRESS_1`, `ADDRESS_2`
    - Get all addresses without filtering
    - Filter address that is equal to `ADDRESS_0`
    - Filter addresses that are not equal to `ADDRESS_0`
    - Filter addresses that start with `ADDRESS_`
    - Filter addresses that do not start with `ADDRESS_`
    - Delete addresses that start with `ADDRESS_`
    - Check addresses have been deleted
    """

    import logging

    from fortigate_api import FortiOS

    logging.getLogger().setLevel(logging.DEBUG)

    HOST = "host"
    USERNAME = "username"
    PASSWORD = "password"

    api = FortiOS(host=HOST, username=USERNAME, password=PASSWORD)

    # Create addresses: `ADDRESS_0`, `ADDRESS_1`, `ADDRESS_2`
    for idx in range(3):
        data = {
            "name": f"ADDRESS_{idx}",
            "obj-type": "ip",
            "subnet": f"127.0.0.10{idx} 255.255.255.255",
            "type": "ipmask",
        }
        response = api.cmdb.firewall.address.create(data=data)
        print("address.create", response)  # address.create <Response [200]>

    # Get all addresses without filtering
    items = api.cmdb.firewall.address.get()
    print(f"addresses count={len(items)}")  # addresses count=16

    # Filter address that is equal to `ADDRESS_0`
    items = api.cmdb.firewall.address.get(filter="==ADDRESS_0")
    print(f"addresses count={len(items)}")  # addresses count=1

    # Filter addresses that are not equal to `ADDRESS_0`
    items = api.cmdb.firewall.address.get(filter="!=ADDRESS_0")
    print(f"addresses count={len(items)}")  # addresses count=15

    # Filter addresses that start with `ADDRESS_`
    items = api.cmdb.firewall.address.get(filter="=@ADDRESS_")
    print(f"addresses count={len(items)}")  # addresses count=3

    # Filter addresses that do not start with `ADDRESS_`
    items = api.cmdb.firewall.address.get(filter="!@ADDRESS_")
    print(f"addresses count={len(items)}")  # addresses count=13

    # Delete addresses that start with `ADDRESS_`
    response = api.cmdb.firewall.address.delete(filters=["=@ADDRESS_"])
    print("address.delete", response)  # address.delete <Response [200]>

    # Check addresses have been deleted
    items = api.cmdb.firewall.address.get(filter="=@ADDRESS_")
    print(f"addresses count={len(items)}")  # addresses count=0
