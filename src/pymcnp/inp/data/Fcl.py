import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Fcl(_option.DataOption):
    """
    Represents INP fcl elements.

    Attributes:
        designator: Data card particle designator.
        control: Forced-collision control for cell.
    """

    _KEYWORD = 'fcl'

    _ATTRS = {
        'designator': types.Designator,
        'control': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Afcl:(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, designator: types.Designator, control: types.Tuple[types.Real]):
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
        self.control: typing.Final[types.Tuple[types.Real]] = control


@dataclasses.dataclass
class FclBuilder(_option.DataOptionBuilder):
    """
    Builds ``Fcl``.

    Attributes:
        designator: Data card particle designator.
        control: Forced-collision control for cell.
    """

    designator: str | types.Designator
    control: list[str] | list[float] | list[types.Real]

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
                if isinstance(item, types.Real):
                    control.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    control.append(types.Real(item))
                elif isinstance(item, str):
                    control.append(types.Real.from_mcnp(item))
            control = types.Tuple(control)
        else:
            control = None

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
