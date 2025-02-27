import re
import typing


from . import block
from .option_ import DawwgOption_
from ....utils import types
from ....utils import errors


class Block(DawwgOption_, keyword='block'):
    """
    Represents INP block elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
        'options': types.Tuple[block.BlockOption_],
    }

    _REGEX = re.compile(rf'block( \S+)(( ({block.BlockOption_._REGEX.pattern}))+)?')

    def __init__(self, setting: types.Integer, options: types.Tuple[block.BlockOption_] = None):
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

        self.setting: typing.Final[types.Integer] = setting
        self.options: typing.Final[types.Tuple[block.BlockOption_]] = options
