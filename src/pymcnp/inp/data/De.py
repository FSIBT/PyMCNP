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
        'values': types.Tuple[types.Real],
    }

    _REGEX = re.compile(
        rf'de(\S+)( {types.String._REGEX.pattern})(( {types.Real._REGEX.pattern})+)'
    )

    def __init__(
        self, suffix: types.Integer, method: types.String, values: types.Tuple[types.Real]
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
        if method is None or method not in {'log', 'lin'}:
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
        self.values: typing.Final[types.Tuple[types.Real]] = values
