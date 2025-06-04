import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Rzmflux(BlockOption):
    """
    Represents INP rzmflux elements.

    Attributes:
        setting: Write b-flux file on/off.
    """

    _KEYWORD = 'rzmflux'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Arzmflux( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Rzmflux``.

        Parameters:
            setting: Write b-flux file on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class RzmfluxBuilder:
    """
    Builds ``Rzmflux``.

    Attributes:
        setting: Write b-flux file on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``RzmfluxBuilder`` into ``Rzmflux``.

        Returns:
            ``Rzmflux`` for ``RzmfluxBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Rzmflux(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Rzmflux):
        """
        Unbuilds ``Rzmflux`` into ``RzmfluxBuilder``

        Returns:
            ``RzmfluxBuilder`` for ``Rzmflux``.
        """

        return Rzmflux(
            setting=copy.deepcopy(ast.setting),
        )
