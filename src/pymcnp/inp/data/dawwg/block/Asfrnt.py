import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Asfrnt(BlockOption):
    """
    Represents INP asfrnt elements.

    Attributes:
        setting: Back-going flux at plane k.
    """

    _KEYWORD = 'asfrnt'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aasfrnt( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Asfrnt``.

        Parameters:
            setting: Back-going flux at plane k.

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
class AsfrntBuilder:
    """
    Builds ``Asfrnt``.

    Attributes:
        setting: Back-going flux at plane k.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``AsfrntBuilder`` into ``Asfrnt``.

        Returns:
            ``Asfrnt`` for ``AsfrntBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Asfrnt(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Asfrnt):
        """
        Unbuilds ``Asfrnt`` into ``AsfrntBuilder``

        Returns:
            ``AsfrntBuilder`` for ``Asfrnt``.
        """

        return Asfrnt(
            setting=copy.deepcopy(ast.setting),
        )
