"""
Client console commands for Archon controller.
These methods are added to the controller tool.
"""

import sys
from types import MethodType
import inspect

import azcam
import azcam.utils
import azcam.fits


def get_cds():
    """
    Get the controller CDS values.
    """

    tokens = azcam.db.tools["server"].command("controller.get_cds")

    if not tokens:
        return

    # make lists
    # tokens = azcam.utils.parse(reply)
    taps = []
    gains = []
    offsets = []
    for cds in tokens:
        tokens = cds.split(",")
        taps.append(tokens[0].strip())
        gains.append(float(tokens[1].strip()))
        offsets.append(float(tokens[2].strip()))

    return taps, gains, offsets


def set_cds(taps, gains, offsets):
    """
    Set the controller CDS values.
    :param offsets:
    :param gains:
    :param taps: list of tap names
    """

    # make CDS list
    cdslist = []

    for i, _ in enumerate(taps):
        s = f'"{taps[i]}, {gains[i]:.01f}, {int(offsets[i])}"'
        cdslist.append(s)

    cds = " ".join(cdslist)

    azcam.db.tools["server"].command(f"controller.update_cds '{cds}'")

    return


def set_biaslevels(imagefilename="test.fits", goal=1000):
    """
    Set controller bias levels from zero image.
    :param goal:
    :param imagefilename:
    """

    taps, gains, offsets = get_cds()
    l1 = len(offsets)

    # get FITS image means
    imagemeans = azcam.fits.mean(imagefilename)

    # remap tap order
    tapmeans = l1 * [0.0]
    if l1 == 16:
        tapmeans[15] = imagemeans[15]
        tapmeans[14] = imagemeans[14]
        tapmeans[13] = imagemeans[13]
        tapmeans[12] = imagemeans[12]
        tapmeans[11] = imagemeans[11]
        tapmeans[10] = imagemeans[10]
        tapmeans[9] = imagemeans[9]
        tapmeans[8] = imagemeans[8]

        tapmeans[0] = imagemeans[7]
        tapmeans[1] = imagemeans[6]
        tapmeans[2] = imagemeans[5]
        tapmeans[3] = imagemeans[4]
        tapmeans[4] = imagemeans[3]
        tapmeans[5] = imagemeans[2]
        tapmeans[6] = imagemeans[1]
        tapmeans[7] = imagemeans[0]
    elif l1 == 8:
        tapmeans[0] = imagemeans[0]
        tapmeans[1] = imagemeans[1]
        tapmeans[2] = imagemeans[2]
        tapmeans[3] = imagemeans[3]
        tapmeans[4] = imagemeans[4]
        tapmeans[5] = imagemeans[5]
        tapmeans[6] = imagemeans[6]
        tapmeans[7] = imagemeans[7]
    else:
        tapmeans = []

    newoffsets = []
    for chan, m in enumerate(tapmeans):
        newvalue = offsets[chan] - m + goal
        newoffsets.append(int(newvalue))

    if len(newoffsets) > 0:
        set_cds(taps, gains, newoffsets)

    return newoffsets


def set_offsets(offset=1000):
    """
    Set all channels to the same bias offset.
    :param offset:
    """

    taps, gains, offsets = get_cds()
    l1 = len(offsets)
    offsets = l1 * [offset]

    set_cds(taps, gains, offsets)

    return


# add methods to the controller tool
for mod in inspect.getmembers(sys.modules[__name__]):
    if inspect.isfunction(mod[1]):
        setattr(
            azcam.db.tools["controller"],
            mod[0],
            MethodType(mod[1], azcam.db.tools["controller"]),
        )
