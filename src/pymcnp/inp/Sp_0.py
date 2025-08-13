import re

from . import _card
from .. import types
from .. import errors


class Sp_0(_card.Card):
    """
    Represents INP `sp` elements variation #0.
    """

    _KEYWORD = 'sp'

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'probabilities': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Asp(\d+)( [dcvw])?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, probabilities: list[str] | list[float] | list[types.Real], option: str | types.String = None):
        """
        Initializes `Sp_0`.

        Parameters:
            suffix: Data card option suffix.
            option: Probability kind setting.
            probabilities: Particle source probabilities.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.option: types.String = option
        self.probabilities: types.Tuple(types.Real) = probabilities

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

        if suffix is None or not (suffix >= 1 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def option(self) -> types.String:
        """
        Probability kind setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._option

    @option.setter
    def option(self, option: str | types.String) -> None:
        """
        Sets `option`.

        Parameters:
            option: Probability kind setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if option is not None:
            if isinstance(option, types.String):
                option = option
            elif isinstance(option, str):
                option = types.String.from_mcnp(option)

        if option is not None and option.value.lower() not in {'d', 'c', 'v', 'w'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, option)

        self._option: types.String = option

    @property
    def probabilities(self) -> types.Tuple(types.Real):
        """
        Particle source probabilities

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._probabilities

    @probabilities.setter
    def probabilities(self, probabilities: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `probabilities`.

        Parameters:
            probabilities: Particle source probabilities.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if probabilities is not None:
            array = []
            for item in probabilities:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            probabilities = types.Tuple(types.Real)(array)

        if probabilities is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, probabilities)

        self._probabilities: types.Tuple(types.Real) = probabilities
