import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Fcl(_option.CellOption):
    """
    Represents INP fcl elements.

    Attributes:
        designator: Cell particle designator.
        control: Cell forced-collision control.
    """

    _KEYWORD = 'fcl'

    _ATTRS = {
        'designator': types.Designator,
        'control': types.Real,
    }

    _REGEX = re.compile(rf'\Afcl:(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z')

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
        if control is None or not (-1 <= control.value <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, control)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                control,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.control: typing.Final[types.Real] = control


@dataclasses.dataclass
class FclBuilder(_option.CellOptionBuilder):
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

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        control = self.control
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

    @staticmethod
    def unbuild(ast: Fcl):
        """
        Unbuilds ``Fcl`` into ``FclBuilder``

        Returns:
            ``FclBuilder`` for ``Fcl``.
        """

        return FclBuilder(
            designator=copy.deepcopy(ast.designator),
            control=copy.deepcopy(ast.control),
        )
