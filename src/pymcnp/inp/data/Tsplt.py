import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Tsplt(DataOption_, keyword='tsplt'):
    """
    Represents INP tsplt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'ratio_1': types.RealOrJump,
        'time_1': types.RealOrJump,
        'ratio_2': types.RealOrJump,
        'time_2': types.RealOrJump,
        'ratio_3': types.RealOrJump,
        'time_3': types.RealOrJump,
        'ratio_4': types.RealOrJump,
        'time_4': types.RealOrJump,
        'ratio_5': types.RealOrJump,
        'time_5': types.RealOrJump,
        'ratio_6': types.RealOrJump,
        'time_6': types.RealOrJump,
        'ratio_7': types.RealOrJump,
        'time_7': types.RealOrJump,
        'ratio_8': types.RealOrJump,
        'time_8': types.RealOrJump,
        'ratio_9': types.RealOrJump,
        'time_9': types.RealOrJump,
        'ratio_10': types.RealOrJump,
        'time_10': types.RealOrJump,
        'ratio_11': types.RealOrJump,
        'time_11': types.RealOrJump,
        'ratio_12': types.RealOrJump,
        'time_12': types.RealOrJump,
        'ratio_13': types.RealOrJump,
        'time_13': types.RealOrJump,
        'ratio_14': types.RealOrJump,
        'time_14': types.RealOrJump,
        'ratio_15': types.RealOrJump,
        'time_15': types.RealOrJump,
        'ratio_16': types.RealOrJump,
        'time_16': types.RealOrJump,
        'ratio_17': types.RealOrJump,
        'time_17': types.RealOrJump,
        'ratio_18': types.RealOrJump,
        'time_18': types.RealOrJump,
        'ratio_19': types.RealOrJump,
        'time_19': types.RealOrJump,
        'ratio_20': types.RealOrJump,
        'time_20': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Atsplt:(\S+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        designator: types.Designator,
        ratio_1: types.RealOrJump,
        time_1: types.RealOrJump,
        ratio_2: types.RealOrJump,
        time_2: types.RealOrJump,
        ratio_3: types.RealOrJump,
        time_3: types.RealOrJump,
        ratio_4: types.RealOrJump,
        time_4: types.RealOrJump,
        ratio_5: types.RealOrJump,
        time_5: types.RealOrJump,
        ratio_6: types.RealOrJump,
        time_6: types.RealOrJump,
        ratio_7: types.RealOrJump,
        time_7: types.RealOrJump,
        ratio_8: types.RealOrJump,
        time_8: types.RealOrJump,
        ratio_9: types.RealOrJump,
        time_9: types.RealOrJump,
        ratio_10: types.RealOrJump,
        time_10: types.RealOrJump,
        ratio_11: types.RealOrJump,
        time_11: types.RealOrJump,
        ratio_12: types.RealOrJump,
        time_12: types.RealOrJump,
        ratio_13: types.RealOrJump,
        time_13: types.RealOrJump,
        ratio_14: types.RealOrJump,
        time_14: types.RealOrJump,
        ratio_15: types.RealOrJump,
        time_15: types.RealOrJump,
        ratio_16: types.RealOrJump,
        time_16: types.RealOrJump,
        ratio_17: types.RealOrJump,
        time_17: types.RealOrJump,
        ratio_18: types.RealOrJump,
        time_18: types.RealOrJump,
        ratio_19: types.RealOrJump,
        time_19: types.RealOrJump,
        ratio_20: types.RealOrJump,
        time_20: types.RealOrJump,
    ):
        """
        Initializes ``Tsplt``.

        Parameters:
            designator: Data card particle designator.
            ratio_1: Splitting/roulette ratio #1.
            time_1: Splitting/roulette time #1.
            ratio_2: Splitting/roulette ratio #2.
            time_2: Splitting/roulette time #2.
            ratio_3: Splitting/roulette ratio #3.
            time_3: Splitting/roulette time #3.
            ratio_4: Splitting/roulette ratio #4.
            time_4: Splitting/roulette time #4.
            ratio_5: Splitting/roulette ratio #5.
            time_5: Splitting/roulette time #5.
            ratio_6: Splitting/roulette ratio #6.
            time_6: Splitting/roulette time #6.
            ratio_7: Splitting/roulette ratio #7.
            time_7: Splitting/roulette time #7.
            ratio_8: Splitting/roulette ratio #8.
            time_8: Splitting/roulette time #8.
            ratio_9: Splitting/roulette ratio #9.
            time_9: Splitting/roulette time #9.
            ratio_10: Splitting/roulette ratio #10.
            time_10: Splitting/roulette time #10.
            ratio_11: Splitting/roulette ratio #11.
            time_11: Splitting/roulette time #11.
            ratio_12: Splitting/roulette ratio #12.
            time_12: Splitting/roulette time #12.
            ratio_13: Splitting/roulette ratio #13.
            time_13: Splitting/roulette time #13.
            ratio_14: Splitting/roulette ratio #14.
            time_14: Splitting/roulette time #14.
            ratio_15: Splitting/roulette ratio #15.
            time_15: Splitting/roulette time #15.
            ratio_16: Splitting/roulette ratio #16.
            time_16: Splitting/roulette time #16.
            ratio_17: Splitting/roulette ratio #17.
            time_17: Splitting/roulette time #17.
            ratio_18: Splitting/roulette ratio #18.
            time_18: Splitting/roulette time #18.
            ratio_19: Splitting/roulette ratio #19.
            time_19: Splitting/roulette time #19.
            ratio_20: Splitting/roulette ratio #20.
            time_20: Splitting/roulette time #20.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if ratio_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_1)
        if time_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_1)
        if ratio_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_2)
        if time_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_2)
        if ratio_3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_3)
        if time_3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_3)
        if ratio_4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_4)
        if time_4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_4)
        if ratio_5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_5)
        if time_5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_5)
        if ratio_6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_6)
        if time_6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_6)
        if ratio_7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_7)
        if time_7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_7)
        if ratio_8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_8)
        if time_8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_8)
        if ratio_9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_9)
        if time_9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_9)
        if ratio_10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_10)
        if time_10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_10)
        if ratio_11 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_11)
        if time_11 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_11)
        if ratio_12 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_12)
        if time_12 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_12)
        if ratio_13 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_13)
        if time_13 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_13)
        if ratio_14 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_14)
        if time_14 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_14)
        if ratio_15 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_15)
        if time_15 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_15)
        if ratio_16 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_16)
        if time_16 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_16)
        if ratio_17 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_17)
        if time_17 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_17)
        if ratio_18 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_18)
        if time_18 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_18)
        if ratio_19 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_19)
        if time_19 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_19)
        if ratio_20 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ratio_20)
        if time_20 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time_20)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ratio_1,
                time_1,
                ratio_2,
                time_2,
                ratio_3,
                time_3,
                ratio_4,
                time_4,
                ratio_5,
                time_5,
                ratio_6,
                time_6,
                ratio_7,
                time_7,
                ratio_8,
                time_8,
                ratio_9,
                time_9,
                ratio_10,
                time_10,
                ratio_11,
                time_11,
                ratio_12,
                time_12,
                ratio_13,
                time_13,
                ratio_14,
                time_14,
                ratio_15,
                time_15,
                ratio_16,
                time_16,
                ratio_17,
                time_17,
                ratio_18,
                time_18,
                ratio_19,
                time_19,
                ratio_20,
                time_20,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.ratio_1: typing.Final[types.RealOrJump] = ratio_1
        self.time_1: typing.Final[types.RealOrJump] = time_1
        self.ratio_2: typing.Final[types.RealOrJump] = ratio_2
        self.time_2: typing.Final[types.RealOrJump] = time_2
        self.ratio_3: typing.Final[types.RealOrJump] = ratio_3
        self.time_3: typing.Final[types.RealOrJump] = time_3
        self.ratio_4: typing.Final[types.RealOrJump] = ratio_4
        self.time_4: typing.Final[types.RealOrJump] = time_4
        self.ratio_5: typing.Final[types.RealOrJump] = ratio_5
        self.time_5: typing.Final[types.RealOrJump] = time_5
        self.ratio_6: typing.Final[types.RealOrJump] = ratio_6
        self.time_6: typing.Final[types.RealOrJump] = time_6
        self.ratio_7: typing.Final[types.RealOrJump] = ratio_7
        self.time_7: typing.Final[types.RealOrJump] = time_7
        self.ratio_8: typing.Final[types.RealOrJump] = ratio_8
        self.time_8: typing.Final[types.RealOrJump] = time_8
        self.ratio_9: typing.Final[types.RealOrJump] = ratio_9
        self.time_9: typing.Final[types.RealOrJump] = time_9
        self.ratio_10: typing.Final[types.RealOrJump] = ratio_10
        self.time_10: typing.Final[types.RealOrJump] = time_10
        self.ratio_11: typing.Final[types.RealOrJump] = ratio_11
        self.time_11: typing.Final[types.RealOrJump] = time_11
        self.ratio_12: typing.Final[types.RealOrJump] = ratio_12
        self.time_12: typing.Final[types.RealOrJump] = time_12
        self.ratio_13: typing.Final[types.RealOrJump] = ratio_13
        self.time_13: typing.Final[types.RealOrJump] = time_13
        self.ratio_14: typing.Final[types.RealOrJump] = ratio_14
        self.time_14: typing.Final[types.RealOrJump] = time_14
        self.ratio_15: typing.Final[types.RealOrJump] = ratio_15
        self.time_15: typing.Final[types.RealOrJump] = time_15
        self.ratio_16: typing.Final[types.RealOrJump] = ratio_16
        self.time_16: typing.Final[types.RealOrJump] = time_16
        self.ratio_17: typing.Final[types.RealOrJump] = ratio_17
        self.time_17: typing.Final[types.RealOrJump] = time_17
        self.ratio_18: typing.Final[types.RealOrJump] = ratio_18
        self.time_18: typing.Final[types.RealOrJump] = time_18
        self.ratio_19: typing.Final[types.RealOrJump] = ratio_19
        self.time_19: typing.Final[types.RealOrJump] = time_19
        self.ratio_20: typing.Final[types.RealOrJump] = ratio_20
        self.time_20: typing.Final[types.RealOrJump] = time_20
