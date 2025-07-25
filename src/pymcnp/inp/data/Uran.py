import re

from . import uran
from . import _option
from ... import types
from ... import errors


class Uran(_option.DataOption):
    """
    Represents INP uran elements.
    """

    _KEYWORD = 'uran'

    _ATTRS = {
        'transformations': types.Tuple(uran.Stochastic),
    }

    _REGEX = re.compile(r'\Auran((?: \S+ \S+ \S+ \S+)+?)\Z', re.IGNORECASE)

    def __init__(self, transformations: list[str] | list[uran.Stochastic]):
        """
        Initializes ``Uran``.

        Parameters:
            transformations: Tuple of stochastic transformations.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.transformations: types.Tuple(uran.Stochastic) = transformations

    @property
    def transformations(self) -> types.Tuple(uran.Stochastic):
        """
        Tuple of stochastic transformations

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._transformations

    @transformations.setter
    def transformations(self, transformations: list[str] | list[uran.Stochastic]) -> None:
        """
        Sets ``transformations``.

        Parameters:
            transformations: Tuple of stochastic transformations.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if transformations is not None:
            array = []
            for item in transformations:
                if isinstance(item, uran.Stochastic):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(uran.Stochastic.from_mcnp(item))
            transformations = types.Tuple(uran.Stochastic)(array)

        if transformations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, transformations)

        self._transformations: types.Tuple(uran.Stochastic) = transformations
