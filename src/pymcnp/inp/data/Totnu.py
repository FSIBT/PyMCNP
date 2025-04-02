import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Totnu(DataOption_, keyword='totnu'):
    """
    Represents INP totnu elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'no': types.String,
    }

    _REGEX = re.compile(rf'\Atotnu( {types.String._REGEX.pattern})?\Z')

    def __init__(self, no: types.String = None):
        """
        Initializes ``Totnu``.

        Parameters:
            no: Delay fission sampling on/off.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if no is not None and not (no == 'no'):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, no)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                no,
            ]
        )

        self.no: typing.Final[types.String] = no
