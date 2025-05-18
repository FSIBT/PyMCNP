import re
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

    _ATTRS = {
        'sign': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Anrm( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, sign: types.IntegerOrJump):
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

        self.sign: typing.Final[types.IntegerOrJump] = sign


@dataclasses.dataclass
class NrmBuilder:
    """
    Builds ``Nrm``.

    Attributes:
        sign: Sign of the surface normal.
    """

    sign: str | int | types.IntegerOrJump

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
            sign = types.IntegerOrJump(self.sign)
        elif isinstance(self.sign, str):
            sign = types.IntegerOrJump.from_mcnp(self.sign)

        return Nrm(
            sign=sign,
        )
