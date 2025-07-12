import re

from . import _option
from ...utils import types
from ...utils import errors


class Si_0(_option.DataOption):
    """
    Represents INP si variation #0 elements.
    """

    _KEYWORD = 'si'

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'information': types.Tuple[types.DistributionNumber],
    }

    _REGEX = re.compile(rf'\Asi(\d+)( {types.String._REGEX.pattern[2:-2]})?((?: {types.DistributionNumber._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, information: list[str] | list[types.DistributionNumber], option: str | types.String = None):
        """
        Initializes ``Si_0``.

        Parameters:
            suffix: Data card option suffix.
            option: Information kind setting.
            information: Particle source information.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.option: types.String = option
        self.information: types.Tuple[types.DistributionNumber] = information

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

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def option(self) -> types.String:
        """
        Information kind setting

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._option

    @option.setter
    def option(self, option: str | types.String) -> None:
        """
        Sets ``option``.

        Parameters:
            option: Information kind setting.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if option is not None:
            if isinstance(option, types.String):
                option = option
            elif isinstance(option, str):
                option = types.String.from_mcnp(option)

        self._option: types.String = option

    @property
    def information(self) -> types.Tuple[types.DistributionNumber]:
        """
        Particle source information

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._information

    @information.setter
    def information(self, information: list[str] | list[types.DistributionNumber]) -> None:
        """
        Sets ``information``.

        Parameters:
            information: Particle source information.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if information is not None:
            array = []
            for item in information:
                if isinstance(item, types.DistributionNumber):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.DistributionNumber.from_mcnp(item))

            information = types.Tuple(array)

        if information is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, information)

        self._information: types.Tuple[types.DistributionNumber] = information
