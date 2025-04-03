import re
import typing


from . import df_1
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Df_1(DataOption_, keyword='df'):
    """
    Represents INP df_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[df_1.Df_1Option_],
    }

    _REGEX = re.compile(rf'\Adf(\d+)((?: (?:{df_1.Df_1Option_._REGEX.pattern}))+?)\Z')

    def __init__(self, suffix: types.Integer, options: types.Tuple[df_1.Df_1Option_]):
        """
        Initializes ``Df_1``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if options is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, options)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.options: typing.Final[types.Tuple[df_1.Df_1Option_]] = options
