import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Factor(MplotOption):
    """
    Represents INP factor elements.

    Attributes:
        a: Multiplication axis.
        f: Multiplication factor.
        s: Addative term.
    """

    _ATTRS = {
        'a': types.String,
        'f': types.Real,
        's': types.Real,
    }

    _REGEX = re.compile(
        rf'\Afactor( {types.String._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})?\Z'
    )

    def __init__(self, a: types.String, f: types.Real, s: types.Real = None):
        """
        Initializes ``Factor``.

        Parameters:
            a: Multiplication axis.
            f: Multiplication factor.
            s: Addative term.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if a is None or a not in {'x', 'y', 'z'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a)
        if f is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, f)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                a,
                f,
                s,
            ]
        )

        self.a: typing.Final[types.String] = a
        self.f: typing.Final[types.Real] = f
        self.s: typing.Final[types.Real] = s


@dataclasses.dataclass
class FactorBuilder:
    """
    Builds ``Factor``.

    Attributes:
        a: Multiplication axis.
        f: Multiplication factor.
        s: Addative term.
    """

    a: str | types.String
    f: str | float | types.Real
    s: str | float | types.Real = None

    def build(self):
        """
        Builds ``FactorBuilder`` into ``Factor``.

        Returns:
            ``Factor`` for ``FactorBuilder``.
        """

        if isinstance(self.a, types.String):
            a = self.a
        elif isinstance(self.a, str):
            a = types.String.from_mcnp(self.a)

        if isinstance(self.f, types.Real):
            f = self.f
        elif isinstance(self.f, float) or isinstance(self.f, int):
            f = types.Real(self.f)
        elif isinstance(self.f, str):
            f = types.Real.from_mcnp(self.f)

        s = None
        if isinstance(self.s, types.Real):
            s = self.s
        elif isinstance(self.s, float) or isinstance(self.s, int):
            s = types.Real(self.s)
        elif isinstance(self.s, str):
            s = types.Real.from_mcnp(self.s)

        return Factor(
            a=a,
            f=f,
            s=s,
        )
