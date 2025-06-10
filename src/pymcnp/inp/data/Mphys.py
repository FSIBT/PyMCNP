import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Mphys(_option.DataOption):
    """
    Represents INP mphys elements.

    Attributes:
        setting: Physics models on/off.
    """

    _KEYWORD = 'mphys'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Amphys( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, setting: types.String = None):
        """
        Initializes ``Mphys``.

        Parameters:
            setting: Physics models on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is not None and setting.value not in {'on', 'off'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class MphysBuilder(_option.DataOptionBuilder):
    """
    Builds ``Mphys``.

    Attributes:
        setting: Physics models on/off.
    """

    setting: str | types.String = None

    def build(self):
        """
        Builds ``MphysBuilder`` into ``Mphys``.

        Returns:
            ``Mphys`` for ``MphysBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Mphys(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Mphys):
        """
        Unbuilds ``Mphys`` into ``MphysBuilder``

        Returns:
            ``MphysBuilder`` for ``Mphys``.
        """

        return MphysBuilder(
            setting=copy.deepcopy(ast.setting),
        )
