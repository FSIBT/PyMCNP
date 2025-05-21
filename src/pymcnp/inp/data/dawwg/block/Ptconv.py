import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ptconv(BlockOption):
    """
    Represents INP ptconv elements.

    Attributes:
        setting: Special criticality convergence scheme on/off.
    """

    _KEYWORD = 'ptconv'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aptconv( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Ptconv``.

        Parameters:
            setting: Special criticality convergence scheme on/off.

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
class PtconvBuilder:
    """
    Builds ``Ptconv``.

    Attributes:
        setting: Special criticality convergence scheme on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``PtconvBuilder`` into ``Ptconv``.

        Returns:
            ``Ptconv`` for ``PtconvBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Ptconv(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Ptconv):
        """
        Unbuilds ``Ptconv`` into ``PtconvBuilder``

        Returns:
            ``PtconvBuilder`` for ``Ptconv``.
        """

        return Ptconv(
            setting=copy.deepcopy(ast.setting),
        )
