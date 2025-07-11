import re

from . import _option
from ...utils import types
from ...utils import errors


class Ds_1(_option.DataOption):
    """
    Represents INP ds variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        ijs: Dependent source independent & dependent variables.
    """

    _KEYWORD = 'ds'

    _ATTRS = {
        'suffix': types.Integer,
        'ijs': types.Tuple[types.IndependentDependent],
    }

    _REGEX = re.compile(rf'\Ads(\d+) t((?: {types.IndependentDependent._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, ijs: list[str] | list[types.IndependentDependent]):
        """
        Initializes ``Ds_1``.

        Parameters:
            suffix: Data card option suffix.
            ijs: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.ijs: types.Tuple[types.IndependentDependent] = ijs

    def to_mcnp(self):
        """
        Generates INP from ``Ds_1``.

        Returns:
            INP for ``Ds_1``.
        """
        return f'ds{self.suffix} t {self.ijs}'

    @property
    def suffix(self) -> types.Integer:
        """
        Gets ``suffix``.

        Returns:
            ``suffix``.
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
            else:
                raise TypeError

        if suffix is None or not (suffix >= 1 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def ijs(self) -> types.Tuple[types.IndependentDependent]:
        """
        Gets ``ijs``.

        Returns:
            ``ijs``.
        """

        return self._ijs

    @ijs.setter
    def ijs(self, ijs: list[str] | list[types.IndependentDependent]) -> None:
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
                if isinstance(item, types.IndependentDependent):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.IndependentDependent.from_mcnp(item))
                else:
                    raise TypeError
            ijs = types.Tuple(array)

        if ijs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ijs)

        self._ijs: types.Tuple[types.IndependentDependent] = ijs
