"""
AzCam is a software framework for the acquisition and analysis of image data
from scientific imaging systems as well as the control of instrumentation.
It is intended to be customized for specific hardware, observational,
and data reduction requirements.
"""

from importlib import metadata

__version__ = metadata.version(__package__)
__version_info__ = tuple(int(i) for i in __version__.split(".") if i.isdigit())

import typing
from typing import List, Dict

# initially azcam.log() is print(), will usually be overwritten
log: typing.Callable = print

mode = "unknown"
"""azcam mode, usually server or console"""

# clean namespace
del metadata
del typing


import azcam_console.console
