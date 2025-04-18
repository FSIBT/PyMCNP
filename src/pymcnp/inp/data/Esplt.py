import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Esplt(DataOption_, keyword='esplt'):
    """
    Represents INP esplt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'ratio_1': types.RealOrJump,
        'energy_1': types.RealOrJump,
        'ratio_2': types.RealOrJump,
        'energy_2': types.RealOrJump,
        'ratio_3': types.RealOrJump,
        'energy_3': types.RealOrJump,
        'ratio_4': types.RealOrJump,
        'energy_4': types.RealOrJump,
        'ratio_5': types.RealOrJump,
        'energy_5': types.RealOrJump,
        'ratio_6': types.RealOrJump,
        'energy_6': types.RealOrJump,
        'ratio_7': types.RealOrJump,
        'energy_7': types.RealOrJump,
        'ratio_8': types.RealOrJump,
        'energy_8': types.RealOrJump,
        'ratio_9': types.RealOrJump,
        'energy_9': types.RealOrJump,
        'ratio_10': types.RealOrJump,
        'energy_10': types.RealOrJump,
        'ratio_11': types.RealOrJump,
        'energy_11': types.RealOrJump,
        'ratio_12': types.RealOrJump,
        'energy_12': types.RealOrJump,
        'ratio_13': types.RealOrJump,
        'energy_13': types.RealOrJump,
        'ratio_14': types.RealOrJump,
        'energy_14': types.RealOrJump,
        'ratio_15': types.RealOrJump,
        'energy_15': types.RealOrJump,
        'ratio_16': types.RealOrJump,
        'energy_16': types.RealOrJump,
        'ratio_17': types.RealOrJump,
        'energy_17': types.RealOrJump,
        'ratio_18': types.RealOrJump,
        'energy_18': types.RealOrJump,
        'ratio_19': types.RealOrJump,
        'energy_19': types.RealOrJump,
        'ratio_20': types.RealOrJump,
        'energy_20': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Aesplt:(\S+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        designator: types.Designator,
        ratio_1: types.RealOrJump,
        energy_1: types.RealOrJump,
        ratio_2: types.RealOrJump,
        energy_2: types.RealOrJump,
        ratio_3: types.RealOrJump,
        energy_3: types.RealOrJump,
        ratio_4: types.RealOrJump,
        energy_4: types.RealOrJump,
        ratio_5: types.RealOrJump,
        energy_5: types.RealOrJump,
        ratio_6: types.RealOrJump,
        energy_6: types.RealOrJump,
        ratio_7: types.RealOrJump,
        energy_7: types.RealOrJump,
        ratio_8: types.RealOrJump,
        energy_8: types.RealOrJump,
        ratio_9: types.RealOrJump,
        energy_9: types.RealOrJump,
        ratio_10: types.RealOrJump,
        energy_10: types.RealOrJump,
        ratio_11: types.RealOrJump,
        energy_11: types.RealOrJump,
        ratio_12: types.RealOrJump,
        energy_12: types.RealOrJump,
        ratio_13: types.RealOrJump,
        energy_13: types.RealOrJump,
        ratio_14: types.RealOrJump,
        energy_14: types.RealOrJump,
        ratio_15: types.RealOrJump,
        energy_15: types.RealOrJump,
        ratio_16: types.RealOrJump,
        energy_16: types.RealOrJump,
        ratio_17: types.RealOrJump,
        energy_17: types.RealOrJump,
        ratio_18: types.RealOrJump,
        energy_18: types.RealOrJump,
        ratio_19: types.RealOrJump,
        energy_19: types.RealOrJump,
        ratio_20: types.RealOrJump,
        energy_20: types.RealOrJump,
    ):
        """
        Initializes ``Esplt``.

        Parameters:
            designator: Data card particle designator.
            ratio_1: Splitting/roulette ratio #1.
            energy_1: Splitting/roulette energy #1.
            ratio_2: Splitting/roulette ratio #2.
            energy_2: Splitting/roulette energy #2.
            ratio_3: Splitting/roulette ratio #3.
            energy_3: Splitting/roulette energy #3.
            ratio_4: Splitting/roulette ratio #4.
            energy_4: Splitting/roulette energy #4.
            ratio_5: Splitting/roulette ratio #5.
            energy_5: Splitting/roulette energy #5.
            ratio_6: Splitting/roulette ratio #6.
            energy_6: Splitting/roulette energy #6.
            ratio_7: Splitting/roulette ratio #7.
            energy_7: Splitting/roulette energy #7.
            ratio_8: Splitting/roulette ratio #8.
            energy_8: Splitting/roulette energy #8.
            ratio_9: Splitting/roulette ratio #9.
            energy_9: Splitting/roulette energy #9.
            ratio_10: Splitting/roulette ratio #10.
            energy_10: Splitting/roulette energy #10.
            ratio_11: Splitting/roulette ratio #11.
            energy_11: Splitting/roulette energy #11.
            ratio_12: Splitting/roulette ratio #12.
            energy_12: Splitting/roulette energy #12.
            ratio_13: Splitting/roulette ratio #13.
            energy_13: Splitting/roulette energy #13.
            ratio_14: Splitting/roulette ratio #14.
            energy_14: Splitting/roulette energy #14.
            ratio_15: Splitting/roulette ratio #15.
            energy_15: Splitting/roulette energy #15.
            ratio_16: Splitting/roulette ratio #16.
            energy_16: Splitting/roulette energy #16.
            ratio_17: Splitting/roulette ratio #17.
            energy_17: Splitting/roulette energy #17.
            ratio_18: Splitting/roulette ratio #18.
            energy_18: Splitting/roulette energy #18.
            ratio_19: Splitting/roulette ratio #19.
            energy_19: Splitting/roulette energy #19.
            ratio_20: Splitting/roulette ratio #20.
            energy_20: Splitting/roulette energy #20.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if ratio_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_1)
        if energy_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_1)
        if ratio_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_2)
        if energy_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_2)
        if ratio_3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_3)
        if energy_3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_3)
        if ratio_4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_4)
        if energy_4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_4)
        if ratio_5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_5)
        if energy_5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_5)
        if ratio_6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_6)
        if energy_6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_6)
        if ratio_7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_7)
        if energy_7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_7)
        if ratio_8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_8)
        if energy_8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_8)
        if ratio_9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_9)
        if energy_9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_9)
        if ratio_10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_10)
        if energy_10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_10)
        if ratio_11 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_11)
        if energy_11 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_11)
        if ratio_12 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_12)
        if energy_12 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_12)
        if ratio_13 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_13)
        if energy_13 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_13)
        if ratio_14 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_14)
        if energy_14 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_14)
        if ratio_15 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_15)
        if energy_15 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_15)
        if ratio_16 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_16)
        if energy_16 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_16)
        if ratio_17 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_17)
        if energy_17 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_17)
        if ratio_18 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_18)
        if energy_18 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_18)
        if ratio_19 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_19)
        if energy_19 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_19)
        if ratio_20 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_20)
        if energy_20 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_20)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ratio_1,
                energy_1,
                ratio_2,
                energy_2,
                ratio_3,
                energy_3,
                ratio_4,
                energy_4,
                ratio_5,
                energy_5,
                ratio_6,
                energy_6,
                ratio_7,
                energy_7,
                ratio_8,
                energy_8,
                ratio_9,
                energy_9,
                ratio_10,
                energy_10,
                ratio_11,
                energy_11,
                ratio_12,
                energy_12,
                ratio_13,
                energy_13,
                ratio_14,
                energy_14,
                ratio_15,
                energy_15,
                ratio_16,
                energy_16,
                ratio_17,
                energy_17,
                ratio_18,
                energy_18,
                ratio_19,
                energy_19,
                ratio_20,
                energy_20,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.ratio_1: typing.Final[types.RealOrJump] = ratio_1
        self.energy_1: typing.Final[types.RealOrJump] = energy_1
        self.ratio_2: typing.Final[types.RealOrJump] = ratio_2
        self.energy_2: typing.Final[types.RealOrJump] = energy_2
        self.ratio_3: typing.Final[types.RealOrJump] = ratio_3
        self.energy_3: typing.Final[types.RealOrJump] = energy_3
        self.ratio_4: typing.Final[types.RealOrJump] = ratio_4
        self.energy_4: typing.Final[types.RealOrJump] = energy_4
        self.ratio_5: typing.Final[types.RealOrJump] = ratio_5
        self.energy_5: typing.Final[types.RealOrJump] = energy_5
        self.ratio_6: typing.Final[types.RealOrJump] = ratio_6
        self.energy_6: typing.Final[types.RealOrJump] = energy_6
        self.ratio_7: typing.Final[types.RealOrJump] = ratio_7
        self.energy_7: typing.Final[types.RealOrJump] = energy_7
        self.ratio_8: typing.Final[types.RealOrJump] = ratio_8
        self.energy_8: typing.Final[types.RealOrJump] = energy_8
        self.ratio_9: typing.Final[types.RealOrJump] = ratio_9
        self.energy_9: typing.Final[types.RealOrJump] = energy_9
        self.ratio_10: typing.Final[types.RealOrJump] = ratio_10
        self.energy_10: typing.Final[types.RealOrJump] = energy_10
        self.ratio_11: typing.Final[types.RealOrJump] = ratio_11
        self.energy_11: typing.Final[types.RealOrJump] = energy_11
        self.ratio_12: typing.Final[types.RealOrJump] = ratio_12
        self.energy_12: typing.Final[types.RealOrJump] = energy_12
        self.ratio_13: typing.Final[types.RealOrJump] = ratio_13
        self.energy_13: typing.Final[types.RealOrJump] = energy_13
        self.ratio_14: typing.Final[types.RealOrJump] = ratio_14
        self.energy_14: typing.Final[types.RealOrJump] = energy_14
        self.ratio_15: typing.Final[types.RealOrJump] = ratio_15
        self.energy_15: typing.Final[types.RealOrJump] = energy_15
        self.ratio_16: typing.Final[types.RealOrJump] = ratio_16
        self.energy_16: typing.Final[types.RealOrJump] = energy_16
        self.ratio_17: typing.Final[types.RealOrJump] = ratio_17
        self.energy_17: typing.Final[types.RealOrJump] = energy_17
        self.ratio_18: typing.Final[types.RealOrJump] = ratio_18
        self.energy_18: typing.Final[types.RealOrJump] = energy_18
        self.ratio_19: typing.Final[types.RealOrJump] = ratio_19
        self.energy_19: typing.Final[types.RealOrJump] = energy_19
        self.ratio_20: typing.Final[types.RealOrJump] = ratio_20
        self.energy_20: typing.Final[types.RealOrJump] = energy_20
