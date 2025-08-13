import re

from . import _card
from .. import types
from .. import errors


class Tmp(_card.Card):
    """
    Represents INP `tmp` cards.
    """

    _KEYWORD = 'tmp'

    _ATTRS = {
        'suffix': types.Integer,
        'temperatures': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Atmp(\d+)?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, temperatures: list[str] | list[float] | list[types.Real], suffix: str | int | types.Integer = None):
        """
        Initializes `Tmp`.

        Parameters:
            suffix: Data card option suffix.
            temperatures: Cell temperatrues.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.temperatures: types.Tuple(types.Real) = temperatures

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        self._suffix: types.Integer = suffix

    @property
    def temperatures(self) -> types.Tuple(types.Real):
        """
        Cell temperatrues

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._temperatures

    @temperatures.setter
    def temperatures(self, temperatures: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `temperatures`.

        Parameters:
            temperatures: Cell temperatrues.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if temperatures is not None:
            array = []
            for item in temperatures:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            temperatures = types.Tuple(types.Real)(array)

        if temperatures is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, temperatures)

        self._temperatures: types.Tuple(types.Real) = temperatures
