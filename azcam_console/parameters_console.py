"""
Parameter handling tool for azcam-console.
"""

import typing

import azcam
from azcam.parameters import Parameters


class ParametersConsole(Parameters):
    """
    Main class for parameters tool.
    """

    def __init__(self, default_dictname: str = "azcamconsole"):
        """
        Creates parameters tool, optionally setting default parameter dictionary name.
        """

        Parameters.__init__(self, "azcamconsole")

    def get_par(self, parameter: str) -> typing.Any:
        """
        Return the value of a parameter in the parameters dictionary.


        Args:
            parameter (str): name of the parameter

        Returns:
            value (Any): value of the parameter
        """

        parameter = parameter.lower()
        value = None

        try:
            reply = azcam.db.tools["server"].command(f"parameters.get_par {parameter}")
        except azcam.AzcamError:
            return
        _, value = azcam.utils.get_datatype(reply)
        return value

    def set_par(self, parameter: str, value: typing.Any = None) -> None:
        """
        Set the value of a parameter in the parameters dictionary.

        Args:
            parameter (str): name of the parameter
            value (Any): value of the parameter. Defaults to None.
        Returns:
            None
        """

        parameter = parameter.lower()

        try:
            azcam.db.tools["server"].command(f"parameters.set_par {parameter} {value}")
        except azcam.AzcamError:
            return
        return None
