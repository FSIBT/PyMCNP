import re
import typing


from . import fmult
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fmult(DataOption_, keyword='fmult'):
    """
    Represents INP fmult elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'zaid': types.Zaid,
        'options': types.Tuple[fmult.FmultOption_],
    }

    _REGEX = re.compile(
        rf'fmult( {types.Zaid._REGEX.pattern})(( ({fmult.FmultOption_._REGEX.pattern}))+)?'
    )

    def __init__(self, zaid: types.Zaid, options: types.Tuple[fmult.FmultOption_] = None):
        """
        Initializes ``Fmult``.

        Parameters:
            zaid: Nuclide for which data are entered.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if zaid is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zaid)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaid,
                options,
            ]
        )

        self.zaid: typing.Final[types.Zaid] = zaid
        self.options: typing.Final[types.Tuple[fmult.FmultOption_]] = options
