import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ibfrnt(BlockOption):
    """
    Represents INP ibfrnt elements.

    Attributes:
        setting: Front boudary condition.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aibfrnt( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Ibfrnt``.

        Parameters:
            setting: Front boudary condition.

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
class IbfrntBuilder:
    """
    Builds ``Ibfrnt``.

    Attributes:
        setting: Front boudary condition.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``IbfrntBuilder`` into ``Ibfrnt``.

        Returns:
            ``Ibfrnt`` for ``IbfrntBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Ibfrnt(
            setting=setting,
        )
