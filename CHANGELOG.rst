
.. :changelog:

CHANGELOG
=========

Unreleased
----------

**New:** `FortiGateAPI.log` connectors, to work with all `Log API` endpoints.

**New:** `FortiGateAPI.monitor` connectors, to work with all `Monitor API` endpoints.


2.0.3 (2024-12-30)
------------------
**Changed:** .github/workflows


2.0.2 (2024-05-17)
------------------

**Changed:** FortiGateBase.login() for token check /api/v2/monitor/system/status

**Changed:** FortiGateBase._get_token_from_cookies() cookie_prefix = "ccsrftoken"


2.0.1 (2024-01-24)
------------------

**Fixed:** FortigateAPI `get`, `update` methods for objects without UID


2.0.0 (2024-01-16)
------------------

The package has been fully refactored.
The skeleton has been changed to make it possible to implement any endpoint
in a manner similar to `FortiOS REST API`_ documentation.

Breaking changes
----------------

**Added:** FortiGateAPI object (replacement for FortigateAPI object). This object contains
connectors to all Configuration (cmdb) REST API endpoints. For example old `FortigateAPI.address`
connector have been transformed to `FortiGateAPI.cmdb.firewall.address`. Other connectors
are transformed in a similar manner.

**Added:** FortiGate object (replacement for Fortigate object). It is a Python wrapper for
the FortiOS REST API. The `get` methods have been significantly changed to support responses
with any data type.

**Removed:** FortigateAPI object (replaced by FortiGateAPI object).

**Removed:** Fortigate object (replaced by FortiGate object).

**Removed:** SSH Netmiko connector.

**Removed:** CiscoConfParse adapted for Fortigate.


1.4.0 (2023-12-26)
------------------

**Added:** readthedocs

**Added:** FortigateAPI.vdoms

**Fixed:** FortigateAPI.<object>.create().
Return <Response [500]> if Object already exist. Before was <Response [200]>.
The behavior is the same as in the Fortigate POST method.

**Fixed:** FortigateAPI.<object>.delete(filter).
Return <Response [404]> if no objects have been found by filter.

**Fixed:** FortigateAPI.<object>.update().
Return <Response [404]> if Object is not exist. Before was <Response [200]>.
The behavior is the same as in the Fortigate PUT method.


1.3.1 (2023-12-06)
------------------

**Fixed:** quoted parameters, FortigateAPI.delete(filter="name=@10.0.0.1/32").


1.3.0 (2023-11-16)
------------------

**Added:** Fortigate.get_l().


1.2.5 (2023-11-06)
------------------

**Fixed:** Look for a cookie that is named "ccsrftoken"


1.2.4 (2023-05-02)
------------------

**Fixed:** Fortigate._valid_url()


1.2.3 (2023-04-27)
------------------

**Added:** poetry


1.2.2 (2023-04-27)
------------------

**Fixed:** dependencies

**Added:** actions


1.2.1 (2023-04-26)
------------------

**Added:** FortigateAPI.ExternalResource.

**Added:** Fortigate.token.

**Fixed:** Fortigate.__repr__() removed password.

**Changed:** FortigateAPI.fgt > FortigateAPI.rest.


1.1.1 (2023-03-16)
------------------

**Added:** ./examples/ssh_vdom.py.

**Changed:** README.rst ssh.


1.1.0 (2023-03-05)
------------------

**Added:** ciscoconfparse.


1.0.2 (2023-02-07)
------------------

**Fixed:** ccsrftoken for fortios v7.


1.0.1 (2022-11-01)
------------------

**Fixed:** py.typed.


1.0.0 (2022-10-29)
------------------

**Added:** SSH.

**Added:** HTTPS SSL verify.

**Added:** `with` statement for FortigateAPI and Fortigate.

**Fixed:** setup.py, ModuleNotFoundError: No module named requests.


----------------------------------------------------------------------------------------

.. _`FortiOS REST API`: https://fndn.fortinet.net/index.php?/fortiapi/1-fortios/