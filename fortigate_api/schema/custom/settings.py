"""Custom models."""
from fortigate_api.types_ import DAny

SETTINGS: DAny = {
    "cmdb": {
        "antivirus": {
            "profile": {
                "path_ui": "ng/utm/antivirus/profile",
            },
        },
        "application": {
            "list": {
                "path_ui": "ng/utm/appctrl/sensor",
            },
        },
        "firewall": {
            "address": {
                "path_ui": "ng/firewall/address",
            },
            "addrgrp": {
                "path_ui": "ng/firewall/address",
            },
            "internet-service": {
                "path_ui": "ng/firewall/internet_service",
            },
            "ippool": {
                "path_ui": "ng/firewall/ip-pool",
            },
            "policy": {
                "is_custom_model": True,
            },
            "vip": {
                "path_ui": "ng/firewall/virtual-ip",
            },
        },
        "firewall.schedule": {
            "onetime": {
                "path_ui": "ng/firewall/schedule",
            },
        },
        "firewall.service": {
            "category": {
                "path_ui": "ng/firewall/service",
            },
            "custom": {
                "path_ui": "ng/firewall/service",
            },
            "group": {
                "path_ui": "ng/firewall/service",
            },
        },
        "system": {
            "external-resource": {
                "path_ui": "ng/external-connector",
            },
            "interface": {
                "is_custom_model": True,
            },
            "vdom": {
                "path_ui": "ng/system/vdom",
            },
            "zone": {
                "path_ui": "ng/interface",
            },
        },
        "system.dhcp": {
            "server": {
                "path_ui": "ng/interface/edit/{name}",
            },
        },
        "system.snmp": {
            "community": {
                "path_ui": "ng/system/snmp",
            },
        },
    },
    "log": {},
    "monitor": {},
}
