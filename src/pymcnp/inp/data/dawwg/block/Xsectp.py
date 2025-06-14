import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Xsectp(_option.BlockOption):
    """
    Represents INP xsectp elements.

    Attributes:
        setting: Cross-section print flag.
    """

    _KEYWORD = 'xsectp'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Axsectp( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Xsectp``.

        Parameters:
            setting: Cross-section print flag.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class XsectpBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Xsectp``.

    Attributes:
        setting: Cross-section print flag.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``XsectpBuilder`` into ``Xsectp``.

        Returns:
            ``Xsectp`` for ``XsectpBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Xsectp(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Xsectp):
        """
        Unbuilds ``Xsectp`` into ``XsectpBuilder``

        Returns:
            ``XsectpBuilder`` for ``Xsectp``.
        """

        return XsectpBuilder(
            setting=copy.deepcopy(ast.setting),
        )
