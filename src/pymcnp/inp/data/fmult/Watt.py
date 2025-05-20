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
        'a': types.Real,
        'b': types.Real,
    }

    _REGEX = re.compile(rf'\Awatt( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z')

    def __init__(self, a: types.Real, b: types.Real):
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

        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b


@dataclasses.dataclass
class WattBuilder:
    """
    Builds ``Watt``.

    Attributes:
        a: Watt energy spectrum parameters a.
        b: Watt energy spectrum parameters b.
    """

    a: str | float | types.Real
    b: str | float | types.Real

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
            a = types.Real(self.a)
        elif isinstance(self.a, str):
            a = types.Real.from_mcnp(self.a)

        b = self.b
        if isinstance(self.b, types.Real):
            b = self.b
        elif isinstance(self.b, float) or isinstance(self.b, int):
            b = types.Real(self.b)
        elif isinstance(self.b, str):
            b = types.Real.from_mcnp(self.b)

        return Watt(
            a=a,
            b=b,
        )
