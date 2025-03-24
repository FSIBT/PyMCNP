import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class F_0(DataOption_, keyword='f'):
    """
    Represents INP f_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'problems': types.Tuple[types.Integer],
        't': types.String,
    }

    _REGEX = re.compile(
        rf'f(\d+):(\S+)(( {types.Integer._REGEX.pattern})+)( {types.String._REGEX.pattern})?'
    )

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        problems: types.Tuple[types.Integer],
        t: types.String = None,
    ):
        """
        Initializes ``F_0``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            problems: Problem numbers of surface or cell.
            t: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 in {1, 2, 4, 6, 7}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if problems is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, problems)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                problems,
                t,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.problems: typing.Final[types.Tuple[types.Integer]] = problems
        self.t: typing.Final[types.String] = t
