filtering conditions
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

Example:

.. code:: python

    import logging

    from fortigate_api import FortigateAPI

    logging.getLogger().setLevel(logging.DEBUG)

    HOST = "host"
    USERNAME = "username"
    PASSWORD = "password"

    fgt = FortigateAPI(host=HOST, username=USERNAME, password=PASSWORD)

    # Create addresses: `ADDRESS_0`, `ADDRESS_1`, `ADDRESS_2`
    for idx in range(3):
        data = {
            "name": f"ADDRESS_{idx}",
            "obj-type": "ip",
            "subnet": f"127.0.0.10{idx} 255.255.255.255",
            "type": "ipmask",
        }
        response = fgt.address.create(data=data)
        print("address.create", response)  # address.create <Response [200]>

    # Filter addresses that starts with `ADDRESS_`
    addresses = fgt.address.get(filter="=@ADDRESS_")
    print(f"{len(addresses)=}")  # len(addresses)=3

    # Delete addresses that starts with `ADDRESS_`
    response = fgt.address.delete(filter="=@ADDRESS_")
    print("address.delete", response)  # address.delete <Response [200]>

    # Check addresses have been deleted
    addresses = fgt.address.get(filter="=@ADDRESS_")
    print(f"{len(addresses)=}")  # len(addresses)=0
