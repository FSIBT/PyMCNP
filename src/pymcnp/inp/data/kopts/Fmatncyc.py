import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Fmatncyc(KoptsOption_, keyword='fmatncyc'):
    """
    Represents INP fmatncyc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'fmat_ncyc': types.Real,
    }

    _REGEX = re.compile(r'fmatncyc( \S+)')

    def __init__(self, fmat_ncyc: types.Real):
        """
        Initializes ``Fmatncyc``.

        Parameters:
            fmat_ncyc: fmat_ncyc.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_ncyc is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_ncyc)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_ncyc,
            ]
        )

        self.fmat_ncyc: typing.Final[types.Real] = fmat_ncyc
