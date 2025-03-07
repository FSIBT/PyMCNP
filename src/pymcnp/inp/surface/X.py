import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors


class X(SurfaceOption_, keyword='x'):
    """
    Represents INP x elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x1': types.Real,
        'r1': types.Real,
        'x2': types.Real,
        'r2': types.Real,
        'x3': types.Real,
        'r3': types.Real,
    }

    _REGEX = re.compile(
        rf'x( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(
        self,
        x1: types.Real,
        r1: types.Real,
        x2: types.Real,
        r2: types.Real,
        x3: types.Real,
        r3: types.Real,
    ):
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x1)
        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r1)
        if x2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x2)
        if r2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r2)
        if x3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x3)
        if r3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r3)

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
