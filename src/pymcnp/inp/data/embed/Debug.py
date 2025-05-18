import re
import typing
import dataclasses


from ._option import EmbedOption
from ....utils import types
from ....utils import errors


class Debug(EmbedOption):
    """
    Represents INP debug elements.

    Attributes:
        parameter: Debug parameter.
    """

    _ATTRS = {
        'parameter': types.String,
    }

    _REGEX = re.compile(rf'\Adebug( {types.String._REGEX.pattern})\Z')

    def __init__(self, parameter: types.String):
        """
        Initializes ``Debug``.

        Parameters:
            parameter: Debug parameter.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if parameter is None or parameter not in {'echomesh'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, parameter)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                parameter,
            ]
        )

        self.parameter: typing.Final[types.String] = parameter


@dataclasses.dataclass
class DebugBuilder:
    """
    Builds ``Debug``.

    Attributes:
        parameter: Debug parameter.
    """

    parameter: str | types.String

    def build(self):
        """
        Builds ``DebugBuilder`` into ``Debug``.

        Returns:
            ``Debug`` for ``DebugBuilder``.
        """

        parameter = self.parameter
        if isinstance(self.parameter, types.String):
            parameter = self.parameter
        elif isinstance(self.parameter, str):
            parameter = types.String.from_mcnp(self.parameter)

        return Debug(
            parameter=parameter,
        )
