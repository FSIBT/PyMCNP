import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Factor(_option.MplotOption):
    """
    Represents INP factor elements.

    Attributes:
        a: Multiplication axis.
        f: Multiplication factor.
        s: Addative term.
    """

    _KEYWORD = 'factor'

    _ATTRS = {
        'a': types.String,
        'f': types.Real,
        's': types.Real,
    }

    _REGEX = re.compile(rf'\Afactor( {types.String._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z')

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
class FactorBuilder(_option.MplotOptionBuilder):
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

        a = self.a
        if isinstance(self.a, types.String):
            a = self.a
        elif isinstance(self.a, str):
            a = types.String.from_mcnp(self.a)

        f = self.f
        if isinstance(self.f, types.Real):
            f = self.f
        elif isinstance(self.f, float) or isinstance(self.f, int):
            f = types.Real(self.f)
        elif isinstance(self.f, str):
            f = types.Real.from_mcnp(self.f)

        s = self.s
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

    @staticmethod
    def unbuild(ast: Factor):
        """
        Unbuilds ``Factor`` into ``FactorBuilder``

        Returns:
            ``FactorBuilder`` for ``Factor``.
        """

        return FactorBuilder(
            a=copy.deepcopy(ast.a),
            f=copy.deepcopy(ast.f),
            s=copy.deepcopy(ast.s),
        )
