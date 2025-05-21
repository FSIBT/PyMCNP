import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ievt(BlockOption):
    """
    Represents INP ievt elements.

    Attributes:
        setting: Calculation type.
    """

    _KEYWORD = 'ievt'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aievt( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Ievt``.

        Parameters:
            setting: Calculation type.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1, 2, 3, 4}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class IevtBuilder:
    """
    Builds ``Ievt``.

    Attributes:
        setting: Calculation type.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``IevtBuilder`` into ``Ievt``.

        Returns:
            ``Ievt`` for ``IevtBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Ievt(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Ievt):
        """
        Unbuilds ``Ievt`` into ``IevtBuilder``

        Returns:
            ``IevtBuilder`` for ``Ievt``.
        """

        return Ievt(
            setting=copy.deepcopy(ast.setting),
        )
