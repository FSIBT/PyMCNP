import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Unc(CellOption_, keyword='unc'):
    """
    Represents INP unc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'setting': types.Integer,
    }

    _REGEX = re.compile(r'unc:(\S+)( \S+)')

    def __init__(self, designator: types.Designator, setting: types.Integer):
        """
        Initializes ``Unc``.

        Parameters:
            designator: Cell particle designator.
            setting: Cell uncollided secondaries setting.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.setting: typing.Final[types.Integer] = setting
