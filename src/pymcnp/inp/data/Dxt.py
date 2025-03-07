import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Dxt(DataOption_, keyword='dxt'):
    """
    Represents INP dxt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'spheres_1': types.Shell,
        'spheres_2': types.Shell,
        'spheres_3': types.Shell,
        'spheres_4': types.Shell,
        'spheres_5': types.Shell,
        'spheres_6': types.Shell,
        'spheres_7': types.Shell,
        'spheres_8': types.Shell,
        'spheres_9': types.Shell,
        'spheres_10': types.Shell,
        'cutoff_1': types.Real,
        'cutoff_2': types.Real,
        'weight': types.Real,
    }

    _REGEX = re.compile(
        rf'dxt:(\S+)( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(
        self,
        designator: types.Designator,
        spheres_1: types.Shell,
        spheres_2: types.Shell,
        spheres_3: types.Shell,
        spheres_4: types.Shell,
        spheres_5: types.Shell,
        spheres_6: types.Shell,
        spheres_7: types.Shell,
        spheres_8: types.Shell,
        spheres_9: types.Shell,
        spheres_10: types.Shell,
        cutoff_1: types.Real,
        cutoff_2: types.Real,
        weight: types.Real,
    ):
        """
        Initializes ``Dxt``.

        Parameters:
            designator: Data card particle designator.
            spheres_1: DXTRAN spheres #1.
            spheres_2: DXTRAN spheres #2.
            spheres_3: DXTRAN spheres #3.
            spheres_4: DXTRAN spheres #4.
            spheres_5: DXTRAN spheres #5.
            spheres_6: DXTRAN spheres #6.
            spheres_7: DXTRAN spheres #7.
            spheres_8: DXTRAN spheres #8.
            spheres_9: DXTRAN spheres #9.
            spheres_10: DXTRAN spheres #10.
            cutoff_1: Upper weight cutoff in the spheres.
            cutoff_2: Lower weight cutoff in the spheres.
            weight: Minimum photon weight.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if spheres_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres_1)
        if spheres_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres_2)
        if spheres_3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres_3)
        if spheres_4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres_4)
        if spheres_5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres_5)
        if spheres_6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres_6)
        if spheres_7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres_7)
        if spheres_8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres_8)
        if spheres_9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres_9)
        if spheres_10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres_10)
        if cutoff_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutoff_1)
        if cutoff_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutoff_2)
        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weight)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                spheres_1,
                spheres_2,
                spheres_3,
                spheres_4,
                spheres_5,
                spheres_6,
                spheres_7,
                spheres_8,
                spheres_9,
                spheres_10,
                cutoff_1,
                cutoff_2,
                weight,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.spheres_1: typing.Final[types.Shell] = spheres_1
        self.spheres_2: typing.Final[types.Shell] = spheres_2
        self.spheres_3: typing.Final[types.Shell] = spheres_3
        self.spheres_4: typing.Final[types.Shell] = spheres_4
        self.spheres_5: typing.Final[types.Shell] = spheres_5
        self.spheres_6: typing.Final[types.Shell] = spheres_6
        self.spheres_7: typing.Final[types.Shell] = spheres_7
        self.spheres_8: typing.Final[types.Shell] = spheres_8
        self.spheres_9: typing.Final[types.Shell] = spheres_9
        self.spheres_10: typing.Final[types.Shell] = spheres_10
        self.cutoff_1: typing.Final[types.Real] = cutoff_1
        self.cutoff_2: typing.Final[types.Real] = cutoff_2
        self.weight: typing.Final[types.Real] = weight
