
CiscoConfParse
--------------
Helper that parses the Fortigate configuration to find and modify command lines.
CiscoConfParse doesn't natively support Fortigate configuration,
but after some tweaking in this package it has become a good tool to play with Fortigate config lines.
For more information, see the documentation for the JunosCfgLine object at https://github.com/mpenning/ciscoconfparse


Examples
........
CiscoConfParse examples:

- get config from the Fortigate by SSH
- create CiscoConfParse object
- filter all JunosCfgLine objects of wan interfaces
- print some data in CiscoConfParse objects
- filter all wan interfaces blocks

`./examples/ccp.py`_


.. _`./examples/ccp.py`: ./examples/ccp.py

