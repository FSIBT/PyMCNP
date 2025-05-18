import re
import typing
import dataclasses


from ._option import FmultOption
from ....utils import types
from ....utils import errors


class Watt(FmultOption):
    """
    Represents INP watt elements.

    Attributes:
        a: Watt energy spectrum parameters a.
        b: Watt energy spectrum parameters b.
    """

    _ATTRS = {
        'a': types.RealOrJump,
        'b': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Awatt( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, a: types.RealOrJump, b: types.RealOrJump):
        """
        Initializes ``Watt``.

        Parameters:
            a: Watt energy spectrum parameters a.
            b: Watt energy spectrum parameters b.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a)
        if b is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, b)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                a,
                b,
            ]
        )

        self.a: typing.Final[types.RealOrJump] = a
        self.b: typing.Final[types.RealOrJump] = b


@dataclasses.dataclass
class WattBuilder:
    """
    Builds ``Watt``.

    Attributes:
        a: Watt energy spectrum parameters a.
        b: Watt energy spectrum parameters b.
    """

    a: str | float | types.RealOrJump
    b: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``WattBuilder`` into ``Watt``.

        Returns:
            ``Watt`` for ``WattBuilder``.
        """

        a = self.a
        if isinstance(self.a, types.Real):
            a = self.a
        elif isinstance(self.a, float) or isinstance(self.a, int):
            a = types.RealOrJump(self.a)
        elif isinstance(self.a, str):
            a = types.RealOrJump.from_mcnp(self.a)

        b = self.b
        if isinstance(self.b, types.Real):
            b = self.b
        elif isinstance(self.b, float) or isinstance(self.b, int):
            b = types.RealOrJump(self.b)
        elif isinstance(self.b, str):
            b = types.RealOrJump.from_mcnp(self.b)

        return Watt(
            a=a,
            b=b,
        )
