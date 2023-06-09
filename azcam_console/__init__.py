"""
*azcam_console* supports python client code for the AzCam image acquisition and analysis package.
"""

from importlib import metadata

__version__ = metadata.version(__package__)
__version_info__ = tuple(int(i) for i in __version__.split(".") if i.isdigit())

import typing
from typing import List, Dict

# import here so future importing is not required
from azcam_console import utils

# initially azcam.log() is print(), will usually be overwritten
log: typing.Callable = print

mode = "unknown"
"""azcam mode, usually server or console"""

# clean namespace
del metadata
del typing


import azcam_console.console
