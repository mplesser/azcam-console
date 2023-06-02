"""
CLI shortcuts for azcam-console.
"""


import azcam
import azcam_console


def bf():
    """Shortcut for file_browser()."""

    folder = azcam_console.utils.file_browser("", "folder", "Select folder")
    if folder == []:
        return
    if isinstance(folder, list):
        folder = folder[0]
    azcam.utils.curdir(folder)

    return folder


def sf_console():
    """Shortcut to set image folder"""

    try:
        folder = azcam.utils.curdir()
        azcam.db.parameters.set_par("imagefolder", folder)
    except Exception:
        pass

    return


def gf_console():
    """
    Shortcut to goto image folder.
    Also issues sav() command to save folder location.
    """

    folder = azcam.db.parameters.get_par("imagefolder")
    azcam.utils.curdir(folder)
    azcam.db.wd = folder
    sav_console()

    return


def sav_console():
    """Shortcut for parfile_write() saving current folder in database."""

    azcam.db.parameters.set_script_par("azcamconsole", "wd", azcam.utils.curdir())
    azcam.db.parameters.update_par_dict("azcamconsole")
    azcam.db.parameters.write_parfile()

    return


def sroi():
    """Alias for set_image_roi()."""
    azcam.utils.set_image_roi()


# add to shortcuts
azcam.db.shortcuts.update(
    {"sav": sav_console, "sroi": sroi, "sf": sf_console, "gf": gf_console, "bf": bf}
)
