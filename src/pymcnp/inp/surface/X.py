import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class X(_option.SurfaceOption):
    """
    Represents INP x elements.

    Attributes:
        x1: X-axisymmetric point-defined surface point #1 x component.
        r1: X-axisymmetric point-defined surface point #1 radius.
        x2: X-axisymmetric point-defined surface point #2 x component.
        r2: X-axisymmetric point-defined surface point #2 radius.
        x3: X-axisymmetric point-defined surface point #3 x component.
        r3: X-axisymmetric point-defined surface point #3 radius.
    """

    _KEYWORD = 'x'

    _ATTRS = {
        'x1': types.Real,
        'r1': types.Real,
        'x2': types.Real,
        'r2': types.Real,
        'x3': types.Real,
        'r3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ax( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(self, x1: types.Real, r1: types.Real, x2: types.Real = None, r2: types.Real = None, x3: types.Real = None, r3: types.Real = None):
        """
        Initializes ``X``.

        Parameters:
            x1: X-axisymmetric point-defined surface point #1 x component.
            r1: X-axisymmetric point-defined surface point #1 radius.
            x2: X-axisymmetric point-defined surface point #2 x component.
            r2: X-axisymmetric point-defined surface point #2 radius.
            x3: X-axisymmetric point-defined surface point #3 x component.
            r3: X-axisymmetric point-defined surface point #3 radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x1)
        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r1)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x1,
                r1,
                x2,
                r2,
                x3,
                r3,
            ]
        )

        self.x1: typing.Final[types.Real] = x1
        self.r1: typing.Final[types.Real] = r1
        self.x2: typing.Final[types.Real] = x2
        self.r2: typing.Final[types.Real] = r2
        self.x3: typing.Final[types.Real] = x3
        self.r3: typing.Final[types.Real] = r3


@dataclasses.dataclass
class XBuilder(_option.SurfaceOptionBuilder):
    """
    Builds ``X``.

    Attributes:
        x1: X-axisymmetric point-defined surface point #1 x component.
        r1: X-axisymmetric point-defined surface point #1 radius.
        x2: X-axisymmetric point-defined surface point #2 x component.
        r2: X-axisymmetric point-defined surface point #2 radius.
        x3: X-axisymmetric point-defined surface point #3 x component.
        r3: X-axisymmetric point-defined surface point #3 radius.
    """

    x1: str | float | types.Real
    r1: str | float | types.Real
    x2: str | float | types.Real = None
    r2: str | float | types.Real = None
    x3: str | float | types.Real = None
    r3: str | float | types.Real = None

    def build(self):
        """
        Builds ``XBuilder`` into ``X``.

        Returns:
            ``X`` for ``XBuilder``.
        """

        x1 = self.x1
        if isinstance(self.x1, types.Real):
            x1 = self.x1
        elif isinstance(self.x1, float) or isinstance(self.x1, int):
            x1 = types.Real(self.x1)
        elif isinstance(self.x1, str):
            x1 = types.Real.from_mcnp(self.x1)

        r1 = self.r1
        if isinstance(self.r1, types.Real):
            r1 = self.r1
        elif isinstance(self.r1, float) or isinstance(self.r1, int):
            r1 = types.Real(self.r1)
        elif isinstance(self.r1, str):
            r1 = types.Real.from_mcnp(self.r1)

        x2 = self.x2
        if isinstance(self.x2, types.Real):
            x2 = self.x2
        elif isinstance(self.x2, float) or isinstance(self.x2, int):
            x2 = types.Real(self.x2)
        elif isinstance(self.x2, str):
            x2 = types.Real.from_mcnp(self.x2)

        r2 = self.r2
        if isinstance(self.r2, types.Real):
            r2 = self.r2
        elif isinstance(self.r2, float) or isinstance(self.r2, int):
            r2 = types.Real(self.r2)
        elif isinstance(self.r2, str):
            r2 = types.Real.from_mcnp(self.r2)

        x3 = self.x3
        if isinstance(self.x3, types.Real):
            x3 = self.x3
        elif isinstance(self.x3, float) or isinstance(self.x3, int):
            x3 = types.Real(self.x3)
        elif isinstance(self.x3, str):
            x3 = types.Real.from_mcnp(self.x3)

        r3 = self.r3
        if isinstance(self.r3, types.Real):
            r3 = self.r3
        elif isinstance(self.r3, float) or isinstance(self.r3, int):
            r3 = types.Real(self.r3)
        elif isinstance(self.r3, str):
            r3 = types.Real.from_mcnp(self.r3)

        return X(
            x1=x1,
            r1=r1,
            x2=x2,
            r2=r2,
            x3=x3,
            r3=r3,
        )

    @staticmethod
    def unbuild(ast: X):
        """
        Unbuilds ``X`` into ``XBuilder``

        Returns:
            ``XBuilder`` for ``X``.
        """

        return XBuilder(
            x1=copy.deepcopy(ast.x1),
            r1=copy.deepcopy(ast.r1),
            x2=copy.deepcopy(ast.x2),
            r2=copy.deepcopy(ast.r2),
            x3=copy.deepcopy(ast.x3),
            r3=copy.deepcopy(ast.r3),
        )
