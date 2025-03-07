import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Bem(SdefOption_, keyword='bem'):
    """
    Represents INP bem elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'exn': types.Real,
        'eyn': types.Real,
        'bml': types.Real,
    }

    _REGEX = re.compile(
        rf'bem( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(self, exn: types.Real, eyn: types.Real, bml: types.Real):
        """
        Initializes ``Bem``.

        Parameters:
            exn: Normalized beam emittance parameter for x coordinates.
            eyn: Normalized beam emittance parameter for x coordinates.
            bml: Distance from the aperture to the spot.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if exn is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, exn)
        if eyn is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, eyn)
        if bml is None or not (bml >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bml)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                exn,
                eyn,
                bml,
            ]
        )

        self.exn: typing.Final[types.Real] = exn
        self.eyn: typing.Final[types.Real] = eyn
        self.bml: typing.Final[types.Real] = bml
