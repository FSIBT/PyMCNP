import re
import typing
import dataclasses


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Fmatskpt(KoptsOption_, keyword='fmatskpt'):
    """
    Represents INP fmatskpt elements.

    Attributes:
        fmat_skip: fmat_skip.
    """

    _ATTRS = {
        'fmat_skip': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afmatskpt( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fmat_skip: types.RealOrJump):
        """
        Initializes ``Fmatskpt``.

        Parameters:
            fmat_skip: fmat_skip.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_skip is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_skip)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_skip,
            ]
        )

        self.fmat_skip: typing.Final[types.RealOrJump] = fmat_skip


@dataclasses.dataclass
class FmatskptBuilder:
    """
    Builds ``Fmatskpt``.

    Attributes:
        fmat_skip: fmat_skip.
    """

    fmat_skip: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``FmatskptBuilder`` into ``Fmatskpt``.

        Returns:
            ``Fmatskpt`` for ``FmatskptBuilder``.
        """

        if isinstance(self.fmat_skip, types.Real):
            fmat_skip = self.fmat_skip
        elif isinstance(self.fmat_skip, float) or isinstance(self.fmat_skip, int):
            fmat_skip = types.RealOrJump(self.fmat_skip)
        elif isinstance(self.fmat_skip, str):
            fmat_skip = types.RealOrJump.from_mcnp(self.fmat_skip)

        return Fmatskpt(
            fmat_skip=fmat_skip,
        )
