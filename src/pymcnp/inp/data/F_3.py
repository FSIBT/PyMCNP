import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class F_3(DataOption):
    """
    Represents INP f variation #3 elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        problems: Problem numbers of cell.
        t: Average tallies option.
    """

    _KEYWORD = 'f'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'problems': types.Tuple[types.Integer],
        't': types.String,
    }

    _REGEX = re.compile(
        rf'\Af(\d*[8]):(\S+)((?: {types.Integer._REGEX.pattern})+?)( {types.String._REGEX.pattern})?\Z'
    )

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
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix.value <= 99_999_999 and suffix.value % 10 == 8):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if problems is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, problems)

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
    problems: list[str] | list[int] | list[types.Integer]
    t: str | types.String = None

    def build(self):
        """
        Builds ``FBuilder_3`` into ``F_3``.

        Returns:
            ``F_3`` for ``FBuilder_3``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        if self.problems:
            problems = []
            for item in self.problems:
                if isinstance(item, types.Integer):
                    problems.append(item)
                elif isinstance(item, int):
                    problems.append(types.Integer(item))
                elif isinstance(item, str):
                    problems.append(types.Integer.from_mcnp(item))
            problems = types.Tuple(problems)
        else:
            problems = None

        t = self.t
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

    @staticmethod
    def unbuild(ast: F_3):
        """
        Unbuilds ``F_3`` into ``FBuilder_3``

        Returns:
            ``FBuilder_3`` for ``F_3``.
        """

        return F_3(
            suffix=copy.deepcopy(ast.suffix),
            designator=copy.deepcopy(ast.designator),
            problems=copy.deepcopy(ast.problems),
            t=copy.deepcopy(ast.t),
        )
