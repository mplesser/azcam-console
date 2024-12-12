import azcam


class API(object):
    """
    API class for console to communicate with azcamserver.
    """

    def __init__(self) -> None:
        pass

    def command(self, command: str):
        """
        Send a command to azcamserver API and return the reply.
        """

        if command.startswith("api"):
            cmd = command
        else:
            cmd = f"api.{command}"

        reply = azcam.db.server.command(cmd)

        return reply

    def set_shutter(self, state: int = 0, shutter_id: int = 0):
        """
        Open or close a shutter.

        Args:
            state: 1 to open shutter or 0 to close
            shutter_id: shutter ID flag

                * 0 => controller default shutter.
                * 1 => instrument default shutter.
        """

        return self.command(f"set_shutter {state} {shutter_id}")

    def get_temperatures(self) -> list[float]:
        """
        Return all system temperatures.

        Returns:
            temperatures: list of temperatures read
        """

        temps = self.command(f"get_temperatures")

        reply = [float(x) for x in temps]

        return reply

    def set_control_temperature(
        self, temperature: float | None = None, temperature_id: int = -1
    ) -> None:
        """
        Set the control temperature (set point).

        Args:
            temperature: control temperature in Celsius. If not specified, use saved value
            temperature_id: control temperature sensor number
        """

        if temperature is None:
            temperature = "None"

        return self.command(f"set_control_temperature {temperature} {temperature_id}")

    def get_control_temperature(self, temperature_id: int = -1) -> float:
        """
        Get the control temperature (set point).

        Args:
            temperature_id: temperature sensor identifier

        Returns:
            control_temperature: control temperature
        """

        temp = self.command(f"get_control_temperature {temperature_id}")

        return float(temp)
