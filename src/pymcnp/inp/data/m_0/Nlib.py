import re
import copy
import typing
import dataclasses


from ._option import MOption_0
from ....utils import types
from ....utils import errors


class Nlib(MOption_0):
    """
    Represents INP nlib elements.

    Attributes:
        abx: Default neutron table identifier.
    """

    _KEYWORD = 'nlib'

    _ATTRS = {
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Anlib( {types.String._REGEX.pattern})\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``Nlib``.

        Parameters:
            abx: Default neutron table identifier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if abx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, abx)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                abx,
            ]
        )

        self.abx: typing.Final[types.String] = abx


@dataclasses.dataclass
class NlibBuilder:
    """
    Builds ``Nlib``.

    Attributes:
        abx: Default neutron table identifier.
    """

    abx: str | types.String

    def build(self):
        """
        Builds ``NlibBuilder`` into ``Nlib``.

        Returns:
            ``Nlib`` for ``NlibBuilder``.
        """

        abx = self.abx
        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return Nlib(
            abx=abx,
        )

    @staticmethod
    def unbuild(ast: Nlib):
        """
        Unbuilds ``Nlib`` into ``NlibBuilder``

        Returns:
            ``NlibBuilder`` for ``Nlib``.
        """

        return Nlib(
            abx=copy.deepcopy(ast.abx),
        )
