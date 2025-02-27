import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors


class Z(SurfaceOption_, keyword='z'):
    """
    Represents INP z elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'z1': types.Real,
        'r1': types.Real,
        'z2': types.Real,
        'r2': types.Real,
        'z3': types.Real,
        'r3': types.Real,
    }

    _REGEX = re.compile(r'z( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)')

    def __init__(
        self,
        z1: types.Real,
        r1: types.Real,
        z2: types.Real,
        r2: types.Real,
        z3: types.Real,
        r3: types.Real,
    ):
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if z1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z1)
        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r1)
        if z2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z2)
        if r2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r2)
        if z3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z3)
        if r3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r3)

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
