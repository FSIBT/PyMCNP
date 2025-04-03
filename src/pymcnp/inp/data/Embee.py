import re
import typing


from . import embee
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Embee(DataOption_, keyword='embee'):
    """
    Represents INP embee elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[embee.EmbeeOption_],
    }

    _REGEX = re.compile(rf'\Aembee(\d+)((?: (?:{embee.EmbeeOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, suffix: types.Integer, options: types.Tuple[embee.EmbeeOption_] = None):
        """
        Initializes ``Embee``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.options: typing.Final[types.Tuple[embee.EmbeeOption_]] = options
