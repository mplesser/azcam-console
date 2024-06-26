"""
AzCam is a software framework for the acquisition and analysis of image data
from scientific imaging systems as well as the control of instrumentation.
"""

import typing
from typing import List, Dict
from importlib import metadata
from azcam_console import utils

__version__ = metadata.version(__package__)
__version_info__ = tuple(int(i) for i in __version__.split(".") if i.isdigit())

from azcam.logger import AzCamLogger

from azcam_console.database_console import AzcamDatabaseConsole

logger: AzCamLogger = AzCamLogger()

# initially azcam.log() is print() but will usually be overwritten
log: typing.Callable = print

# initial database but will ususally be overwritten by server or console
db: AzcamDatabaseConsole = AzcamDatabaseConsole()

mode = "console"
"""azcam mode, usually server or console"""

import azcam_console.console

# cleanup namespace
del metadata
del typing
del AzCamLogger
del AzcamDatabaseConsole
