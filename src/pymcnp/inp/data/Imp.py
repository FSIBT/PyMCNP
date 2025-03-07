import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Imp(DataOption_, keyword='imp'):
    """
    Represents INP imp elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'importances': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'imp:(\S+)(( {types.Real._REGEX.pattern})+)')

    def __init__(self, designator: types.Designator, importances: types.Tuple[types.Real]):
        """
        Initializes ``Imp``.

        Parameters:
            designator: Data card particle designator.
            importances: Cell importance.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if importances is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, importances)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                importances,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.importances: typing.Final[types.Tuple[types.Real]] = importances
