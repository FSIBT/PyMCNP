import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Balxs(BlockOption):
    """
    Represents INP balxs elements.

    Attributes:
        setting: Cross-section balance control.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Abalxs( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Balxs``.

        Parameters:
            setting: Cross-section balance control.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {-1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class BalxsBuilder:
    """
    Builds ``Balxs``.

    Attributes:
        setting: Cross-section balance control.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``BalxsBuilder`` into ``Balxs``.

        Returns:
            ``Balxs`` for ``BalxsBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Balxs(
            setting=setting,
        )
