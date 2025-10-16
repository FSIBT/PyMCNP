import re

from . import _card
from .. import types
from .. import errors


class Ds_3(_card.Card):
    """
    Represents INP `ds` elements variation #3.
    """

    _KEYWORD = 'ds'

    _ATTRS = {
        'suffix': types.Integer,
        'distributions': types.Tuple(types.Distribution),
    }

    _REGEX = re.compile(rf'\Ads(\d+) s((?: {types.Distribution._REGEX.pattern[2:-2]})+)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, distributions: list[str] | list[types.Distribution]):
        """
        Initializes `Ds_3`.

        Parameters:
            suffix: Data card option suffix.
            distributions: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.distributions: types.Tuple(types.Distribution) = distributions

    def to_mcnp(self):
        """
        Generates INP from `Ds_3`.

        Returns:
            INP for `Ds_3`.
        """
        return f'ds{self.suffix} s {self.distributions}'

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
    def distributions(self) -> types.Tuple(types.Distribution):
        """
        Distribution numbers.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._distributions

    @distributions.setter
    def distributions(self, distributions: list[str] | list[types.Distribution]) -> None:
        """
        Sets `distributions`.

        Parameters:
            distributions: Distribution numbers

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if distributions is not None:
            array = []
            for item in distributions:
                if isinstance(item, types.Distribution):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Distribution.from_mcnp(item))
            distributions = types.Tuple(types.Distribution)(array)

        if distributions is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, distributions)

        self._distributions: types.Tuple(types.Distribution) = distributions
