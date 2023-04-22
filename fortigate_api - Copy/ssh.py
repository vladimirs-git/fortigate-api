"""SSH connector to the Fortigate.
Contains methods to get and put configuration commands using ssh
"""

from netmiko import ConnectHandler  # type: ignore

from fortigate_api.types_ import DAny, UStr


class SSH:
    """SSH connector to the Fortigate.
    Contains methods to get and put configuration commands using ssh
    """

    def __init__(self, host: str, username: str = "", password: str = "", **kwargs):
        """SSH
        ::
            :param host: Firewall ip address or hostname
            :type host: str

            :param username: Administrator name
            :type username: str

            :param password: Administrator password
            :type password: str

            :param ssh: Netmiko *ConnectHandler* parameters
            :type ssh: Dict[str, Any]
        """
        ssh_kwargs: DAny = dict(kwargs.get("ssh") or {})
        ssh_kwargs.update(dict(
            device_type="fortinet",
            auto_connect=False,
        ))
        self.session = ConnectHandler(host=host,
                                      username=username,
                                      password=password,
                                      **ssh_kwargs)

    def __enter__(self):
        self.login()
        return self

    def __exit__(self, *args):
        self.logout()

    # ============================ login =============================

    def login(self) -> None:
        """Login to Fortigate using SSH"""
        if self.session.remote_conn:
            return
        # noinspection PyProtectedMember
        self.session._open()
        if not self.session.remote_conn:
            raise ConnectionError("Cannot open remote connection")

    def logout(self) -> None:
        """Logout from the Fortigate using SSH"""
        if self.session.remote_conn:
            self.session.cleanup()
            self.session.remote_conn = None

    # =========================== methods ============================

    def send_command(self, cmd: str, **kwargs) -> str:
        """Sends the command to the Fortigate
        ::
            :param cmd: The command to be executed on the Fortigate
            :type cmd: str

            :param kwargs: (optional) Netmiko parameters
            :type kwargs: Dict[str, Any]

            :return: Output of the command
            :rtype: str
        """
        self.login()
        output = self.session.send_command(cmd, **kwargs)
        return str(output)

    def send_config_set(self, cmds: UStr, **kwargs) -> str:
        """Sends configuration commands to the Fortigate
        ::
            :param cmds: Configuration commands to be executed on the Fortigate
            :type cmds: List[str], str

            :param kwargs: (optional) Netmiko parameters
            :type kwargs: Dict[str, Any]

            :return: Output of the commands
            :rtype: str
        """
        self.login()
        if isinstance(cmds, str):
            cmds = [cmds]
        cmds_ = list(cmds)

        output = self.session.send_config_set(cmds_, **kwargs)
        return str(output)
