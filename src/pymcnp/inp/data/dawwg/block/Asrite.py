import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Asrite(BlockOption):
    """
    Represents INP asrite elements.

    Attributes:
        setting: Left-going flux at plane i.
    """

    _KEYWORD = 'asrite'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aasrite( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Asrite``.

        Parameters:
            setting: Left-going flux at plane i.

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
class AsriteBuilder:
    """
    Builds ``Asrite``.

    Attributes:
        setting: Left-going flux at plane i.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``AsriteBuilder`` into ``Asrite``.

        Returns:
            ``Asrite`` for ``AsriteBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Asrite(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Asrite):
        """
        Unbuilds ``Asrite`` into ``AsriteBuilder``

        Returns:
            ``AsriteBuilder`` for ``Asrite``.
        """

        return Asrite(
            setting=copy.deepcopy(ast.setting),
        )
