import re

from . import f
from . import _option
from ... import errors


class Par_1(_option.SdefOption):
    """
    Represents INP `par` elements variation #1.
    """

    _KEYWORD = 'par'

    _ATTRS = {
        'option': f.FOption,
    }

    _REGEX = re.compile(rf'\Apar( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)

    def __init__(self, option: str | f.FOption):
        """
        Initializes `Par_1`.

        Parameters:
            option: Dependent distribution option.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.option: f.FOption = option

    @property
    def option(self) -> f.FOption:
        """
        Dependent distribution option

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._option

    @option.setter
    def option(self, option: str | f.FOption) -> None:
        """
        Sets `option`.

        Parameters:
            option: Dependent distribution option.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if option is not None:
            if isinstance(option, f.FOption):
                option = option
            elif isinstance(option, str):
                option = f.FOption.from_mcnp(option)

        if option is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, option)

        self._option: f.FOption = option
