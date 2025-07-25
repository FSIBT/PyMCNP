import re

from . import _option
from ... import types
from ... import errors


class Elpt(_option.DataOption):
    """
    Represents INP elpt elements.
    """

    _KEYWORD = 'elpt'

    _ATTRS = {
        'cutoffs': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Aelpt((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, cutoffs: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Elpt``.

        Parameters:
            cutoffs: Tuple of cell lower energy cutoffs.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.cutoffs: types.Tuple(types.Real) = cutoffs

    @property
    def cutoffs(self) -> types.Tuple(types.Real):
        """
        Tuple of cell lower energy cutoffs

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cutoffs

    @cutoffs.setter
    def cutoffs(self, cutoffs: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``cutoffs``.

        Parameters:
            cutoffs: Tuple of cell lower energy cutoffs.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cutoffs is not None:
            array = []
            for item in cutoffs:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            cutoffs = types.Tuple(types.Real)(array)

        if cutoffs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoffs)

        self._cutoffs: types.Tuple(types.Real) = cutoffs
