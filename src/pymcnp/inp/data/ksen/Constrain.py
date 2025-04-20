import re
import typing
import dataclasses


from .option_ import KsenOption_
from ....utils import types
from ....utils import errors


class Constrain(KsenOption_, keyword='constrain'):
    """
    Represents INP constrain elements.

    Attributes:
        setting: Renormalize sensitivity distribution on/off.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aconstrain( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Constrain``.

        Parameters:
            setting: Renormalize sensitivity distribution on/off.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class ConstrainBuilder:
    """
    Builds ``Constrain``.

    Attributes:
        setting: Renormalize sensitivity distribution on/off.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``ConstrainBuilder`` into ``Constrain``.

        Returns:
            ``Constrain`` for ``ConstrainBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Constrain(
            setting=setting,
        )
