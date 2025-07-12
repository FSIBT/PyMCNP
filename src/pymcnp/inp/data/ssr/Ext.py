import re

from . import _option
from ....utils import types
from ....utils import errors


class Ext(_option.SsrOption):
    """
    Represents INP ext elements.
    """

    _KEYWORD = 'ext'

    _ATTRS = {
        'number': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Aext( {types.DistributionNumber._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: str | types.DistributionNumber):
        """
        Initializes ``Ext``.

        Parameters:
            number: Distribution number for baising sampling.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.number: types.DistributionNumber = number

    @property
    def number(self) -> types.DistributionNumber:
        """
        Distribution number for baising sampling

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._number

    @number.setter
    def number(self, number: str | types.DistributionNumber) -> None:
        """
        Sets ``number``.

        Parameters:
            number: Distribution number for baising sampling.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if number is not None:
            if isinstance(number, types.DistributionNumber):
                number = number
            elif isinstance(number, str):
                number = types.DistributionNumber.from_mcnp(number)

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self._number: types.DistributionNumber = number
