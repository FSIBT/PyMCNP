import re

from . import _option
from ... import types
from ... import errors


class Cel(_option.SswOption):
    """
    Represents INP `cel` elements.
    """

    _KEYWORD = 'cel'

    _ATTRS = {
        'cfs': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Acel((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, cfs: list[str] | list[int] | list[types.Integer]):
        """
        Initializes `Cel`.

        Parameters:
            cfs: Cells from which KCODE neutrons are written.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.cfs: types.Tuple(types.Integer) = cfs

    @property
    def cfs(self) -> types.Tuple(types.Integer):
        """
        Cells from which KCODE neutrons are written

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cfs

    @cfs.setter
    def cfs(self, cfs: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `cfs`.

        Parameters:
            cfs: Cells from which KCODE neutrons are written.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cfs is not None:
            array = []
            for item in cfs:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            cfs = types.Tuple(types.Integer)(array)

        if cfs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cfs)

        self._cfs: types.Tuple(types.Integer) = cfs
