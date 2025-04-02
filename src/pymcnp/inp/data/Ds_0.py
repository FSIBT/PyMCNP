import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ds_0(DataOption_, keyword='ds'):
    """
    Represents INP ds_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'js': types.Tuple[types.Real],
    }

    _REGEX = re.compile(
        rf'\Ads(\d+)( {types.String._REGEX.pattern})?((?: {types.Real._REGEX.pattern})+?)\Z'
    )

    def __init__(
        self, suffix: types.Integer, js: types.Tuple[types.Real], option: types.String = None
    ):
        """
        Initializes ``Ds_0``.

        Parameters:
            suffix: Data card option suffix.
            option: Dependent variable setting.
            js: Depdented source dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if option is not None and option not in {'h', 'l', 's'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, option)
        if js is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, js)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                option,
                js,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.option: typing.Final[types.String] = option
        self.js: typing.Final[types.Tuple[types.Real]] = js
