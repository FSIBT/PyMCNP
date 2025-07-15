import re

from . import ds_1
from . import _option
from ...utils import types
from ...utils import errors


class Ds_1(_option.DataOption):
    """
    Represents INP ds variation #1 elements.
    """

    _KEYWORD = 'ds'

    _ATTRS = {
        'suffix': types.Integer,
        'ijs': types.Tuple[ds_1.Variables],
    }

    _REGEX = re.compile(rf'\Ads(\d+) t((?: {ds_1.Variables._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, ijs: list[str] | list[ds_1.Variables]):
        """
        Initializes ``Ds_1``.

        Parameters:
            suffix: Data card option suffix.
            ijs: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.ijs: types.Tuple[ds_1.Variables] = ijs

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

        if suffix is None or not (suffix >= 1 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def ijs(self) -> types.Tuple[ds_1.Variables]:
        """
        Dependent source independent & dependent variables

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ijs

    @ijs.setter
    def ijs(self, ijs: list[str] | list[ds_1.Variables]) -> None:
        """
        Sets ``ijs``.

        Parameters:
            ijs: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ijs is not None:
            array = []
            for item in ijs:
                if isinstance(item, ds_1.Variables):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(ds_1.Variables.from_mcnp(item))
            ijs = types.Tuple(array)

        if ijs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ijs)

        self._ijs: types.Tuple[ds_1.Variables] = ijs

    def to_mcnp(self):
        """
        Generates INP from ``Ds_1``.

        Returns:
            INP for ``Ds_1``.
        """
        return f'ds{self.suffix} t {self.ijs}'
