import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Angp(_option.BlockOption):
    """
    Represents INP angp elements.

    Attributes:
        setting: Print angular flux on/off.
    """

    _KEYWORD = 'angp'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aangp( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Angp``.

        Parameters:
            setting: Print angular flux on/off.

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
class AngpBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Angp``.

    Attributes:
        setting: Print angular flux on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``AngpBuilder`` into ``Angp``.

        Returns:
            ``Angp`` for ``AngpBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Angp(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Angp):
        """
        Unbuilds ``Angp`` into ``AngpBuilder``

        Returns:
            ``AngpBuilder`` for ``Angp``.
        """

        return AngpBuilder(
            setting=copy.deepcopy(ast.setting),
        )
