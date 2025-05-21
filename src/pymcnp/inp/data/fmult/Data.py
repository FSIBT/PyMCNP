import re
import copy
import typing
import dataclasses


from ._option import FmultOption
from ....utils import types
from ....utils import errors


class Data(FmultOption):
    """
    Represents INP data elements.

    Attributes:
        setting: Sampling method setting.
    """

    _KEYWORD = 'data'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Adata( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Data``.

        Parameters:
            setting: Sampling method setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class DataBuilder:
    """
    Builds ``Data``.

    Attributes:
        setting: Sampling method setting.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``DataBuilder`` into ``Data``.

        Returns:
            ``Data`` for ``DataBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Data(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Data):
        """
        Unbuilds ``Data`` into ``DataBuilder``

        Returns:
            ``DataBuilder`` for ``Data``.
        """

        return Data(
            setting=copy.deepcopy(ast.setting),
        )
