import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fu(DataOption_, keyword='fu'):
    """
    Represents INP fu elements.

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
        rf'\Afu(\d+)((?: {types.Real._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        bounds: types.Tuple[types.Real],
        nt: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``Fu``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Input parameters for user bins.
            nt: Notation to inhibit automatic totaling.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if bounds is None or not (filter(lambda entry: not (entry > -1), bounds)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bounds)
        if nt is not None and nt not in {'nt'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nt)
        if c is not None and c not in {'c'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, c)

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
