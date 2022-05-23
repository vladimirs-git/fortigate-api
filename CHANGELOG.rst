
.. :changelog:

CHANGELOG
=========

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
