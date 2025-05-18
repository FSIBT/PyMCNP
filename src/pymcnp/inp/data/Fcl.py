import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Fcl(DataOption):
    """
    Represents INP fcl elements.

    Attributes:
        designator: Data card particle designator.
        control: Forced-collision control for cell.
    """

    _ATTRS = {
        'designator': types.Designator,
        'control': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Afcl:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, designator: types.Designator, control: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Fcl``.

        Parameters:
            designator: Data card particle designator.
            control: Forced-collision control for cell.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if control is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, control)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                control,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.control: typing.Final[types.Tuple[types.RealOrJump]] = control


@dataclasses.dataclass
class FclBuilder:
    """
    Builds ``Fcl``.

    Attributes:
        designator: Data card particle designator.
        control: Forced-collision control for cell.
    """

    designator: str | types.Designator
    control: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``FclBuilder`` into ``Fcl``.

        Returns:
            ``Fcl`` for ``FclBuilder``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        if self.control:
            control = []
            for item in self.control:
                if isinstance(item, types.RealOrJump):
                    control.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    control.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    control.append(types.RealOrJump.from_mcnp(item))
            control = types.Tuple(control)
        else:
            control = None

        return Fcl(
            designator=designator,
            control=control,
        )
