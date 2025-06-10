import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Ext(_option.DataOption):
    """
    Represents INP ext elements.

    Attributes:
        designator: Data card particle designator.
        stretching: Stretching direction for the cell.
    """

    _KEYWORD = 'ext'

    _ATTRS = {
        'designator': types.Designator,
        'stretching': types.Tuple[types.String],
    }

    _REGEX = re.compile(rf'\Aext:(\S+)((?: {types.String._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, designator: types.Designator, stretching: types.Tuple[types.String]):
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
        self.stretching: typing.Final[types.Tuple[types.String]] = stretching


@dataclasses.dataclass
class ExtBuilder(_option.DataOptionBuilder):
    """
    Builds ``Ext``.

    Attributes:
        designator: Data card particle designator.
        stretching: Stretching direction for the cell.
    """

    designator: str | types.Designator
    stretching: list[str] | list[types.String]

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
                if isinstance(item, types.String):
                    stretching.append(item)
                elif isinstance(item, str):
                    stretching.append(types.String.from_mcnp(item))
            stretching = types.Tuple(stretching)
        else:
            stretching = None

        return Ext(
            designator=designator,
            stretching=stretching,
        )

    @staticmethod
    def unbuild(ast: Ext):
        """
        Unbuilds ``Ext`` into ``ExtBuilder``

        Returns:
            ``ExtBuilder`` for ``Ext``.
        """

        return ExtBuilder(
            designator=copy.deepcopy(ast.designator),
            stretching=copy.deepcopy(ast.stretching),
        )
