import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Nomacr(BlockOption):
    """
    Represents INP nomacr elements.

    Attributes:
        setting: Suppress writing MACRXS on/off.
    """

    _KEYWORD = 'nomacr'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Anomacr( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Nomacr``.

        Parameters:
            setting: Suppress writing MACRXS on/off.

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
class NomacrBuilder:
    """
    Builds ``Nomacr``.

    Attributes:
        setting: Suppress writing MACRXS on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``NomacrBuilder`` into ``Nomacr``.

        Returns:
            ``Nomacr`` for ``NomacrBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Nomacr(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Nomacr):
        """
        Unbuilds ``Nomacr`` into ``NomacrBuilder``

        Returns:
            ``NomacrBuilder`` for ``Nomacr``.
        """

        return Nomacr(
            setting=copy.deepcopy(ast.setting),
        )
