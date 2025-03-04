import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class F_3(DataOption_, keyword='f'):
    """
    Represents INP f_3 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'problems': types.Tuple[types.Integer],
        't': types.String,
    }

    _REGEX = re.compile(r'f(\S+):(\S+)(( \S+)+)( \S+)?')

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        problems: types.Tuple[types.Integer],
        t: types.String = None,
    ):
        """
        Initializes ``F_3``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            problems: Problem numbers of cell.
            t: Average tallies option.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 == 8):
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
