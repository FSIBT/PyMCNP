import re
import typing


from . import t_1
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class T_1(DataOption_, keyword='t'):
    """
    Represents INP t_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[t_1.T_1Option_],
    }

    _REGEX = re.compile(rf'\At(\d+)((?: (?:{t_1.T_1Option_._REGEX.pattern}))+?)\Z')

    def __init__(self, suffix: types.Integer, options: types.Tuple[t_1.T_1Option_]):
        """
        Initializes ``T_1``.

        Parameters:
            suffix: Data card option suffix.
            options: Data card options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if options is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, options)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.IntegerOrJump] = suffix
        self.options: typing.Final[types.Tuple[t_1.T_1Option_]] = options
