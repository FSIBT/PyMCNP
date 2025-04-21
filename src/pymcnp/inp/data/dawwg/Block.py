import re
import typing
import dataclasses


from . import block
from ._option import DawwgOption
from ....utils import types
from ....utils import errors


class Block(DawwgOption, keyword='block'):
    """
    Represents INP block elements.

    Attributes:
        setting: Destination of key-value pairs.
        options: Dictionary of dawwg block options.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
        'options': types.Tuple[block.BlockOption],
    }

    _REGEX = re.compile(
        rf'\Ablock( {types.IntegerOrJump._REGEX.pattern})((?: (?:{block.BlockOption._REGEX.pattern}))+?)?\Z'
    )

    def __init__(
        self, setting: types.IntegerOrJump, options: types.Tuple[block.BlockOption] = None
    ):
        """
        Initializes ``Block``.

        Parameters:
            setting: Destination of key-value pairs.
            options: Dictionary of dawwg block options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {1, 3, 5, 6}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
                options,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting
        self.options: typing.Final[types.Tuple[block.BlockOption]] = options


@dataclasses.dataclass
class BlockBuilder:
    """
    Builds ``Block``.

    Attributes:
        setting: Destination of key-value pairs.
        options: Dictionary of dawwg block options.
    """

    setting: str | int | types.IntegerOrJump
    options: list[str] | list[block.BlockOption] = None

    def build(self):
        """
        Builds ``BlockBuilder`` into ``Block``.

        Returns:
            ``Block`` for ``BlockBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        options = []
        for item in self.options:
            if isinstance(item, block.BlockOption):
                options.append(item)
            elif isinstance(item, str):
                options.append(block.BlockOption.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Block(
            setting=setting,
            options=options,
        )
