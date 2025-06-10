import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Y(_option.SurfaceOption):
    """
    Represents INP y elements.

    Attributes:
        y1: Y-axisymmetric point-defined surface point #1 y component.
        r1: Y-axisymmetric point-defined surface point #1 radius.
        y2: Y-axisymmetric point-defined surface point #2 y component.
        r2: Y-axisymmetric point-defined surface point #2 radius.
        y3: Y-axisymmetric point-defined surface point #3 y component.
        r3: Y-axisymmetric point-defined surface point #3 radius.
    """

    _KEYWORD = 'y'

    _ATTRS = {
        'y1': types.Real,
        'r1': types.Real,
        'y2': types.Real,
        'r2': types.Real,
        'y3': types.Real,
        'r3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ay( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(self, y1: types.Real, r1: types.Real, y2: types.Real = None, r2: types.Real = None, y3: types.Real = None, r3: types.Real = None):
        """
        Initializes ``Y``.

        Parameters:
            y1: Y-axisymmetric point-defined surface point #1 y component.
            r1: Y-axisymmetric point-defined surface point #1 radius.
            y2: Y-axisymmetric point-defined surface point #2 y component.
            r2: Y-axisymmetric point-defined surface point #2 radius.
            y3: Y-axisymmetric point-defined surface point #3 y component.
            r3: Y-axisymmetric point-defined surface point #3 radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if y1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y1)
        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r1)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                y1,
                r1,
                y2,
                r2,
                y3,
                r3,
            ]
        )

        self.y1: typing.Final[types.Real] = y1
        self.r1: typing.Final[types.Real] = r1
        self.y2: typing.Final[types.Real] = y2
        self.r2: typing.Final[types.Real] = r2
        self.y3: typing.Final[types.Real] = y3
        self.r3: typing.Final[types.Real] = r3


@dataclasses.dataclass
class YBuilder(_option.SurfaceOptionBuilder):
    """
    Builds ``Y``.

    Attributes:
        y1: Y-axisymmetric point-defined surface point #1 y component.
        r1: Y-axisymmetric point-defined surface point #1 radius.
        y2: Y-axisymmetric point-defined surface point #2 y component.
        r2: Y-axisymmetric point-defined surface point #2 radius.
        y3: Y-axisymmetric point-defined surface point #3 y component.
        r3: Y-axisymmetric point-defined surface point #3 radius.
    """

    y1: str | float | types.Real
    r1: str | float | types.Real
    y2: str | float | types.Real = None
    r2: str | float | types.Real = None
    y3: str | float | types.Real = None
    r3: str | float | types.Real = None

    def build(self):
        """
        Builds ``YBuilder`` into ``Y``.

        Returns:
            ``Y`` for ``YBuilder``.
        """

        y1 = self.y1
        if isinstance(self.y1, types.Real):
            y1 = self.y1
        elif isinstance(self.y1, float) or isinstance(self.y1, int):
            y1 = types.Real(self.y1)
        elif isinstance(self.y1, str):
            y1 = types.Real.from_mcnp(self.y1)

        r1 = self.r1
        if isinstance(self.r1, types.Real):
            r1 = self.r1
        elif isinstance(self.r1, float) or isinstance(self.r1, int):
            r1 = types.Real(self.r1)
        elif isinstance(self.r1, str):
            r1 = types.Real.from_mcnp(self.r1)

        y2 = self.y2
        if isinstance(self.y2, types.Real):
            y2 = self.y2
        elif isinstance(self.y2, float) or isinstance(self.y2, int):
            y2 = types.Real(self.y2)
        elif isinstance(self.y2, str):
            y2 = types.Real.from_mcnp(self.y2)

        r2 = self.r2
        if isinstance(self.r2, types.Real):
            r2 = self.r2
        elif isinstance(self.r2, float) or isinstance(self.r2, int):
            r2 = types.Real(self.r2)
        elif isinstance(self.r2, str):
            r2 = types.Real.from_mcnp(self.r2)

        y3 = self.y3
        if isinstance(self.y3, types.Real):
            y3 = self.y3
        elif isinstance(self.y3, float) or isinstance(self.y3, int):
            y3 = types.Real(self.y3)
        elif isinstance(self.y3, str):
            y3 = types.Real.from_mcnp(self.y3)

        r3 = self.r3
        if isinstance(self.r3, types.Real):
            r3 = self.r3
        elif isinstance(self.r3, float) or isinstance(self.r3, int):
            r3 = types.Real(self.r3)
        elif isinstance(self.r3, str):
            r3 = types.Real.from_mcnp(self.r3)

        return Y(
            y1=y1,
            r1=r1,
            y2=y2,
            r2=r2,
            y3=y3,
            r3=r3,
        )

    @staticmethod
    def unbuild(ast: Y):
        """
        Unbuilds ``Y`` into ``YBuilder``

        Returns:
            ``YBuilder`` for ``Y``.
        """

        return YBuilder(
            y1=copy.deepcopy(ast.y1),
            r1=copy.deepcopy(ast.r1),
            y2=copy.deepcopy(ast.y2),
            r2=copy.deepcopy(ast.r2),
            y3=copy.deepcopy(ast.y3),
            r3=copy.deepcopy(ast.r3),
        )
