import re
import typing
import dataclasses


from ._option import KoptsOption
from ....utils import types
from ....utils import errors


class Fmatncyc(KoptsOption, keyword='fmatncyc'):
    """
    Represents INP fmatncyc elements.

    Attributes:
        fmat_ncyc: fmat_ncyc.
    """

    _ATTRS = {
        'fmat_ncyc': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afmatncyc( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fmat_ncyc: types.RealOrJump):
        """
        Initializes ``Fmatncyc``.

        Parameters:
            fmat_ncyc: fmat_ncyc.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if fmat_ncyc is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fmat_ncyc)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_ncyc,
            ]
        )

        self.fmat_ncyc: typing.Final[types.RealOrJump] = fmat_ncyc


@dataclasses.dataclass
class FmatncycBuilder:
    """
    Builds ``Fmatncyc``.

    Attributes:
        fmat_ncyc: fmat_ncyc.
    """

    fmat_ncyc: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``FmatncycBuilder`` into ``Fmatncyc``.

        Returns:
            ``Fmatncyc`` for ``FmatncycBuilder``.
        """

        if isinstance(self.fmat_ncyc, types.Real):
            fmat_ncyc = self.fmat_ncyc
        elif isinstance(self.fmat_ncyc, float) or isinstance(self.fmat_ncyc, int):
            fmat_ncyc = types.RealOrJump(self.fmat_ncyc)
        elif isinstance(self.fmat_ncyc, str):
            fmat_ncyc = types.RealOrJump.from_mcnp(self.fmat_ncyc)

        return Fmatncyc(
            fmat_ncyc=fmat_ncyc,
        )
