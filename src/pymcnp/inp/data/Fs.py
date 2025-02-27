import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fs(DataOption_, keyword='fs'):
    """
    Represents INP fs elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'numbers': types.Tuple[types.Integer],
        't': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(r'fs(\S+)(( \S+)+)( \S+)?( \S+)?')

    def __init__(
        self,
        suffix: types.Integer,
        numbers: types.Tuple[types.Integer],
        t: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``Fs``.

        Parameters:
            suffix: Data card option suffix.
            numbers: Signed problem number of a segmenting surface..
            t: Notation to provide totals.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if numbers is None or not (
            filter(lambda entry: not (-99_999_999 <= numbers <= 99_999_999), numbers)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)
        if t is not None and t not in {'t'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, t)
        if c is not None and c not in {'c'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, c)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
                t,
                c,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers
        self.t: typing.Final[types.String] = t
        self.c: typing.Final[types.String] = c
