
.. :changelog:

CHANGELOG
=========

1.0.2 (2023-02-07)
------------------
* [fix] ccsrftoken for fortios v7


1.0.1 (2022-11-01)
------------------
* [fix] py.typed


1.0.0 (2022-10-29)
------------------
* [new] SSH
* [new] HTTPS SSL verify
* [new] *with* statement for FortigateAPI and Fortigate
* [fix] setup.py, ModuleNotFoundError: No module named requests


0.2.6 (2022-09-01)
------------------
* [new] dhcp_server


0.2.5 (2022-06-16)
------------------
* [change] delete(uid, kwargs), uid is optional


0.2.4 (2022-06-15)
------------------
* [change] update(data, uid), uid is optional
* [new] fortigate.py Fortigate.is_connected


0.2.3 (2022-06-13)
------------------
* [change] Fortigate._valid_url()
* [change] tests/test__fortigate.py
* [new] Fortigate.scheme, "https" or "http"
* [change] Pipfile packages versions


0.2.2 (2022-05-23)
------------------
* [change] Fortigate.login() - return: Fortigate (before was Session)
* [new] FortigateAPI.vdom - Gets the ability to change the vdom in the same session
* [fix] py.typed, setup.py


0.2.2 (2022-05-21)
------------------
* [change] README.nd changed to README.rst
* [change] renamed unique identifier "name" and "id" replaced to "uid"
* [deleted] FortigateAPI.{object}.delete_name(), replaced by FortigateAPI.{object}.delete(filter)
* [fix] Fortigate.__repr__()
* [new] FortigateAPI.policy.get(efilter)
* [new] FortigateAPI.{object}.delete(filter)
* [new] FortigateAPI.{object}.is_exist()
