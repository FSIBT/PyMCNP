import re

from . import _option
from ...utils import types
from ...utils import errors


class Ds_2(_option.DataOption):
    """
    Represents INP ds variation #2 elements.
    """

    _KEYWORD = 'ds'

    _ATTRS = {
        'suffix': types.Integer,
        'vss': types.Tuple[types.IndependentDependent],
    }

    _REGEX = re.compile(rf'\Ads(\d+) q((?: {types.IndependentDependent._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, vss: list[str] | list[types.IndependentDependent]):
        """
        Initializes ``Ds_2``.

        Parameters:
            suffix: Data card option suffix.
            vss: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.vss: types.Tuple[types.IndependentDependent] = vss

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
    def vss(self) -> types.Tuple[types.IndependentDependent]:
        """
        Dependent source independent & dependent variables

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._vss

    @vss.setter
    def vss(self, vss: list[str] | list[types.IndependentDependent]) -> None:
        """
        Sets ``vss``.

        Parameters:
            vss: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if vss is not None:
            array = []
            for item in vss:
                if isinstance(item, types.IndependentDependent):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.IndependentDependent.from_mcnp(item))
            vss = types.Tuple(array)

        if vss is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vss)

        self._vss: types.Tuple[types.IndependentDependent] = vss

    def to_mcnp(self):
        """
        Generates INP from ``Ds_2``.

        Returns:
            INP for ``Ds_2``.
        """
        return f'ds{self.suffix} q {self.vss}'
