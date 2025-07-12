import re

from . import _option
from ....utils import types
from ....utils import errors


class Matcell(_option.EmbedOption):
    """
    Represents INP matcell elements.
    """

    _KEYWORD = 'matcell'

    _ATTRS = {
        'pairs': types.Tuple[types.Matcell],
    }

    _REGEX = re.compile(rf'\Amatcell((?: {types.Matcell._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, pairs: list[str] | list[types.Matcell]):
        """
        Initializes ``Matcell``.

        Parameters:
            pairs: Tuple of material-cell paris.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.pairs: types.Tuple[types.Matcell] = pairs

    @property
    def pairs(self) -> types.Tuple[types.Matcell]:
        """
        Tuple of material-cell paris

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._pairs

    @pairs.setter
    def pairs(self, pairs: list[str] | list[types.Matcell]) -> None:
        """
        Sets ``pairs``.

        Parameters:
            pairs: Tuple of material-cell paris.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if pairs is not None:
            array = []
            for item in pairs:
                if isinstance(item, types.Matcell):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Matcell.from_mcnp(item))

            pairs = types.Tuple(array)

        if pairs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, pairs)

        self._pairs: types.Tuple[types.Matcell] = pairs
