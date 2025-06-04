import re
import copy
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Nrm(SdefOption):
    """
    Represents INP nrm elements.

    Attributes:
        sign: Sign of the surface normal.
    """

    _KEYWORD = 'nrm'

    _ATTRS = {
        'sign': types.Integer,
    }

    _REGEX = re.compile(rf'\Anrm( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, sign: types.Integer):
        """
        Initializes ``Nrm``.

        Parameters:
            sign: Sign of the surface normal.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if sign is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, sign)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                sign,
            ]
        )

        self.sign: typing.Final[types.Integer] = sign


@dataclasses.dataclass
class NrmBuilder:
    """
    Builds ``Nrm``.

    Attributes:
        sign: Sign of the surface normal.
    """

    sign: str | int | types.Integer

    def build(self):
        """
        Builds ``NrmBuilder`` into ``Nrm``.

        Returns:
            ``Nrm`` for ``NrmBuilder``.
        """

        sign = self.sign
        if isinstance(self.sign, types.Integer):
            sign = self.sign
        elif isinstance(self.sign, int):
            sign = types.Integer(self.sign)
        elif isinstance(self.sign, str):
            sign = types.Integer.from_mcnp(self.sign)

        return Nrm(
            sign=sign,
        )

    @staticmethod
    def unbuild(ast: Nrm):
        """
        Unbuilds ``Nrm`` into ``NrmBuilder``

        Returns:
            ``NrmBuilder`` for ``Nrm``.
        """

        return Nrm(
            sign=copy.deepcopy(ast.sign),
        )
