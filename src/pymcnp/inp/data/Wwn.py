import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwn(DataOption_, keyword='wwn'):
    """
    Represents INP wwn elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'bounds': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'wwn(\S+):(\S+)(( {types.Real._REGEX.pattern})+)')

    def __init__(
        self, suffix: types.Integer, designator: types.Designator, bounds: types.Tuple[types.Real]
    ):
        """
        Initializes ``Wwn``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            bounds: Lower weight bound.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds
