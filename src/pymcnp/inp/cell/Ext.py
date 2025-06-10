import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Ext(_option.CellOption):
    """
    Represents INP ext elements.

    Attributes:
        designator: Cell particle designator.
        stretch: Cell exponential transform stretching specifier.
    """

    _KEYWORD = 'ext'

    _ATTRS = {
        'designator': types.Designator,
        'stretch': types.String,
    }

    _REGEX = re.compile(rf'\Aext:(\S+)( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, designator: types.Designator, stretch: types.String):
        """
        Initializes ``Ext``.

        Parameters:
            designator: Cell particle designator.
            stretch: Cell exponential transform stretching specifier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if stretch is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, stretch)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                stretch,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.stretch: typing.Final[types.String] = stretch


@dataclasses.dataclass
class ExtBuilder(_option.CellOptionBuilder):
    """
    Builds ``Ext``.

    Attributes:
        designator: Cell particle designator.
        stretch: Cell exponential transform stretching specifier.
    """

    designator: str | types.Designator
    stretch: str | types.String

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

        stretch = self.stretch
        if isinstance(self.stretch, types.String):
            stretch = self.stretch
        elif isinstance(self.stretch, str):
            stretch = types.String.from_mcnp(self.stretch)

        return Ext(
            designator=designator,
            stretch=stretch,
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
            stretch=copy.deepcopy(ast.stretch),
        )
