.. :changelog:

CHANGELOG
=========

0.1.2 (2022-05-21)
------------------
* [change] README.nd changed to README.rst
* [change] renamed unique identifier "name" and "id" replaced to "uid"
* [deleted] FortigateAPI.{object}.delete_name(), replaced by FortigateAPI.{object}.delete(filter)
* [fix] Fortigate.__repr__()
* [new] FortigateAPI.policy.get(efilter)
* [new] FortigateAPI.{object}.delete(filter)
* [new] FortigateAPI.{object}.is_exist()
