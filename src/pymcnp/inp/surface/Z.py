import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Z(_option.SurfaceOption):
    """
    Represents INP z elements.

    Attributes:
        z1: Z-axisymmetric point-defined surface point #1 z component.
        r1: Z-axisymmetric point-defined surface point #1 radius.
        z2: Z-axisymmetric point-defined surface point #2 z component.
        r2: Z-axisymmetric point-defined surface point #2 radius.
        z3: Z-axisymmetric point-defined surface point #3 z component.
        r3: Z-axisymmetric point-defined surface point #3 radius.
    """

    _KEYWORD = 'z'

    _ATTRS = {
        'z1': types.Real,
        'r1': types.Real,
        'z2': types.Real,
        'r2': types.Real,
        'z3': types.Real,
        'r3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Az( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(self, z1: types.Real, r1: types.Real, z2: types.Real = None, r2: types.Real = None, z3: types.Real = None, r3: types.Real = None):
        """
        Initializes ``Z``.

        Parameters:
            z1: Z-axisymmetric point-defined surface point #1 z component.
            r1: Z-axisymmetric point-defined surface point #1 radius.
            z2: Z-axisymmetric point-defined surface point #2 z component.
            r2: Z-axisymmetric point-defined surface point #2 radius.
            z3: Z-axisymmetric point-defined surface point #3 z component.
            r3: Z-axisymmetric point-defined surface point #3 radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if z1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z1)
        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r1)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                z1,
                r1,
                z2,
                r2,
                z3,
                r3,
            ]
        )

        self.z1: typing.Final[types.Real] = z1
        self.r1: typing.Final[types.Real] = r1
        self.z2: typing.Final[types.Real] = z2
        self.r2: typing.Final[types.Real] = r2
        self.z3: typing.Final[types.Real] = z3
        self.r3: typing.Final[types.Real] = r3


@dataclasses.dataclass
class ZBuilder(_option.SurfaceOptionBuilder):
    """
    Builds ``Z``.

    Attributes:
        z1: Z-axisymmetric point-defined surface point #1 z component.
        r1: Z-axisymmetric point-defined surface point #1 radius.
        z2: Z-axisymmetric point-defined surface point #2 z component.
        r2: Z-axisymmetric point-defined surface point #2 radius.
        z3: Z-axisymmetric point-defined surface point #3 z component.
        r3: Z-axisymmetric point-defined surface point #3 radius.
    """

    z1: str | float | types.Real
    r1: str | float | types.Real
    z2: str | float | types.Real = None
    r2: str | float | types.Real = None
    z3: str | float | types.Real = None
    r3: str | float | types.Real = None

    def build(self):
        """
        Builds ``ZBuilder`` into ``Z``.

        Returns:
            ``Z`` for ``ZBuilder``.
        """

        z1 = self.z1
        if isinstance(self.z1, types.Real):
            z1 = self.z1
        elif isinstance(self.z1, float) or isinstance(self.z1, int):
            z1 = types.Real(self.z1)
        elif isinstance(self.z1, str):
            z1 = types.Real.from_mcnp(self.z1)

        r1 = self.r1
        if isinstance(self.r1, types.Real):
            r1 = self.r1
        elif isinstance(self.r1, float) or isinstance(self.r1, int):
            r1 = types.Real(self.r1)
        elif isinstance(self.r1, str):
            r1 = types.Real.from_mcnp(self.r1)

        z2 = self.z2
        if isinstance(self.z2, types.Real):
            z2 = self.z2
        elif isinstance(self.z2, float) or isinstance(self.z2, int):
            z2 = types.Real(self.z2)
        elif isinstance(self.z2, str):
            z2 = types.Real.from_mcnp(self.z2)

        r2 = self.r2
        if isinstance(self.r2, types.Real):
            r2 = self.r2
        elif isinstance(self.r2, float) or isinstance(self.r2, int):
            r2 = types.Real(self.r2)
        elif isinstance(self.r2, str):
            r2 = types.Real.from_mcnp(self.r2)

        z3 = self.z3
        if isinstance(self.z3, types.Real):
            z3 = self.z3
        elif isinstance(self.z3, float) or isinstance(self.z3, int):
            z3 = types.Real(self.z3)
        elif isinstance(self.z3, str):
            z3 = types.Real.from_mcnp(self.z3)

        r3 = self.r3
        if isinstance(self.r3, types.Real):
            r3 = self.r3
        elif isinstance(self.r3, float) or isinstance(self.r3, int):
            r3 = types.Real(self.r3)
        elif isinstance(self.r3, str):
            r3 = types.Real.from_mcnp(self.r3)

        return Z(
            z1=z1,
            r1=r1,
            z2=z2,
            r2=r2,
            z3=z3,
            r3=r3,
        )

    @staticmethod
    def unbuild(ast: Z):
        """
        Unbuilds ``Z`` into ``ZBuilder``

        Returns:
            ``ZBuilder`` for ``Z``.
        """

        return ZBuilder(
            z1=copy.deepcopy(ast.z1),
            r1=copy.deepcopy(ast.r1),
            z2=copy.deepcopy(ast.z2),
            r2=copy.deepcopy(ast.r2),
            z3=copy.deepcopy(ast.z3),
            r3=copy.deepcopy(ast.r3),
        )
