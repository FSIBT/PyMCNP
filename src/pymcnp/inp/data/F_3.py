import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class F_3(DataOption_, keyword='f'):
    """
    Represents INP f variation #3 elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        problems: Problem numbers of cell.
        t: Average tallies option.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'problems': types.Tuple[types.IntegerOrJump],
        't': types.String,
    }

    _REGEX = re.compile(
        rf'\Af(\d*[8]):(\S+)((?: {types.IntegerOrJump._REGEX.pattern})+?)( {types.String._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        problems: types.Tuple[types.IntegerOrJump],
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
        self.problems: typing.Final[types.Tuple[types.IntegerOrJump]] = problems
        self.t: typing.Final[types.String] = t


@dataclasses.dataclass
class FBuilder_3:
    """
    Builds ``F_3``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        problems: Problem numbers of cell.
        t: Average tallies option.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    problems: list[str] | list[int] | list[types.IntegerOrJump]
    t: str | types.String = None

    def build(self):
        """
        Builds ``FBuilder_3`` into ``F_3``.

        Returns:
            ``F_3`` for ``FBuilder_3``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        problems = []
        for item in self.problems:
            if isinstance(item, types.IntegerOrJump):
                problems.append(item)
            elif isinstance(item, int):
                problems.append(types.IntegerOrJump(item))
            elif isinstance(item, str):
                problems.append(types.IntegerOrJump.from_mcnp(item))
        problems = types.Tuple(problems)

        t = None
        if isinstance(self.t, types.String):
            t = self.t
        elif isinstance(self.t, str):
            t = types.String.from_mcnp(self.t)

        return F_3(
            suffix=suffix,
            designator=designator,
            problems=problems,
            t=t,
        )
