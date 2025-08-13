import re

from . import ds_2
from . import _card
from .. import types
from .. import errors


class Ds_2(_card.Card):
    """
    Represents INP `ds` elements variation #2.
    """

    _KEYWORD = 'ds'

    _ATTRS = {
        'suffix': types.Integer,
        'vss': types.Tuple(ds_2.Variables),
    }

    _REGEX = re.compile(rf'\Ads(\d+) q((?: {ds_2.Variables._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, vss: list[str] | list[ds_2.Variables]):
        """
        Initializes `Ds_2`.

        Parameters:
            suffix: Data card option suffix.
            vss: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.vss: types.Tuple(ds_2.Variables) = vss

    def to_mcnp(self):
        """
        Generates INP from `Ds_2`.

        Returns:
            INP for `Ds_2`.
        """
        return f'ds{self.suffix} q {self.vss}'

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
    def vss(self) -> types.Tuple(ds_2.Variables):
        """
        Dependent source independent & dependent variables

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._vss

    @vss.setter
    def vss(self, vss: list[str] | list[ds_2.Variables]) -> None:
        """
        Sets `vss`.

        Parameters:
            vss: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if vss is not None:
            array = []
            for item in vss:
                if isinstance(item, ds_2.Variables):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(ds_2.Variables.from_mcnp(item))
            vss = types.Tuple(ds_2.Variables)(array)

        if vss is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, vss)

        self._vss: types.Tuple(ds_2.Variables) = vss
