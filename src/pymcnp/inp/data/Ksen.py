import re
import typing


from . import ksen
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ksen(DataOption_, keyword='ksen'):
    """
    Represents INP ksen elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'sen': types.String,
        'options': types.Tuple[ksen.KsenOption_],
    }

    _REGEX = re.compile(
        rf'ksen(\d+)( {types.String._REGEX.pattern})(( ({ksen.KsenOption_._REGEX.pattern}))+)?'
    )

    def __init__(
        self,
        suffix: types.Integer,
        sen: types.String,
        options: types.Tuple[ksen.KsenOption_] = None,
    ):
        """
        Initializes ``Ksen``.

        Parameters:
            suffix: Data card option suffix.
            sen: Type of sensitivity.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (0 < suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if sen is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, sen)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                sen,
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.sen: typing.Final[types.String] = sen
        self.options: typing.Final[types.Tuple[ksen.KsenOption_]] = options
