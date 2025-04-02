import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class C_1(DataOption_, keyword='[*]c'):
    """
    Represents INP c_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple[types.Real],
        't': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(
        rf'\A[*]c(\d+)((?: {types.Real._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        bounds: types.Tuple[types.Real],
        t: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``C_1``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Upper angle limit for bin.
            t: Notation to provide totals.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if bounds is None or not (bounds[-1] == 0 and max(bounds) <= 180):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
                t,
                c,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds
        self.t: typing.Final[types.String] = t
        self.c: typing.Final[types.String] = c
