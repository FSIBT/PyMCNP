import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Mx(DataOption_, keyword='mx'):
    """
    Represents INP mx elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(r'mx(\S+):(\S+)(( \S+)+)')

    def __init__(
        self, suffix: types.Integer, designator: types.Designator, zaids: types.Tuple[types.Zaid]
    ):
        """
        Initializes ``Mx``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            zaids: Zaid substitutions for particles.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zaids)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaids,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.zaids: typing.Final[types.Tuple[types.Zaid]] = zaids
