import re

from . import _option
from ... import types
from ... import errors


class Embdb(_option.DataOption):
    """
    Represents INP embdb elements.
    """

    _KEYWORD = 'embdb'

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Aembdb(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, bounds: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Embdb``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Tuple of upper dose energy bounds.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.bounds: types.Tuple(types.Real) = bounds

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

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def bounds(self) -> types.Tuple(types.Real):
        """
        Tuple of upper dose energy bounds

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._bounds

    @bounds.setter
    def bounds(self, bounds: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``bounds``.

        Parameters:
            bounds: Tuple of upper dose energy bounds.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if bounds is not None:
            array = []
            for item in bounds:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            bounds = types.Tuple(types.Real)(array)

        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bounds)

        self._bounds: types.Tuple(types.Real) = bounds
