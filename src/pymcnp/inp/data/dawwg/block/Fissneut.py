import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Fissneut(_option.BlockOption):
    """
    Represents INP fissneut elements.

    Attributes:
        setting: Fission neutron flag.
    """

    _KEYWORD = 'fissneut'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Afissneut( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Fissneut``.

        Parameters:
            setting: Fission neutron flag.

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
class FissneutBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Fissneut``.

    Attributes:
        setting: Fission neutron flag.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``FissneutBuilder`` into ``Fissneut``.

        Returns:
            ``Fissneut`` for ``FissneutBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Fissneut(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Fissneut):
        """
        Unbuilds ``Fissneut`` into ``FissneutBuilder``

        Returns:
            ``FissneutBuilder`` for ``Fissneut``.
        """

        return FissneutBuilder(
            setting=copy.deepcopy(ast.setting),
        )
