import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Fmatnx(KoptsOption_, keyword='fmatnx'):
    """
    Represents INP fmatnx elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'fmat_nx': types.Real,
    }

    _REGEX = re.compile(rf'\Afmatnx( {types.Real._REGEX.pattern})\Z')

    def __init__(self, fmat_nx: types.Real):
        """
        Initializes ``Fmatnx``.

        Parameters:
            fmat_nx: fmat_nx.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_nx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_nx)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_nx,
            ]
        )

        self.fmat_nx: typing.Final[types.Real] = fmat_nx
