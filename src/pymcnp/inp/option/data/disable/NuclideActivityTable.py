import typing

from ..... import abc
from ..Disable import Disable


class NuclideActivityTable(Disable):
    """
    Represents nuclideactivitytable disable data options.

    Attributes:
        keyword: nuclideactivitytable disable data option `NUCLIDE_ACTIVITY_TABLE` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'NUCLIDE_ACTIVITY_TABLE'] | str = abc.Terminal[r'NUCLIDE_ACTIVITY_TABLE']('NUCLIDE_ACTIVITY_TABLE')
