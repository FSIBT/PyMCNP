import re
import typing


from . import fmesh
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fmesh(DataOption_, keyword='fmesh'):
    """
    Represents INP fmesh elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'options': types.Tuple[fmesh.FmeshOption_],
    }

    _REGEX = re.compile(rf'\Afmesh(\d+):(\S+)((?: (?:{fmesh.FmeshOption_._REGEX.pattern}))+?)?\Z')

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        options: types.Tuple[fmesh.FmeshOption_] = None,
    ):
        """
        Initializes ``Fmesh``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (0 < suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.options: typing.Final[types.Tuple[fmesh.FmeshOption_]] = options
