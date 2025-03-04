import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class F_2(DataOption_, keyword='f'):
    """
    Represents INP f_2 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'a': types.String,
        'designator': types.Designator,
        'rings': types.Tuple[types.RingEntry],
        'nd': types.String,
    }

    _REGEX = re.compile(rf'f(\S+):(\S+)( \S+)(( {types.RingEntry._REGEX.pattern})+)( \S+)?')

    def __init__(
        self,
        suffix: types.Integer,
        a: types.String,
        designator: types.Designator,
        rings: types.Tuple[types.RingEntry],
        nd: types.String = None,
    ):
        """
        Initializes ``F_2``.

        Parameters:
            suffix: Data card option suffix.
            a: Letter.
            designator: Data card particle designator.
            rings: Detector points.
            nd: Total/average specified surfaces/cells option.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 == 5):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if a is None or a not in {'x', 'y', 'z'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if rings is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, rings)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                a,
                rings,
                nd,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.a: typing.Final[types.String] = a
        self.designator: typing.Final[types.Designator] = designator
        self.rings: typing.Final[types.Tuple[types.RingEntry]] = rings
        self.nd: typing.Final[types.String] = nd
