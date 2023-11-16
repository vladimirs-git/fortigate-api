
.. :changelog:

CHANGELOG
=========

1.3.0 (2023-11-16)
------------------
* [new] Fortigate.get_l()


1.2.5 (2023-11-06)
------------------
* [fix] Look for a cookie that is named "ccsrftoken" or stars with "ccsrftoken_".


1.2.4 (2023-05-02)
------------------
* [fix] Fortigate._valid_url()


1.2.3 (2023-04-27)
------------------
* [feat] poetry


1.2.2 (2023-04-27)
------------------
* [fix] dependencies
* [feat] actions


1.2.1 (2023-04-26)
------------------
* [feat] FortigateAPI.ExternalResource
* [feat] Fortigate.token
* [fix] Fortigate.__repr__() removed password
* [doc] README.rst
* [refact] FortigateAPI.fgt > FortigateAPI.rest


1.1.1 (2023-03-16)
------------------
* [feat] ./examples/ssh_vdom.py
* [change] README.rst ssh


1.1.0 (2023-03-05)
------------------
* [feat] ciscoconfparse


1.0.2 (2023-02-07)
------------------
* [fix] ccsrftoken for fortios v7


1.0.1 (2022-11-01)
------------------
* [fix] py.typed


1.0.0 (2022-10-29)
------------------
* [feat] SSH
* [feat] HTTPS SSL verify
* [feat] *with* statement for FortigateAPI and Fortigate
* [fix] setup.py, ModuleNotFoundError: No module named requests


0.2.6 (2022-09-01)
------------------
* [feat] dhcp_server


0.2.5 (2022-06-16)
------------------
* [change] delete(uid, kwargs), uid is optional


0.2.4 (2022-06-15)
------------------
* [change] update(data, uid), uid is optional
* [feat] fortigate.py Fortigate.is_connected


0.2.3 (2022-06-13)
------------------
* [change] Fortigate._valid_url()
* [change] tests/test__fortigate.py
* [feat] Fortigate.scheme, "https" or "http"
* [change] Pipfile packages versions


0.2.2 (2022-05-23)
------------------
* [change] Fortigate.login() - return: Fortigate (before was Session)
* [feat] FortigateAPI.vdom - Gets the ability to change the vdom in the same session
* [fix] py.typed, setup.py


0.2.2 (2022-05-21)
------------------
* [change] README.nd changed to README.rst
* [change] renamed unique identifier "name" and "id" replaced to "uid"
* [deleted] FortigateAPI.{object}.delete_name(), replaced by FortigateAPI.{object}.delete(filter)
* [fix] Fortigate.__repr__()
* [feat] FortigateAPI.policy.get(efilter)
* [feat] FortigateAPI.{object}.delete(filter)
* [feat] FortigateAPI.{object}.is_exist()
