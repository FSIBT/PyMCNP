import re
import copy
import typing
import dataclasses


from . import free
from . import _option
from ....utils import types
from ....utils import errors


class Free(_option.MplotOption):
    """
    Represents INP free elements.

    Attributes:
        x: Independent variable.
        y: Dependent variable.
        option: free option.
    """

    _KEYWORD = 'free'

    _ATTRS = {
        'x': types.String,
        'y': types.String,
        'option': free.FreeOption,
    }

    _REGEX = re.compile(rf'\Afree( {types.String._REGEX.pattern[2:-2]})( {types.String._REGEX.pattern[2:-2]})( (?:{free.FreeOption._REGEX.pattern[2:-2]}))?\Z')

    def __init__(self, x: types.String, y: types.String, option: free.FreeOption = None):
        """
        Initializes ``Free``.

        Parameters:
            x: Independent variable.
            y: Dependent variable.
            option: free option.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None or x not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't', 'i', 'j', 'k'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if y is None or y not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't', 'i', 'j', 'k'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                option,
            ]
        )

        self.x: typing.Final[types.String] = x
        self.y: typing.Final[types.String] = y
        self.option: typing.Final[free.FreeOption] = option


@dataclasses.dataclass
class FreeBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Free``.

    Attributes:
        x: Independent variable.
        y: Dependent variable.
        option: free option.
    """

    x: str | types.String
    y: str | types.String
    option: str | free.FreeOption = None

    def build(self):
        """
        Builds ``FreeBuilder`` into ``Free``.

        Returns:
            ``Free`` for ``FreeBuilder``.
        """

        x = self.x
        if isinstance(self.x, types.String):
            x = self.x
        elif isinstance(self.x, str):
            x = types.String.from_mcnp(self.x)

        y = self.y
        if isinstance(self.y, types.String):
            y = self.y
        elif isinstance(self.y, str):
            y = types.String.from_mcnp(self.y)

        option = self.option
        if isinstance(self.option, free.FreeOption):
            option = self.option
        elif isinstance(self.option, str):
            option = free.FreeOption.from_mcnp(self.option)
        elif isinstance(self.option, free.FreeOptionBuilder):
            option = self.option.build()

        return Free(
            x=x,
            y=y,
            option=option,
        )

    @staticmethod
    def unbuild(ast: Free):
        """
        Unbuilds ``Free`` into ``FreeBuilder``

        Returns:
            ``FreeBuilder`` for ``Free``.
        """

        return FreeBuilder(
            x=copy.deepcopy(ast.x),
            y=copy.deepcopy(ast.y),
            option=copy.deepcopy(ast.option),
        )
