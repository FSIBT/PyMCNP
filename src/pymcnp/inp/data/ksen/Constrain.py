import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Constrain(_option.KsenOption):
    """
    Represents INP constrain elements.

    Attributes:
        setting: Renormalize sensitivity distribution on/off.
    """

    _KEYWORD = 'constrain'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aconstrain( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Constrain``.

        Parameters:
            setting: Renormalize sensitivity distribution on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class ConstrainBuilder(_option.KsenOptionBuilder):
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

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Constrain(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Constrain):
        """
        Unbuilds ``Constrain`` into ``ConstrainBuilder``

        Returns:
            ``ConstrainBuilder`` for ``Constrain``.
        """

        return ConstrainBuilder(
            setting=copy.deepcopy(ast.setting),
        )
