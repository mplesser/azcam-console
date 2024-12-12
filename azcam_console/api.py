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
