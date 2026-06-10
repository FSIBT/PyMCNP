import typing
import dataclasses

from ..... import abc
from ..Disable import Disable


class NuclideActivityTable(Disable):
    """
    Represents nuclideactivitytable disable data options.

    Attributes:
        keyword: nuclideactivitytable disable data option `NUCLIDE_ACTIVITY_TABLE` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NUCLIDE_ACTIVITY_TABLE'] | str = abc.Terminal[r'NUCLIDE_ACTIVITY_TABLE']('NUCLIDE_ACTIVITY_TABLE')
