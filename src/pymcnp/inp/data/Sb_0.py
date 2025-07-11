import re

from . import _option
from ...utils import types
from ...utils import errors


class Sb_0(_option.DataOption):
    """
    Represents INP sb variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        option: Bias kind setting.
        biases: Particle source biases.
    """

    _KEYWORD = 'sb'

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'biases': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Asb(\d+)( [dcvw])?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, biases: list[str] | list[float] | list[types.Real], option: str | types.String = None):
        """
        Initializes ``Sb_0``.

        Parameters:
            suffix: Data card option suffix.
            option: Bias kind setting.
            biases: Particle source biases.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.option: types.String = option
        self.biases: types.Tuple[types.Real] = biases

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
    def option(self) -> types.String:
        """
        Gets ``option``.

        Returns:
            ``option``.
        """

        return self._option

    @option.setter
    def option(self, option: str | types.String) -> None:
        """
        Sets ``option``.

        Parameters:
            option: Bias kind setting.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if option is not None:
            if isinstance(option, types.String):
                option = option
            elif isinstance(option, str):
                option = types.String.from_mcnp(option)
            else:
                raise TypeError

        if option is not None and option not in {'d', 'c', 'v', 'w'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, option)

        self._option: types.String = option

    @property
    def biases(self) -> types.Tuple[types.Real]:
        """
        Gets ``biases``.

        Returns:
            ``biases``.
        """

        return self._biases

    @biases.setter
    def biases(self, biases: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``biases``.

        Parameters:
            biases: Particle source biases.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if biases is not None:
            array = []
            for item in biases:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Real(item))
                elif isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
                else:
                    raise TypeError
            biases = types.Tuple(array)

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, biases)

        self._biases: types.Tuple[types.Real] = biases
