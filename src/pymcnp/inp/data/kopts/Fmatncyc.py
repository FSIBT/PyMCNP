import re
import copy
import typing
import dataclasses


from ._option import KoptsOption
from ....utils import types
from ....utils import errors


class Fmatncyc(KoptsOption):
    """
    Represents INP fmatncyc elements.

    Attributes:
        fmat_ncyc: fmat_ncyc.
    """

    _KEYWORD = 'fmatncyc'

    _ATTRS = {
        'fmat_ncyc': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatncyc( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, fmat_ncyc: types.Real):
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

        self.fmat_ncyc: typing.Final[types.Real] = fmat_ncyc


@dataclasses.dataclass
class FmatncycBuilder:
    """
    Builds ``Fmatncyc``.

    Attributes:
        fmat_ncyc: fmat_ncyc.
    """

    fmat_ncyc: str | float | types.Real

    def build(self):
        """
        Builds ``FmatncycBuilder`` into ``Fmatncyc``.

        Returns:
            ``Fmatncyc`` for ``FmatncycBuilder``.
        """

        fmat_ncyc = self.fmat_ncyc
        if isinstance(self.fmat_ncyc, types.Real):
            fmat_ncyc = self.fmat_ncyc
        elif isinstance(self.fmat_ncyc, float) or isinstance(self.fmat_ncyc, int):
            fmat_ncyc = types.Real(self.fmat_ncyc)
        elif isinstance(self.fmat_ncyc, str):
            fmat_ncyc = types.Real.from_mcnp(self.fmat_ncyc)

        return Fmatncyc(
            fmat_ncyc=fmat_ncyc,
        )

    @staticmethod
    def unbuild(ast: Fmatncyc):
        """
        Unbuilds ``Fmatncyc`` into ``FmatncycBuilder``

        Returns:
            ``FmatncycBuilder`` for ``Fmatncyc``.
        """

        return Fmatncyc(
            fmat_ncyc=copy.deepcopy(ast.fmat_ncyc),
        )
