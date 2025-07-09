import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Fluxone(_option.BlockOption):
    """
    Represents INP fluxone elements.

    Attributes:
        setting: Flux override on/off.
    """

    _KEYWORD = 'fluxone'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Afluxone( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Fluxone``.

        Parameters:
            setting: Flux override on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class FluxoneBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Fluxone``.

    Attributes:
        setting: Flux override on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``FluxoneBuilder`` into ``Fluxone``.

        Returns:
            ``Fluxone`` for ``FluxoneBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Fluxone(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Fluxone):
        """
        Unbuilds ``Fluxone`` into ``FluxoneBuilder``

        Returns:
            ``FluxoneBuilder`` for ``Fluxone``.
        """

        return FluxoneBuilder(
            setting=copy.deepcopy(ast.setting),
        )
