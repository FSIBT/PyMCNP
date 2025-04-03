import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class De(DataOption_, keyword='de'):
    """
    Represents INP de elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'method': types.String,
        'values': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(
        rf'\Ade(\d+)( (?:log|lin))?((?: {types.RealOrJump._REGEX.pattern})+?)\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        values: types.Tuple[types.RealOrJump],
        method: types.String = None,
    ):
        """
        Initializes ``De``.

        Parameters:
            suffix: Data card option suffix.
            method: Interpolation method for energy table.
            values: Energy values.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if method is not None and method not in {'log', 'lin'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, method)
        if values is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, values)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                method,
                values,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.method: typing.Final[types.String] = method
        self.values: typing.Final[types.Tuple[types.RealOrJump]] = values
