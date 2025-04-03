import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class C_0(DataOption_, keyword='c'):
    """
    Represents INP c_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple[types.RealOrJump],
        't': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(
        rf'\Ac(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        bounds: types.Tuple[types.RealOrJump],
        t: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``C_0``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Upper cosine bounds for bin.
            t: Notation to provide totals.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
                t,
                c,
            ]
        )

        self.suffix: typing.Final[types.IntegerOrJump] = suffix
        self.bounds: typing.Final[types.Tuple[types.RealOrJump]] = bounds
        self.t: typing.Final[types.String] = t
        self.c: typing.Final[types.String] = c
