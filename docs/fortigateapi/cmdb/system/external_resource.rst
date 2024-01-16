FortiGateAPI.cmdb.system.external_resource
==========================================

.. autoclass:: fortigate_api.cmdb.system.ExternalResourceSC
  :members:
  :undoc-members:
  :inherited-members:
  :class-doc-from: class


Usage
-----

.. code:: python

    """api/v2/cmdb/system/external-resource
    
    - Create External Resources
    - Gets all external-resources from the Fortigate
    - Gets filtered external-resources by name (unique identifier)
    - Updates external-resource data in the Fortigate
    - Deletes external-resource from the Fortigate by name
    - Checks for absence of external_resource in the Fortigate
    """
    
    from fortigate_api import FortiGateAPI
    
    HOST = "host"
    USERNAME = "username"
    PASSWORD = "password"
    
    api = FortiGateAPI(host=HOST, username=USERNAME, password=PASSWORD)
    
    # Create External Resources
    data = {"name": "RESOURCE_1", "resource": "https://domain.com/resource.txt", "type": "address"}
    response = api.cmdb.system.external_resource.create(data)
    print("external_resource.create", response)  # external_resource.create <Response [200]>
    
    # Gets all external-resources from the Fortigate
    items = api.cmdb.system.external_resource.get()
    print(f"external-resources count={len(items)}")  # external-resources count=5
    
    # Gets filtered external-resources by name (unique identifier)
    items = api.cmdb.system.external_resource.get(name="RESOURCE_1")
    print(f"external-resources count={len(items)}")  # external-resources count=1
    
    # Updates external-resource data in the Fortigate
    data = dict(name="RESOURCE_1", status="disable")
    response = api.cmdb.system.external_resource.update(data)
    print("external_resource.update", response)  # external_resource.update <Response [200]>
    
    # Deletes external-resource from the Fortigate by name
    response = api.cmdb.system.external_resource.delete("RESOURCE_1")
    print("external_resource.delete", response)  # external_resource.delete <Response [200]>
    
    # Checks for absence of external_resource in the Fortigate
    response = api.cmdb.system.external_resource.is_exist("RESOURCE_1")
    print("external_resource.is_exist", response)  # external_resource.is_exist False
    
    api.logout()


