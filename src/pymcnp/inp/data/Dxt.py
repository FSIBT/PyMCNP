import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Dxt(DataOption):
    """
    Represents INP dxt elements.

    Attributes:
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
    """

    _KEYWORD = 'dxt'

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
        rf'\Adxt:(\S+)( {types.Shell._REGEX.pattern[2:-2]})( {types.Shell._REGEX.pattern[2:-2]})( {types.Shell._REGEX.pattern[2:-2]})( {types.Shell._REGEX.pattern[2:-2]})( {types.Shell._REGEX.pattern[2:-2]})( {types.Shell._REGEX.pattern[2:-2]})( {types.Shell._REGEX.pattern[2:-2]})( {types.Shell._REGEX.pattern[2:-2]})( {types.Shell._REGEX.pattern[2:-2]})( {types.Shell._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z'
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
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if spheres_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, spheres_1)
        if spheres_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, spheres_2)
        if spheres_3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, spheres_3)
        if spheres_4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, spheres_4)
        if spheres_5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, spheres_5)
        if spheres_6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, spheres_6)
        if spheres_7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, spheres_7)
        if spheres_8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, spheres_8)
        if spheres_9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, spheres_9)
        if spheres_10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, spheres_10)
        if cutoff_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoff_1)
        if cutoff_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoff_2)
        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, weight)

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


@dataclasses.dataclass
class DxtBuilder:
    """
    Builds ``Dxt``.

    Attributes:
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
    """

    designator: str | types.Designator
    spheres_1: str | types.Shell
    spheres_2: str | types.Shell
    spheres_3: str | types.Shell
    spheres_4: str | types.Shell
    spheres_5: str | types.Shell
    spheres_6: str | types.Shell
    spheres_7: str | types.Shell
    spheres_8: str | types.Shell
    spheres_9: str | types.Shell
    spheres_10: str | types.Shell
    cutoff_1: str | float | types.Real
    cutoff_2: str | float | types.Real
    weight: str | float | types.Real

    def build(self):
        """
        Builds ``DxtBuilder`` into ``Dxt``.

        Returns:
            ``Dxt`` for ``DxtBuilder``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        spheres_1 = self.spheres_1
        if isinstance(self.spheres_1, types.Shell):
            spheres_1 = self.spheres_1
        elif isinstance(self.spheres_1, str):
            spheres_1 = types.Shell.from_mcnp(self.spheres_1)

        spheres_2 = self.spheres_2
        if isinstance(self.spheres_2, types.Shell):
            spheres_2 = self.spheres_2
        elif isinstance(self.spheres_2, str):
            spheres_2 = types.Shell.from_mcnp(self.spheres_2)

        spheres_3 = self.spheres_3
        if isinstance(self.spheres_3, types.Shell):
            spheres_3 = self.spheres_3
        elif isinstance(self.spheres_3, str):
            spheres_3 = types.Shell.from_mcnp(self.spheres_3)

        spheres_4 = self.spheres_4
        if isinstance(self.spheres_4, types.Shell):
            spheres_4 = self.spheres_4
        elif isinstance(self.spheres_4, str):
            spheres_4 = types.Shell.from_mcnp(self.spheres_4)

        spheres_5 = self.spheres_5
        if isinstance(self.spheres_5, types.Shell):
            spheres_5 = self.spheres_5
        elif isinstance(self.spheres_5, str):
            spheres_5 = types.Shell.from_mcnp(self.spheres_5)

        spheres_6 = self.spheres_6
        if isinstance(self.spheres_6, types.Shell):
            spheres_6 = self.spheres_6
        elif isinstance(self.spheres_6, str):
            spheres_6 = types.Shell.from_mcnp(self.spheres_6)

        spheres_7 = self.spheres_7
        if isinstance(self.spheres_7, types.Shell):
            spheres_7 = self.spheres_7
        elif isinstance(self.spheres_7, str):
            spheres_7 = types.Shell.from_mcnp(self.spheres_7)

        spheres_8 = self.spheres_8
        if isinstance(self.spheres_8, types.Shell):
            spheres_8 = self.spheres_8
        elif isinstance(self.spheres_8, str):
            spheres_8 = types.Shell.from_mcnp(self.spheres_8)

        spheres_9 = self.spheres_9
        if isinstance(self.spheres_9, types.Shell):
            spheres_9 = self.spheres_9
        elif isinstance(self.spheres_9, str):
            spheres_9 = types.Shell.from_mcnp(self.spheres_9)

        spheres_10 = self.spheres_10
        if isinstance(self.spheres_10, types.Shell):
            spheres_10 = self.spheres_10
        elif isinstance(self.spheres_10, str):
            spheres_10 = types.Shell.from_mcnp(self.spheres_10)

        cutoff_1 = self.cutoff_1
        if isinstance(self.cutoff_1, types.Real):
            cutoff_1 = self.cutoff_1
        elif isinstance(self.cutoff_1, float) or isinstance(self.cutoff_1, int):
            cutoff_1 = types.Real(self.cutoff_1)
        elif isinstance(self.cutoff_1, str):
            cutoff_1 = types.Real.from_mcnp(self.cutoff_1)

        cutoff_2 = self.cutoff_2
        if isinstance(self.cutoff_2, types.Real):
            cutoff_2 = self.cutoff_2
        elif isinstance(self.cutoff_2, float) or isinstance(self.cutoff_2, int):
            cutoff_2 = types.Real(self.cutoff_2)
        elif isinstance(self.cutoff_2, str):
            cutoff_2 = types.Real.from_mcnp(self.cutoff_2)

        weight = self.weight
        if isinstance(self.weight, types.Real):
            weight = self.weight
        elif isinstance(self.weight, float) or isinstance(self.weight, int):
            weight = types.Real(self.weight)
        elif isinstance(self.weight, str):
            weight = types.Real.from_mcnp(self.weight)

        return Dxt(
            designator=designator,
            spheres_1=spheres_1,
            spheres_2=spheres_2,
            spheres_3=spheres_3,
            spheres_4=spheres_4,
            spheres_5=spheres_5,
            spheres_6=spheres_6,
            spheres_7=spheres_7,
            spheres_8=spheres_8,
            spheres_9=spheres_9,
            spheres_10=spheres_10,
            cutoff_1=cutoff_1,
            cutoff_2=cutoff_2,
            weight=weight,
        )

    @staticmethod
    def unbuild(ast: Dxt):
        """
        Unbuilds ``Dxt`` into ``DxtBuilder``

        Returns:
            ``DxtBuilder`` for ``Dxt``.
        """

        return Dxt(
            designator=copy.deepcopy(ast.designator),
            spheres_1=copy.deepcopy(ast.spheres_1),
            spheres_2=copy.deepcopy(ast.spheres_2),
            spheres_3=copy.deepcopy(ast.spheres_3),
            spheres_4=copy.deepcopy(ast.spheres_4),
            spheres_5=copy.deepcopy(ast.spheres_5),
            spheres_6=copy.deepcopy(ast.spheres_6),
            spheres_7=copy.deepcopy(ast.spheres_7),
            spheres_8=copy.deepcopy(ast.spheres_8),
            spheres_9=copy.deepcopy(ast.spheres_9),
            spheres_10=copy.deepcopy(ast.spheres_10),
            cutoff_1=copy.deepcopy(ast.cutoff_1),
            cutoff_2=copy.deepcopy(ast.cutoff_2),
            weight=copy.deepcopy(ast.weight),
        )
