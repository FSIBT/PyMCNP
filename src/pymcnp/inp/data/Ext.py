import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Ext(DataOption):
    """
    Represents INP ext elements.

    Attributes:
        designator: Data card particle designator.
        stretching: Stretching direction for the cell.
    """

    _ATTRS = {
        'designator': types.Designator,
        'stretching': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aext:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, designator: types.Designator, stretching: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Ext``.

        Parameters:
            designator: Data card particle designator.
            stretching: Stretching direction for the cell.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if stretching is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, stretching)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                stretching,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.stretching: typing.Final[types.Tuple[types.RealOrJump]] = stretching


@dataclasses.dataclass
class ExtBuilder:
    """
    Builds ``Ext``.

    Attributes:
        designator: Data card particle designator.
        stretching: Stretching direction for the cell.
    """

    designator: str | types.Designator
    stretching: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``ExtBuilder`` into ``Ext``.

        Returns:
            ``Ext`` for ``ExtBuilder``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        if self.stretching:
            stretching = []
            for item in self.stretching:
                if isinstance(item, types.RealOrJump):
                    stretching.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    stretching.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    stretching.append(types.RealOrJump.from_mcnp(item))
            stretching = types.Tuple(stretching)
        else:
            stretching = None

        return Ext(
            designator=designator,
            stretching=stretching,
        )
