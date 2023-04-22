"""Helpers."""

CONFIG_JUNOS = """
A1 {
    B1 {
        C1 {
            D1
            D2
        }
        C2 {
            D3
            D4
        }
        B1 {
            D3
        }
    }
    B2 {
        C3 {
            D5
            D6
        }
        C4
    }
    B3 {
        C5 {
            D7
            D8
        }
        A1 {
            D1
            D2
        }
        B1 {
            D3
            D4
        }
        B2 {
            D5
            D6
        }
    }
    B11 {
        C11 {
            D11
        }
    }
}
"""

CONFIG_FGT_DUMMY = """
# config section without edit items
config system A1
    set value B1
    # value with new-line
    set buffer "
line B2 1
line B2 2
"
end

# config section with edit items
config system A2
    # param is quoted
    edit "B1"
        # value is quoted
        set value "C1"
    next
end

config system A3
    # param is not quoted
    edit B1
        # value is not quoted
        set value C1
        # param with dash
        config D-1
            # edit without value
            edit E1
            next
            # edit with value
            edit E2
                set value F1
            next
        end
    next
end

# config section without params
config system A4
end
"""
CONFIG_JFGT_DUMMY = """
config system A1 {
    set value B1
    set buffer "
line B2 1
line B2 2
"
}
end
config system A2 {
    edit "B1" {
        set value "C1"
    }
    next
}
end
config system A3 {
    edit B1 {
        set value C1
        config D-1 {
            edit E1 {
            }
            next
            edit E2 {
                set value F1
            }
            next
        }
        end
    }
    next
}
end
config system A4 {
}
end
""".strip()
CONFIG_JFGT_DUMMY2 = """
config system A1
    set value B1
    set buffer "
    line B2 1
    line B2 2
    "
end
config system A2
    edit "B1"
        set value "C1"
    next
end
config system A3
    edit B1
        set value C1
        config D-1
            edit E1
            next
            edit E2
                set value F1
            next
        end
    next
end
config system A4
end
""".strip()

CONFIG_FGT = """
#config-version=FG100F-6.4.5-FW-build1828-210218:opmode=1:vdom=0:user=TACACS_ADMIN
#conf_file_ver=1969083591884498
#buildno=5651
#global_vdom=1
config system global
    set admin-console-timeout 300
    set hostname "FortiGate"
end

config system interface
    edit "dmz"
        set vdom "root"
        set mode dhcp
        set allowaccess ping https fgfm fabric
        set status down
        set type physical
        set role dmz
        set snmp-index 1
    next
    edit "mgmt"
        set ip 10.0.0.1 255.255.255.0
        set allowaccess ping https ssh snmp fgfm
        set type physical
        set dedicated-to management
        set lldp-reception enable
        set lldp-transmission enable
        set role lan
        set snmp-index 2
    next
    edit "wan1"
        set vdom "root"
        set mode dhcp
        set status down
        set type physical
        set role wan
        set snmp-index 3
    next
    edit "ha1"
        set vdom "root"
        set type physical
        set snmp-index 5
    next
    edit "ha2"
        set vdom "root"
        set type physical
        set snmp-index 6
    next
    edit "port1"
        set vdom "root"
        set type physical
        set snmp-index 7
    next
    edit "port2"
        set vdom "root"
        set type physical
        set snmp-index 8
    next
    edit "ae1"
        set vdom "root"
        set type aggregate
        set member "port1" "port2"
        set device-identification enable
        set lldp-reception enable
        set lldp-transmission enable
        set monitor-bandwidth enable
        set snmp-index 9
    next
    edit "ae1.2"
        set vdom "root"
        set dhcp-relay-service enable
        set ip 10.0.2.1 255.255.255.0
        set allowaccess ping
        set description "description2"
        set alias "alias2"
        set device-identification enable
        set role lan
        set snmp-index 10
        set secondary-IP enable
        set dhcp-relay-ip "10.1.1.1" "10.1.1.2"
        set interface "ae1"
        set vlanid 2
    next
end

config system replacemsg admin "pre_admin-disclaimer-text"
    set buffer "
%%%%%%%%%%%%%%%% * * * W A R N I N G * * * %%%%%%%%%%%%%%%%
%      This system is restricted to authorized users      %
%                 for authorized use only.                %
%        Unauthorized access is strictly prohibited.      %
%    All access and use may be monitored and recorded.    %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"
end
"""
CONFIG_JFGT = """
config system global {
    set admin-console-timeout 300
    set hostname "FortiGate"
}
end
config system interface {
    edit "dmz" {
        set vdom "root"
        set mode dhcp
        set allowaccess ping https fgfm fabric
        set status down
        set type physical
        set role dmz
        set snmp-index 1
    }
    next
    edit "mgmt" {
        set ip 10.0.0.1 255.255.255.0
        set allowaccess ping https ssh snmp fgfm
        set type physical
        set dedicated-to management
        set lldp-reception enable
        set lldp-transmission enable
        set role lan
        set snmp-index 2
    }
    next
    edit "wan1" {
        set vdom "root"
        set mode dhcp
        set status down
        set type physical
        set role wan
        set snmp-index 3
    }
    next
    edit "ha1" {
        set vdom "root"
        set type physical
        set snmp-index 5
    }
    next
    edit "ha2" {
        set vdom "root"
        set type physical
        set snmp-index 6
    }
    next
    edit "port1" {
        set vdom "root"
        set type physical
        set snmp-index 7
    }
    next
    edit "port2" {
        set vdom "root"
        set type physical
        set snmp-index 8
    }
    next
    edit "ae1" {
        set vdom "root"
        set type aggregate
        set member "port1" "port2"
        set device-identification enable
        set lldp-reception enable
        set lldp-transmission enable
        set monitor-bandwidth enable
        set snmp-index 9
    }
    next
    edit "ae1.2" {
        set vdom "root"
        set dhcp-relay-service enable
        set ip 10.0.2.1 255.255.255.0
        set allowaccess ping
        set description "description2"
        set alias "alias2"
        set device-identification enable
        set role lan
        set snmp-index 10
        set secondary-IP enable
        set dhcp-relay-ip "10.1.1.1" "10.1.1.2"
        set interface "ae1"
        set vlanid 2
    }
    next
}
end
config system replacemsg admin "pre_admin-disclaimer-text" {
    set buffer "
%%%%%%%%%%%%%%%% * * * W A R N I N G * * * %%%%%%%%%%%%%%%%
%      This system is restricted to authorized users      %
%                 for authorized use only.                %
%        Unauthorized access is strictly prohibited.      %
%    All access and use may be monitored and recorded.    %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"
}
end
""".strip()

BLOCK_A1 = """
config system A1
    set value B1
    set buffer "
    line B2 1
    line B2 2
    "
""".strip("\n")
BLOCK_A2 = """
config system A2
    edit "B1"
        set value "C1"
    next
""".strip("\n")
BLOCK_E2 = """
            edit E2
                set value F1
""".strip("\n")

JOINED1 = """
    edit "B1"
        set value "C1"
    next
""".strip("\n")
JOINED2 = """
        set value "C1"
""".strip("\n")
