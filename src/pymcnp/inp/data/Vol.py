import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Vol(DataOption_, keyword='vol'):
    """
    Represents INP vol elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'no': types.String,
        'volumes': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(
        rf'\Avol( no)?((?: {types.RealOrJump._REGEX.pattern})+?)\Z'
    )

    def __init__(self, volumes: types.Tuple[types.RealOrJump], no: types.String = None):
        """
        Initializes ``Vol``.

        Parameters:
            no: Volume calculation on/off.
            volumes: Tuple of cell volumes.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if no is not None and no not in {'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, no)
        if volumes is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, volumes)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                no,
                volumes,
            ]
        )

        self.no: typing.Final[types.String] = no
        self.volumes: typing.Final[types.Tuple[types.RealOrJump]] = volumes
