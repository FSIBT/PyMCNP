import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Wwn(CellOption):
    """
    Represents INP wwn elements.

    Attributes:
        suffix: Cell option suffix.
        designator: Cell particle designator.
        bound: Cell weight-window space, time, or energy lower bound.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'bound': types.Real,
    }

    _REGEX = re.compile(rf'\Awwn(\d+):(\S+)( {types.Real._REGEX.pattern})\Z')

    def __init__(self, suffix: types.Integer, designator: types.Designator, bound: types.Real):
        """
        Initializes ``Wwn``.

        Parameters:
            suffix: Cell option suffix.
            designator: Cell particle designator.
            bound: Cell weight-window space, time, or energy lower bound.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if bound is None or not (bound == -1 or bound >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bound)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bound,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.bound: typing.Final[types.Real] = bound


@dataclasses.dataclass
class WwnBuilder:
    """
    Builds ``Wwn``.

    Attributes:
        suffix: Cell option suffix.
        designator: Cell particle designator.
        bound: Cell weight-window space, time, or energy lower bound.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    bound: str | float | types.Real

    def build(self):
        """
        Builds ``WwnBuilder`` into ``Wwn``.

        Returns:
            ``Wwn`` for ``WwnBuilder``.
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

        if isinstance(self.bound, types.Real):
            bound = self.bound
        elif isinstance(self.bound, float) or isinstance(self.bound, int):
            bound = types.Real(self.bound)
        elif isinstance(self.bound, str):
            bound = types.Real.from_mcnp(self.bound)

        return Wwn(
            suffix=suffix,
            designator=designator,
            bound=bound,
        )
