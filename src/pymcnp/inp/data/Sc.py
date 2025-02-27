import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Sc(DataOption_, keyword='sc'):
    """
    Represents INP sc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'comment': types.Tuple[str],
    }

    _REGEX = re.compile(r'sc(\S+)(( \S+)+)')

    def __init__(self, suffix: types.Integer, comment: types.Tuple[str]):
        """
        Initializes ``Sc``.

        Parameters:
            suffix: Data card option suffix.
            comment: source comment.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if comment is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, comment)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                comment,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.comment: typing.Final[types.Tuple[str]] = comment
