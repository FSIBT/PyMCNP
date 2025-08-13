import re

from . import _card
from .. import types
from .. import errors


class Sd(_card.Card):
    """
    Represents INP `sd` cards.
    """

    _KEYWORD = 'sd'

    _ATTRS = {
        'suffix': types.Integer,
        'information': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Asd(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, information: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Sd`.

        Parameters:
            suffix: Data card option suffix.
            information: Area, volume, or mass by segmented, surface/cell.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.information: types.Tuple(types.Real) = information

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

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def information(self) -> types.Tuple(types.Real):
        """
        Area, volume, or mass by segmented, surface/cell

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._information

    @information.setter
    def information(self, information: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `information`.

        Parameters:
            information: Area, volume, or mass by segmented, surface/cell.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if information is not None:
            array = []
            for item in information:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            information = types.Tuple(types.Real)(array)

        if information is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, information)

        self._information: types.Tuple(types.Real) = information
