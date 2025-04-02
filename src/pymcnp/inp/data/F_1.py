import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class F_1(DataOption_, keyword='f'):
    """
    Represents INP f_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'spheres': types.Tuple[types.Sphere],
        'nd': types.String,
    }

    _REGEX = re.compile(rf'\Af(\d*[5]):(\S+)((?: {types.Sphere._REGEX.pattern})+?)( nd)?\Z')

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        spheres: types.Tuple[types.Sphere],
        nd: types.String = None,
    ):
        """
        Initializes ``F_1``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            spheres: Detector points.
            nd: Total/average specified surfaces/cells option.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 == 5):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if spheres is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                spheres,
                nd,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.spheres: typing.Final[types.Tuple[types.Sphere]] = spheres
        self.nd: typing.Final[types.String] = nd
