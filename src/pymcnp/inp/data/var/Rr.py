import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Rr(_option.VarOption):
    """
    Represents INP rr elements.

    Attributes:
        setting: Roulette game for weight windows and cell/energy/time importance off/no.
    """

    _KEYWORD = 'rr'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Arr( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Rr``.

        Parameters:
            setting: Roulette game for weight windows and cell/energy/time importance off/no.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'no', 'off'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class RrBuilder(_option.VarOptionBuilder):
    """
    Builds ``Rr``.

    Attributes:
        setting: Roulette game for weight windows and cell/energy/time importance off/no.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``RrBuilder`` into ``Rr``.

        Returns:
            ``Rr`` for ``RrBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Rr(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Rr):
        """
        Unbuilds ``Rr`` into ``RrBuilder``

        Returns:
            ``RrBuilder`` for ``Rr``.
        """

        return RrBuilder(
            setting=copy.deepcopy(ast.setting),
        )
