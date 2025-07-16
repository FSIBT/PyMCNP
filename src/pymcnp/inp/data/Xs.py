import re

from . import _option
from ... import types
from ... import errors


class Xs(_option.DataOption):
    """
    Represents INP xs elements.
    """

    _KEYWORD = 'xs'

    _ATTRS = {
        'suffix': types.Integer,
        'weight_ratios': types.Tuple[types.Substance],
    }

    _REGEX = re.compile(rf'\Axs(\d+)((?: {types.Substance._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, weight_ratios: list[str] | list[types.Substance]):
        """
        Initializes ``Xs``.

        Parameters:
            suffix: Data card option suffix.
            weight_ratios: Tuple of atomic weight ratios.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.weight_ratios: types.Tuple[types.Substance] = weight_ratios

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
    def weight_ratios(self) -> types.Tuple[types.Substance]:
        """
        Tuple of atomic weight ratios

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._weight_ratios

    @weight_ratios.setter
    def weight_ratios(self, weight_ratios: list[str] | list[types.Substance]) -> None:
        """
        Sets ``weight_ratios``.

        Parameters:
            weight_ratios: Tuple of atomic weight ratios.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if weight_ratios is not None:
            array = []
            for item in weight_ratios:
                if isinstance(item, types.Substance):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Substance.from_mcnp(item))
            weight_ratios = types.Tuple(array)

        if weight_ratios is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, weight_ratios)

        self._weight_ratios: types.Tuple[types.Substance] = weight_ratios
