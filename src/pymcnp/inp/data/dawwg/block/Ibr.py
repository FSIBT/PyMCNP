import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ibr(BlockOption):
    """
    Represents INP ibr elements.

    Attributes:
        setting: Right boudary condition.
    """

    _KEYWORD = 'ibr'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aibr( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Ibr``.

        Parameters:
            setting: Right boudary condition.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class IbrBuilder:
    """
    Builds ``Ibr``.

    Attributes:
        setting: Right boudary condition.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``IbrBuilder`` into ``Ibr``.

        Returns:
            ``Ibr`` for ``IbrBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Ibr(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Ibr):
        """
        Unbuilds ``Ibr`` into ``IbrBuilder``

        Returns:
            ``IbrBuilder`` for ``Ibr``.
        """

        return Ibr(
            setting=copy.deepcopy(ast.setting),
        )
