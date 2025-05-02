import re
import typing
import dataclasses


from . import free
from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Free(MplotOption):
    """
    Represents INP free elements.

    Attributes:
        x: Independent variable.
        y: Dependent variable.
        option: free option.
    """

    _ATTRS = {
        'x': types.String,
        'y': types.Real,
        'option': free.FreeOption,
    }

    _REGEX = re.compile(
        rf'\Afree( {types.String._REGEX.pattern})( {types.Real._REGEX.pattern})( (?:{free.FreeOption._REGEX.pattern}))?\Z'
    )

    def __init__(self, x: types.String, y: types.Real, option: free.FreeOption = None):
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
        self.y: typing.Final[types.Real] = y
        self.option: typing.Final[free.FreeOption] = option


@dataclasses.dataclass
class FreeBuilder:
    """
    Builds ``Free``.

    Attributes:
        x: Independent variable.
        y: Dependent variable.
        option: free option.
    """

    x: str | types.String
    y: str | float | types.Real
    option: str | free.FreeOption = None

    def build(self):
        """
        Builds ``FreeBuilder`` into ``Free``.

        Returns:
            ``Free`` for ``FreeBuilder``.
        """

        if isinstance(self.x, types.String):
            x = self.x
        elif isinstance(self.x, str):
            x = types.String.from_mcnp(self.x)

        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

        option = None
        if isinstance(self.option, free.FreeOption):
            option = self.option
        elif isinstance(self.option, str):
            option = free.FreeOption.from_mcnp(self.option)

        return Free(
            x=x,
            y=y,
            option=option,
        )
