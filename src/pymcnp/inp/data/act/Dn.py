import re
import typing


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Dn(ActOption_, keyword='dn'):
    """
    Represents INP dn elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'source': types.String,
    }

    _REGEX = re.compile(rf'\Adn( {types.String._REGEX.pattern})\Z')

    def __init__(self, source: types.String):
        """
        Initializes ``Dn``.

        Parameters:
            source: Delayed neutron data source.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if source is None or source not in {'model', 'library', 'both', 'prompt'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, source)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                source,
            ]
        )

        self.source: typing.Final[types.String] = source
