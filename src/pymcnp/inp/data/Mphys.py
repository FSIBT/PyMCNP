import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Mphys(DataOption, keyword='mphys'):
    """
    Represents INP mphys elements.

    Attributes:
        setting: Physics models on/off.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Amphys( {types.String._REGEX.pattern})?\Z')

    def __init__(self, setting: types.String = None):
        """
        Initializes ``Mphys``.

        Parameters:
            setting: Physics models on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is not None and setting not in {'on', 'off'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class MphysBuilder:
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

        setting = None
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Mphys(
            setting=setting,
        )
