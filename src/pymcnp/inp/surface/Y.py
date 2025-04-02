import re
import typing


from .option_ import SurfaceOption_
from ...utils import types
from ...utils import errors


class Y(SurfaceOption_, keyword='y'):
    """
    Represents INP y elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'y1': types.Real,
        'r1': types.Real,
        'y2': types.Real,
        'r2': types.Real,
        'y3': types.Real,
        'r3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ay( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        y1: types.Real,
        r1: types.Real,
        y2: types.Real,
        r2: types.Real,
        y3: types.Real,
        r3: types.Real,
    ):
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if y1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y1)
        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r1)
        if y2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y2)
        if r2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r2)
        if y3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y3)
        if r3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, r3)

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
