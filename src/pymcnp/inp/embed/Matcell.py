import re

from . import matcell
from . import _option
from ... import types
from ... import errors


class Matcell(_option.EmbedOption):
    """
    Represents INP `matcell` elements.
    """

    _KEYWORD = 'matcell'

    _ATTRS = {
        'pairs': types.Tuple(matcell.Entry),
    }

    _REGEX = re.compile(rf'\Amatcell((?: {matcell.Entry._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, pairs: list[str] | list[matcell.Entry]):
        """
        Initializes `Matcell`.

        Parameters:
            pairs: Tuple of material-cell paris.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.pairs: types.Tuple(matcell.Entry) = pairs

    @property
    def pairs(self) -> types.Tuple(matcell.Entry):
        """
        Tuple of material-cell paris

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._pairs

    @pairs.setter
    def pairs(self, pairs: list[str] | list[matcell.Entry]) -> None:
        """
        Sets `pairs`.

        Parameters:
            pairs: Tuple of material-cell paris.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if pairs is not None:
            array = []
            for item in pairs:
                if isinstance(item, matcell.Entry):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(matcell.Entry.from_mcnp(item))
            pairs = types.Tuple(matcell.Entry)(array)

        if pairs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, pairs)

        self._pairs: types.Tuple(matcell.Entry) = pairs
