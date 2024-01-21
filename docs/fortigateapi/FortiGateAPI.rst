FortiGateAPI
============

.. autoclass:: fortigate_api.FortiGateAPI
  :members:


Usage
-----

.. code:: python

    """FortiGateAPI examples.
    
    - Initialize FortiGateAPI with optional parameters scheme=`https`, port=443
    - Create address in the Fortigate
    - Get address by name (unique identifier)
    - Update address data in the Fortigate
    - Delete address from the Fortigate
    - Check for absence of address in the Fortigate
    - FortiGateAPI `with` statement
    """
    
    import logging
    
    from fortigate_api import FortiGateAPI
    
    logging.getLogger().setLevel(logging.DEBUG)
    
    HOST = "host"
    USERNAME = "username"
    PASSWORD = "password"
    
    # Initialize FortiGateAPI with optional parameters scheme=`https`, port=443
    api = FortiGateAPI(
        host=HOST,
        username=USERNAME,
        password=PASSWORD,
        scheme="https",
        port=443,
        logging_error=True,
    )
    api.login()  # login is optional
    
    # Create address in the Fortigate
    data = {
        "name": "ADDRESS",
        "obj-type": "ip",
        "subnet": "127.0.0.100 255.255.255.252",
        "type": "ipmask",
    }
    response = api.cmdb.firewall.address.create(data)
    print(f"address.create {response}")  # address.create <Response [200]>
    
    # Get address by name (unique identifier)
    items = api.cmdb.firewall.address.get(name="ADDRESS")
    print(f"addresses count={len(items)}")  # addresses count=1
    
    # Update address data in the Fortigate
    data = {"name": "ADDRESS", "subnet": "127.0.0.255 255.255.255.255"}
    response = api.cmdb.firewall.address.update(data)
    print(f"address.update {response}")  # address.update <Response [200]>
    
    # Delete address from the Fortigate
    response = api.cmdb.firewall.address.delete("ADDRESS")
    print(f"address.delete {response}")  # address.delete <Response [200]>
    
    # Check for absence of address in the Fortigate
    response = api.cmdb.firewall.address.is_exist("ADDRESS")
    print(f"address.is_exist {response}")  # address.is_exist False
    
    api.logout()
    
    # FortiGateAPI `with` statement
    with FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD) as api:
        response = api.cmdb.firewall.address.is_exist("ADDRESS")
        print("address.is_exist", response)  # exist <Response [404]>


