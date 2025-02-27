import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ds_1(DataOption_, keyword='ds'):
    """
    Represents INP ds_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        't': types.String,
        'ijs': types.Tuple[types.IndependentDependentEntry],
    }

    _REGEX = re.compile(rf'ds(\S+)( \S+)(( {types.IndependentDependentEntry._REGEX.pattern})+)')

    def __init__(
        self,
        suffix: types.Integer,
        t: types.String,
        ijs: types.Tuple[types.IndependentDependentEntry],
    ):
        """
        Initializes ``Ds_1``.

        Parameters:
            suffix: Data card option suffix.
            t: Dependent source T option.
            ijs: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if t is None or t not in {'t'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, t)
        if ijs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ijs)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                t,
                ijs,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.t: typing.Final[types.String] = t
        self.ijs: typing.Final[types.Tuple[types.IndependentDependentEntry]] = ijs
