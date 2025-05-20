import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Asleft(BlockOption):
    """
    Represents INP asleft elements.

    Attributes:
        setting: Right-going flux at plane i.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aasleft( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Asleft``.

        Parameters:
            setting: Right-going flux at plane i.

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
class AsleftBuilder:
    """
    Builds ``Asleft``.

    Attributes:
        setting: Right-going flux at plane i.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``AsleftBuilder`` into ``Asleft``.

        Returns:
            ``Asleft`` for ``AsleftBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Asleft(
            setting=setting,
        )
