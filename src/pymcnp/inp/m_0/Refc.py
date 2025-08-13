import re

from . import _option
from ... import types
from ... import errors


class Refc(_option.MOption_0):
    """
    Represents INP `refc` elements.
    """

    _KEYWORD = 'refc'

    _ATTRS = {
        'coefficents': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Arefc((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, coefficents: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Refc`.

        Parameters:
            coefficents: Cauchy coefficents.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.coefficents: types.Tuple(types.Real) = coefficents

    @property
    def coefficents(self) -> types.Tuple(types.Real):
        """
        Cauchy coefficents

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._coefficents

    @coefficents.setter
    def coefficents(self, coefficents: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `coefficents`.

        Parameters:
            coefficents: Cauchy coefficents.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if coefficents is not None:
            array = []
            for item in coefficents:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            coefficents = types.Tuple(types.Real)(array)

        if coefficents is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, coefficents)

        self._coefficents: types.Tuple(types.Real) = coefficents
