import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ajed(BlockOption):
    """
    Represents INP ajed elements.

    Attributes:
        setting: Regular/adjoint edits control.
    """

    _KEYWORD = 'ajed'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aajed( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Ajed``.

        Parameters:
            setting: Regular/adjoint edits control.

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
class AjedBuilder:
    """
    Builds ``Ajed``.

    Attributes:
        setting: Regular/adjoint edits control.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``AjedBuilder`` into ``Ajed``.

        Returns:
            ``Ajed`` for ``AjedBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Ajed(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Ajed):
        """
        Unbuilds ``Ajed`` into ``AjedBuilder``

        Returns:
            ``AjedBuilder`` for ``Ajed``.
        """

        return Ajed(
            setting=copy.deepcopy(ast.setting),
        )
