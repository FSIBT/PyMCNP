import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Fcl(CellOption, keyword='fcl'):
    """
    Represents INP fcl elements.

    Attributes:
        designator: Cell particle designator.
        control: Cell forced-collision control.
    """

    _ATTRS = {
        'designator': types.Designator,
        'control': types.Real,
    }

    _REGEX = re.compile(rf'\Afcl:(\S+)( {types.Real._REGEX.pattern})\Z')

    def __init__(self, designator: types.Designator, control: types.Real):
        """
        Initializes ``Fcl``.

        Parameters:
            designator: Cell particle designator.
            control: Cell forced-collision control.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if control is None or not (-1 <= control <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, control)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                control,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.control: typing.Final[types.Real] = control


@dataclasses.dataclass
class FclBuilder:
    """
    Builds ``Fcl``.

    Attributes:
        designator: Cell particle designator.
        control: Cell forced-collision control.
    """

    designator: str | types.Designator
    control: str | float | types.Real

    def build(self):
        """
        Builds ``FclBuilder`` into ``Fcl``.

        Returns:
            ``Fcl`` for ``FclBuilder``.
        """

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        if isinstance(self.control, types.Real):
            control = self.control
        elif isinstance(self.control, float) or isinstance(self.control, int):
            control = types.Real(self.control)
        elif isinstance(self.control, str):
            control = types.Real.from_mcnp(self.control)

        return Fcl(
            designator=designator,
            control=control,
        )
