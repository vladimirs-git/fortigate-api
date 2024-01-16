"""Cmdb/user/adgrp connector."""

from fortigate_api.connector import Connector


class AdgrpUC(Connector):
    """Cmdb/user/adgrp connector."""

    uid = "name"
    _path = "api/v2/cmdb/user/adgrp"
