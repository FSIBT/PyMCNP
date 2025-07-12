import re

from . import _option
from ...utils import types
from ...utils import errors


class Em(_option.DataOption):
    """
    Represents INP em elements.
    """

    _KEYWORD = 'em'

    _ATTRS = {
        'suffix': types.Integer,
        'multipliers': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aem(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, multipliers: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Em``.

        Parameters:
            suffix: Data card option suffix.
            multipliers: Energy bin multiplier to apply.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.multipliers: types.Tuple[types.Real] = multipliers

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def multipliers(self) -> types.Tuple[types.Real]:
        """
        Energy bin multiplier to apply

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._multipliers

    @multipliers.setter
    def multipliers(self, multipliers: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``multipliers``.

        Parameters:
            multipliers: Energy bin multiplier to apply.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if multipliers is not None:
            array = []
            for item in multipliers:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))

            multipliers = types.Tuple(array)

        if multipliers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, multipliers)

        self._multipliers: types.Tuple[types.Real] = multipliers
