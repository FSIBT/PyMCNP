import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class E(DataOption_, keyword='e'):
    """
    Represents INP e elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple[types.Real],
        'nt': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(
        rf'e(\d+)(( {types.Real._REGEX.pattern})+)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?'
    )

    def __init__(
        self,
        suffix: types.Integer,
        bounds: types.Tuple[types.Real],
        nt: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``E``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Upper energy bounds for bin.
            nt: Notation to inhibit automatic totaling.
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
                nt,
                c,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds
        self.nt: typing.Final[types.String] = nt
        self.c: typing.Final[types.String] = c
