"""
*azcam.console* is imported to define console mode, create the azcamconsole parameters dictionary, and define a logger.
"""

import azcam
from azcam.logger import Logger
from azcam_console.parameters_console import ParametersConsole
from azcam_console.database_console import AzcamDatabaseConsole

azcam.db = AzcamDatabaseConsole()  # overwrite azcamdatabase

# parameters
azcam.db.parameters = ParametersConsole()

# logging
azcam.db.logger = Logger()
azcam.log = azcam.db.logger.log  # to allow azcam.log()
