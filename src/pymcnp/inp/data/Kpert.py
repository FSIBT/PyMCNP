import re
import typing


from . import kpert
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Kpert(DataOption_, keyword='kpert'):
    """
    Represents INP kpert elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'options': types.Tuple[kpert.KpertOption_],
    }

    _REGEX = re.compile(rf'\Akpert(\d+)((?: (?:{kpert.KpertOption_._REGEX.pattern}))+?)?\Z')

    def __init__(
        self, suffix: types.Integer, options: types.Tuple[kpert.KpertOption_] = None
    ):
        """
        Initializes ``Kpert``.

        Parameters:
            suffix: Data card option suffix.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (0 < suffix <= 10_000):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.IntegerOrJump] = suffix
        self.options: typing.Final[types.Tuple[kpert.KpertOption_]] = options
