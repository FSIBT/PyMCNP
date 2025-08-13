import re

from . import _card
from .. import types
from .. import errors


class Dxc(_card.Card):
    """
    Represents INP `dxc` cards.
    """

    _KEYWORD = 'dxc'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'probabilities': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Adxc(\d+):(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, designator: str | types.Designator, probabilities: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Dxc`.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            probabilities: Probability of contribution to DXTRAN.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.designator: types.Designator = designator
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

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def designator(self) -> types.Designator:
        """
        Data card particle designator

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets `designator`.

        Parameters:
            designator: Data card particle designator.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, designator)

        self._designator: types.Designator = designator

    @property
    def probabilities(self) -> types.Tuple(types.Real):
        """
        Probability of contribution to DXTRAN

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
            probabilities: Probability of contribution to DXTRAN.

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
