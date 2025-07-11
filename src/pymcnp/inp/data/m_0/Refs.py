import re

from . import _option
from ....utils import types
from ....utils import errors


class Refs(_option.MOption_0):
    """
    Represents INP refs elements.

    Attributes:
        coefficents: Sellmeier coefficents.
    """

    _KEYWORD = 'refs'

    _ATTRS = {
        'coefficents': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Arefs((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, coefficents: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Refs``.

        Parameters:
            coefficents: Sellmeier coefficents.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.coefficents: types.Tuple[types.Real] = coefficents

    @property
    def coefficents(self) -> types.Tuple[types.Real]:
        """
        Gets ``coefficents``.

        Returns:
            ``coefficents``.
        """

        return self._coefficents

    @coefficents.setter
    def coefficents(self, coefficents: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``coefficents``.

        Parameters:
            coefficents: Sellmeier coefficents.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if coefficents is not None:
            array = []
            for item in coefficents:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Real(item))
                elif isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
                else:
                    raise TypeError
            coefficents = types.Tuple(array)

        if coefficents is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, coefficents)

        self._coefficents: types.Tuple[types.Real] = coefficents
