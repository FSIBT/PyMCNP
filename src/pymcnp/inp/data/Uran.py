import re

from . import _option
from ...utils import types
from ...utils import errors


class Uran(_option.DataOption):
    """
    Represents INP uran elements.
    """

    _KEYWORD = 'uran'

    _ATTRS = {
        'transformations': types.Tuple[types.Stochastic],
    }

    _REGEX = re.compile(r'\Auran((?: \S+ \S+ \S+ \S+)+?)\Z')

    def __init__(self, transformations: list[str] | list[types.Stochastic]):
        """
        Initializes ``Uran``.

        Parameters:
            transformations: Tuple of stochastic transformations.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.transformations: types.Tuple[types.Stochastic] = transformations

    @property
    def transformations(self) -> types.Tuple[types.Stochastic]:
        """
        Tuple of stochastic transformations

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._transformations

    @transformations.setter
    def transformations(self, transformations: list[str] | list[types.Stochastic]) -> None:
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
                if isinstance(item, types.Stochastic):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Stochastic.from_mcnp(item))

            transformations = types.Tuple(array)

        if transformations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, transformations)

        self._transformations: types.Tuple[types.Stochastic] = transformations
