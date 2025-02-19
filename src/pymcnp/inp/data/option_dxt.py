import re
import typing

from . import dxt
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Dxt(_option.DataOption_, keyword='dxt'):
    """
    Represents INP data card dxt options.

    Attributes:
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
        designator: Data card particle designator.
    """

    _REGEX = re.compile(
        r'\Adxt:(\S+?)( ( \S+)( \S+)( \S+)( \S+)( \S+))( ( \S+)( \S+)( \S+)( \S+)( \S+))( ( \S+)( \S+)( \S+)( \S+)( \S+))( ( \S+)( \S+)( \S+)( \S+)( \S+))( ( \S+)( \S+)( \S+)( \S+)( \S+))( ( \S+)( \S+)( \S+)( \S+)( \S+))( ( \S+)( \S+)( \S+)( \S+)( \S+))( ( \S+)( \S+)( \S+)( \S+)( \S+))( ( \S+)( \S+)( \S+)( \S+)( \S+))( ( \S+)( \S+)( \S+)( \S+)( \S+))( \S+)( \S+)( \S+)\Z'
    )

    def __init__(
        self,
        spheres_1: dxt.DxtEntry_Sphere,
        spheres_2: dxt.DxtEntry_Sphere,
        spheres_3: dxt.DxtEntry_Sphere,
        spheres_4: dxt.DxtEntry_Sphere,
        spheres_5: dxt.DxtEntry_Sphere,
        spheres_6: dxt.DxtEntry_Sphere,
        spheres_7: dxt.DxtEntry_Sphere,
        spheres_8: dxt.DxtEntry_Sphere,
        spheres_9: dxt.DxtEntry_Sphere,
        spheres_10: dxt.DxtEntry_Sphere,
        cutoff_1: types.Real,
        cutoff_2: types.Real,
        weight: types.Real,
        designator: types.Designator,
    ):
        """
        Initializes ``DataOption_Dxt``.

        Parameters:
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
            designator: Data card particle designator.

        Returns:
            ``DataOption_Dxt``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

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
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple(
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
        self.spheres_1: typing.Final[dxt.DxtEntry_Sphere] = spheres_1
        self.spheres_2: typing.Final[dxt.DxtEntry_Sphere] = spheres_2
        self.spheres_3: typing.Final[dxt.DxtEntry_Sphere] = spheres_3
        self.spheres_4: typing.Final[dxt.DxtEntry_Sphere] = spheres_4
        self.spheres_5: typing.Final[dxt.DxtEntry_Sphere] = spheres_5
        self.spheres_6: typing.Final[dxt.DxtEntry_Sphere] = spheres_6
        self.spheres_7: typing.Final[dxt.DxtEntry_Sphere] = spheres_7
        self.spheres_8: typing.Final[dxt.DxtEntry_Sphere] = spheres_8
        self.spheres_9: typing.Final[dxt.DxtEntry_Sphere] = spheres_9
        self.spheres_10: typing.Final[dxt.DxtEntry_Sphere] = spheres_10
        self.cutoff_1: typing.Final[types.Real] = cutoff_1
        self.cutoff_2: typing.Final[types.Real] = cutoff_2
        self.weight: typing.Final[types.Real] = weight
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Dxt`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Dxt``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Dxt._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        designator = types.Designator.from_mcnp(tokens[1])
        spheres_1 = dxt.DxtEntry_Sphere.from_mcnp(tokens[2])
        spheres_2 = dxt.DxtEntry_Sphere.from_mcnp(tokens[3])
        spheres_3 = dxt.DxtEntry_Sphere.from_mcnp(tokens[4])
        spheres_4 = dxt.DxtEntry_Sphere.from_mcnp(tokens[5])
        spheres_5 = dxt.DxtEntry_Sphere.from_mcnp(tokens[6])
        spheres_6 = dxt.DxtEntry_Sphere.from_mcnp(tokens[7])
        spheres_7 = dxt.DxtEntry_Sphere.from_mcnp(tokens[8])
        spheres_8 = dxt.DxtEntry_Sphere.from_mcnp(tokens[9])
        spheres_9 = dxt.DxtEntry_Sphere.from_mcnp(tokens[10])
        spheres_10 = dxt.DxtEntry_Sphere.from_mcnp(tokens[11])
        cutoff_1 = types.Real.from_mcnp(tokens[12])
        cutoff_2 = types.Real.from_mcnp(tokens[13])
        weight = types.Real.from_mcnp(tokens[14])

        return DataOption_Dxt(
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
            designator,
        )
