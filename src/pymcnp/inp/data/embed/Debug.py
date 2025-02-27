import re
import typing


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Debug(EmbedOption_, keyword='debug'):
    """
    Represents INP debug elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'parameter': types.String,
    }

    _REGEX = re.compile(r'debug( \S+)')

    def __init__(self, parameter: types.String):
        """
        Initializes ``Debug``.

        Parameters:
            parameter: Debug parameter.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if parameter is None or parameter not in {'echomesh'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, parameter)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                parameter,
            ]
        )

        self.parameter: typing.Final[types.String] = parameter
