import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Unc(_option.CellOption):
    """
    Represents INP unc elements.

    Attributes:
        designator: Cell particle designator.
        setting: Cell uncollided secondaries setting.
    """

    _KEYWORD = 'unc'

    _ATTRS = {
        'designator': types.Designator,
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aunc:(\S+)( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, designator: types.Designator, setting: types.Integer):
        """
        Initializes ``Unc``.

        Parameters:
            designator: Cell particle designator.
            setting: Cell uncollided secondaries setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class UncBuilder(_option.CellOptionBuilder):
    """
    Builds ``Unc``.

    Attributes:
        designator: Cell particle designator.
        setting: Cell uncollided secondaries setting.
    """

    designator: str | types.Designator
    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``UncBuilder`` into ``Unc``.

        Returns:
            ``Unc`` for ``UncBuilder``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Unc(
            designator=designator,
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Unc):
        """
        Unbuilds ``Unc`` into ``UncBuilder``

        Returns:
            ``UncBuilder`` for ``Unc``.
        """

        return UncBuilder(
            designator=copy.deepcopy(ast.designator),
            setting=copy.deepcopy(ast.setting),
        )
