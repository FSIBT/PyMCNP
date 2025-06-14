import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Tsplt(_option.DataOption):
    """
    Represents INP tsplt elements.

    Attributes:
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
    """

    _KEYWORD = 'tsplt'

    _ATTRS = {
        'designator': types.Designator,
        'ratio_1': types.Real,
        'time_1': types.Real,
        'ratio_2': types.Real,
        'time_2': types.Real,
        'ratio_3': types.Real,
        'time_3': types.Real,
        'ratio_4': types.Real,
        'time_4': types.Real,
        'ratio_5': types.Real,
        'time_5': types.Real,
        'ratio_6': types.Real,
        'time_6': types.Real,
        'ratio_7': types.Real,
        'time_7': types.Real,
        'ratio_8': types.Real,
        'time_8': types.Real,
        'ratio_9': types.Real,
        'time_9': types.Real,
        'ratio_10': types.Real,
        'time_10': types.Real,
        'ratio_11': types.Real,
        'time_11': types.Real,
        'ratio_12': types.Real,
        'time_12': types.Real,
        'ratio_13': types.Real,
        'time_13': types.Real,
        'ratio_14': types.Real,
        'time_14': types.Real,
        'ratio_15': types.Real,
        'time_15': types.Real,
        'ratio_16': types.Real,
        'time_16': types.Real,
        'ratio_17': types.Real,
        'time_17': types.Real,
        'ratio_18': types.Real,
        'time_18': types.Real,
        'ratio_19': types.Real,
        'time_19': types.Real,
        'ratio_20': types.Real,
        'time_20': types.Real,
    }

    _REGEX = re.compile(
        rf'\Atsplt:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        designator: types.Designator,
        ratio_1: types.Real = None,
        time_1: types.Real = None,
        ratio_2: types.Real = None,
        time_2: types.Real = None,
        ratio_3: types.Real = None,
        time_3: types.Real = None,
        ratio_4: types.Real = None,
        time_4: types.Real = None,
        ratio_5: types.Real = None,
        time_5: types.Real = None,
        ratio_6: types.Real = None,
        time_6: types.Real = None,
        ratio_7: types.Real = None,
        time_7: types.Real = None,
        ratio_8: types.Real = None,
        time_8: types.Real = None,
        ratio_9: types.Real = None,
        time_9: types.Real = None,
        ratio_10: types.Real = None,
        time_10: types.Real = None,
        ratio_11: types.Real = None,
        time_11: types.Real = None,
        ratio_12: types.Real = None,
        time_12: types.Real = None,
        ratio_13: types.Real = None,
        time_13: types.Real = None,
        ratio_14: types.Real = None,
        time_14: types.Real = None,
        ratio_15: types.Real = None,
        time_15: types.Real = None,
        ratio_16: types.Real = None,
        time_16: types.Real = None,
        ratio_17: types.Real = None,
        time_17: types.Real = None,
        ratio_18: types.Real = None,
        time_18: types.Real = None,
        ratio_19: types.Real = None,
        time_19: types.Real = None,
        ratio_20: types.Real = None,
        time_20: types.Real = None,
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
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)

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
        self.ratio_1: typing.Final[types.Real] = ratio_1
        self.time_1: typing.Final[types.Real] = time_1
        self.ratio_2: typing.Final[types.Real] = ratio_2
        self.time_2: typing.Final[types.Real] = time_2
        self.ratio_3: typing.Final[types.Real] = ratio_3
        self.time_3: typing.Final[types.Real] = time_3
        self.ratio_4: typing.Final[types.Real] = ratio_4
        self.time_4: typing.Final[types.Real] = time_4
        self.ratio_5: typing.Final[types.Real] = ratio_5
        self.time_5: typing.Final[types.Real] = time_5
        self.ratio_6: typing.Final[types.Real] = ratio_6
        self.time_6: typing.Final[types.Real] = time_6
        self.ratio_7: typing.Final[types.Real] = ratio_7
        self.time_7: typing.Final[types.Real] = time_7
        self.ratio_8: typing.Final[types.Real] = ratio_8
        self.time_8: typing.Final[types.Real] = time_8
        self.ratio_9: typing.Final[types.Real] = ratio_9
        self.time_9: typing.Final[types.Real] = time_9
        self.ratio_10: typing.Final[types.Real] = ratio_10
        self.time_10: typing.Final[types.Real] = time_10
        self.ratio_11: typing.Final[types.Real] = ratio_11
        self.time_11: typing.Final[types.Real] = time_11
        self.ratio_12: typing.Final[types.Real] = ratio_12
        self.time_12: typing.Final[types.Real] = time_12
        self.ratio_13: typing.Final[types.Real] = ratio_13
        self.time_13: typing.Final[types.Real] = time_13
        self.ratio_14: typing.Final[types.Real] = ratio_14
        self.time_14: typing.Final[types.Real] = time_14
        self.ratio_15: typing.Final[types.Real] = ratio_15
        self.time_15: typing.Final[types.Real] = time_15
        self.ratio_16: typing.Final[types.Real] = ratio_16
        self.time_16: typing.Final[types.Real] = time_16
        self.ratio_17: typing.Final[types.Real] = ratio_17
        self.time_17: typing.Final[types.Real] = time_17
        self.ratio_18: typing.Final[types.Real] = ratio_18
        self.time_18: typing.Final[types.Real] = time_18
        self.ratio_19: typing.Final[types.Real] = ratio_19
        self.time_19: typing.Final[types.Real] = time_19
        self.ratio_20: typing.Final[types.Real] = ratio_20
        self.time_20: typing.Final[types.Real] = time_20


@dataclasses.dataclass
class TspltBuilder(_option.DataOptionBuilder):
    """
    Builds ``Tsplt``.

    Attributes:
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
    """

    designator: str | types.Designator
    ratio_1: str | float | types.Real = None
    time_1: str | float | types.Real = None
    ratio_2: str | float | types.Real = None
    time_2: str | float | types.Real = None
    ratio_3: str | float | types.Real = None
    time_3: str | float | types.Real = None
    ratio_4: str | float | types.Real = None
    time_4: str | float | types.Real = None
    ratio_5: str | float | types.Real = None
    time_5: str | float | types.Real = None
    ratio_6: str | float | types.Real = None
    time_6: str | float | types.Real = None
    ratio_7: str | float | types.Real = None
    time_7: str | float | types.Real = None
    ratio_8: str | float | types.Real = None
    time_8: str | float | types.Real = None
    ratio_9: str | float | types.Real = None
    time_9: str | float | types.Real = None
    ratio_10: str | float | types.Real = None
    time_10: str | float | types.Real = None
    ratio_11: str | float | types.Real = None
    time_11: str | float | types.Real = None
    ratio_12: str | float | types.Real = None
    time_12: str | float | types.Real = None
    ratio_13: str | float | types.Real = None
    time_13: str | float | types.Real = None
    ratio_14: str | float | types.Real = None
    time_14: str | float | types.Real = None
    ratio_15: str | float | types.Real = None
    time_15: str | float | types.Real = None
    ratio_16: str | float | types.Real = None
    time_16: str | float | types.Real = None
    ratio_17: str | float | types.Real = None
    time_17: str | float | types.Real = None
    ratio_18: str | float | types.Real = None
    time_18: str | float | types.Real = None
    ratio_19: str | float | types.Real = None
    time_19: str | float | types.Real = None
    ratio_20: str | float | types.Real = None
    time_20: str | float | types.Real = None

    def build(self):
        """
        Builds ``TspltBuilder`` into ``Tsplt``.

        Returns:
            ``Tsplt`` for ``TspltBuilder``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        ratio_1 = self.ratio_1
        if isinstance(self.ratio_1, types.Real):
            ratio_1 = self.ratio_1
        elif isinstance(self.ratio_1, float) or isinstance(self.ratio_1, int):
            ratio_1 = types.Real(self.ratio_1)
        elif isinstance(self.ratio_1, str):
            ratio_1 = types.Real.from_mcnp(self.ratio_1)

        time_1 = self.time_1
        if isinstance(self.time_1, types.Real):
            time_1 = self.time_1
        elif isinstance(self.time_1, float) or isinstance(self.time_1, int):
            time_1 = types.Real(self.time_1)
        elif isinstance(self.time_1, str):
            time_1 = types.Real.from_mcnp(self.time_1)

        ratio_2 = self.ratio_2
        if isinstance(self.ratio_2, types.Real):
            ratio_2 = self.ratio_2
        elif isinstance(self.ratio_2, float) or isinstance(self.ratio_2, int):
            ratio_2 = types.Real(self.ratio_2)
        elif isinstance(self.ratio_2, str):
            ratio_2 = types.Real.from_mcnp(self.ratio_2)

        time_2 = self.time_2
        if isinstance(self.time_2, types.Real):
            time_2 = self.time_2
        elif isinstance(self.time_2, float) or isinstance(self.time_2, int):
            time_2 = types.Real(self.time_2)
        elif isinstance(self.time_2, str):
            time_2 = types.Real.from_mcnp(self.time_2)

        ratio_3 = self.ratio_3
        if isinstance(self.ratio_3, types.Real):
            ratio_3 = self.ratio_3
        elif isinstance(self.ratio_3, float) or isinstance(self.ratio_3, int):
            ratio_3 = types.Real(self.ratio_3)
        elif isinstance(self.ratio_3, str):
            ratio_3 = types.Real.from_mcnp(self.ratio_3)

        time_3 = self.time_3
        if isinstance(self.time_3, types.Real):
            time_3 = self.time_3
        elif isinstance(self.time_3, float) or isinstance(self.time_3, int):
            time_3 = types.Real(self.time_3)
        elif isinstance(self.time_3, str):
            time_3 = types.Real.from_mcnp(self.time_3)

        ratio_4 = self.ratio_4
        if isinstance(self.ratio_4, types.Real):
            ratio_4 = self.ratio_4
        elif isinstance(self.ratio_4, float) or isinstance(self.ratio_4, int):
            ratio_4 = types.Real(self.ratio_4)
        elif isinstance(self.ratio_4, str):
            ratio_4 = types.Real.from_mcnp(self.ratio_4)

        time_4 = self.time_4
        if isinstance(self.time_4, types.Real):
            time_4 = self.time_4
        elif isinstance(self.time_4, float) or isinstance(self.time_4, int):
            time_4 = types.Real(self.time_4)
        elif isinstance(self.time_4, str):
            time_4 = types.Real.from_mcnp(self.time_4)

        ratio_5 = self.ratio_5
        if isinstance(self.ratio_5, types.Real):
            ratio_5 = self.ratio_5
        elif isinstance(self.ratio_5, float) or isinstance(self.ratio_5, int):
            ratio_5 = types.Real(self.ratio_5)
        elif isinstance(self.ratio_5, str):
            ratio_5 = types.Real.from_mcnp(self.ratio_5)

        time_5 = self.time_5
        if isinstance(self.time_5, types.Real):
            time_5 = self.time_5
        elif isinstance(self.time_5, float) or isinstance(self.time_5, int):
            time_5 = types.Real(self.time_5)
        elif isinstance(self.time_5, str):
            time_5 = types.Real.from_mcnp(self.time_5)

        ratio_6 = self.ratio_6
        if isinstance(self.ratio_6, types.Real):
            ratio_6 = self.ratio_6
        elif isinstance(self.ratio_6, float) or isinstance(self.ratio_6, int):
            ratio_6 = types.Real(self.ratio_6)
        elif isinstance(self.ratio_6, str):
            ratio_6 = types.Real.from_mcnp(self.ratio_6)

        time_6 = self.time_6
        if isinstance(self.time_6, types.Real):
            time_6 = self.time_6
        elif isinstance(self.time_6, float) or isinstance(self.time_6, int):
            time_6 = types.Real(self.time_6)
        elif isinstance(self.time_6, str):
            time_6 = types.Real.from_mcnp(self.time_6)

        ratio_7 = self.ratio_7
        if isinstance(self.ratio_7, types.Real):
            ratio_7 = self.ratio_7
        elif isinstance(self.ratio_7, float) or isinstance(self.ratio_7, int):
            ratio_7 = types.Real(self.ratio_7)
        elif isinstance(self.ratio_7, str):
            ratio_7 = types.Real.from_mcnp(self.ratio_7)

        time_7 = self.time_7
        if isinstance(self.time_7, types.Real):
            time_7 = self.time_7
        elif isinstance(self.time_7, float) or isinstance(self.time_7, int):
            time_7 = types.Real(self.time_7)
        elif isinstance(self.time_7, str):
            time_7 = types.Real.from_mcnp(self.time_7)

        ratio_8 = self.ratio_8
        if isinstance(self.ratio_8, types.Real):
            ratio_8 = self.ratio_8
        elif isinstance(self.ratio_8, float) or isinstance(self.ratio_8, int):
            ratio_8 = types.Real(self.ratio_8)
        elif isinstance(self.ratio_8, str):
            ratio_8 = types.Real.from_mcnp(self.ratio_8)

        time_8 = self.time_8
        if isinstance(self.time_8, types.Real):
            time_8 = self.time_8
        elif isinstance(self.time_8, float) or isinstance(self.time_8, int):
            time_8 = types.Real(self.time_8)
        elif isinstance(self.time_8, str):
            time_8 = types.Real.from_mcnp(self.time_8)

        ratio_9 = self.ratio_9
        if isinstance(self.ratio_9, types.Real):
            ratio_9 = self.ratio_9
        elif isinstance(self.ratio_9, float) or isinstance(self.ratio_9, int):
            ratio_9 = types.Real(self.ratio_9)
        elif isinstance(self.ratio_9, str):
            ratio_9 = types.Real.from_mcnp(self.ratio_9)

        time_9 = self.time_9
        if isinstance(self.time_9, types.Real):
            time_9 = self.time_9
        elif isinstance(self.time_9, float) or isinstance(self.time_9, int):
            time_9 = types.Real(self.time_9)
        elif isinstance(self.time_9, str):
            time_9 = types.Real.from_mcnp(self.time_9)

        ratio_10 = self.ratio_10
        if isinstance(self.ratio_10, types.Real):
            ratio_10 = self.ratio_10
        elif isinstance(self.ratio_10, float) or isinstance(self.ratio_10, int):
            ratio_10 = types.Real(self.ratio_10)
        elif isinstance(self.ratio_10, str):
            ratio_10 = types.Real.from_mcnp(self.ratio_10)

        time_10 = self.time_10
        if isinstance(self.time_10, types.Real):
            time_10 = self.time_10
        elif isinstance(self.time_10, float) or isinstance(self.time_10, int):
            time_10 = types.Real(self.time_10)
        elif isinstance(self.time_10, str):
            time_10 = types.Real.from_mcnp(self.time_10)

        ratio_11 = self.ratio_11
        if isinstance(self.ratio_11, types.Real):
            ratio_11 = self.ratio_11
        elif isinstance(self.ratio_11, float) or isinstance(self.ratio_11, int):
            ratio_11 = types.Real(self.ratio_11)
        elif isinstance(self.ratio_11, str):
            ratio_11 = types.Real.from_mcnp(self.ratio_11)

        time_11 = self.time_11
        if isinstance(self.time_11, types.Real):
            time_11 = self.time_11
        elif isinstance(self.time_11, float) or isinstance(self.time_11, int):
            time_11 = types.Real(self.time_11)
        elif isinstance(self.time_11, str):
            time_11 = types.Real.from_mcnp(self.time_11)

        ratio_12 = self.ratio_12
        if isinstance(self.ratio_12, types.Real):
            ratio_12 = self.ratio_12
        elif isinstance(self.ratio_12, float) or isinstance(self.ratio_12, int):
            ratio_12 = types.Real(self.ratio_12)
        elif isinstance(self.ratio_12, str):
            ratio_12 = types.Real.from_mcnp(self.ratio_12)

        time_12 = self.time_12
        if isinstance(self.time_12, types.Real):
            time_12 = self.time_12
        elif isinstance(self.time_12, float) or isinstance(self.time_12, int):
            time_12 = types.Real(self.time_12)
        elif isinstance(self.time_12, str):
            time_12 = types.Real.from_mcnp(self.time_12)

        ratio_13 = self.ratio_13
        if isinstance(self.ratio_13, types.Real):
            ratio_13 = self.ratio_13
        elif isinstance(self.ratio_13, float) or isinstance(self.ratio_13, int):
            ratio_13 = types.Real(self.ratio_13)
        elif isinstance(self.ratio_13, str):
            ratio_13 = types.Real.from_mcnp(self.ratio_13)

        time_13 = self.time_13
        if isinstance(self.time_13, types.Real):
            time_13 = self.time_13
        elif isinstance(self.time_13, float) or isinstance(self.time_13, int):
            time_13 = types.Real(self.time_13)
        elif isinstance(self.time_13, str):
            time_13 = types.Real.from_mcnp(self.time_13)

        ratio_14 = self.ratio_14
        if isinstance(self.ratio_14, types.Real):
            ratio_14 = self.ratio_14
        elif isinstance(self.ratio_14, float) or isinstance(self.ratio_14, int):
            ratio_14 = types.Real(self.ratio_14)
        elif isinstance(self.ratio_14, str):
            ratio_14 = types.Real.from_mcnp(self.ratio_14)

        time_14 = self.time_14
        if isinstance(self.time_14, types.Real):
            time_14 = self.time_14
        elif isinstance(self.time_14, float) or isinstance(self.time_14, int):
            time_14 = types.Real(self.time_14)
        elif isinstance(self.time_14, str):
            time_14 = types.Real.from_mcnp(self.time_14)

        ratio_15 = self.ratio_15
        if isinstance(self.ratio_15, types.Real):
            ratio_15 = self.ratio_15
        elif isinstance(self.ratio_15, float) or isinstance(self.ratio_15, int):
            ratio_15 = types.Real(self.ratio_15)
        elif isinstance(self.ratio_15, str):
            ratio_15 = types.Real.from_mcnp(self.ratio_15)

        time_15 = self.time_15
        if isinstance(self.time_15, types.Real):
            time_15 = self.time_15
        elif isinstance(self.time_15, float) or isinstance(self.time_15, int):
            time_15 = types.Real(self.time_15)
        elif isinstance(self.time_15, str):
            time_15 = types.Real.from_mcnp(self.time_15)

        ratio_16 = self.ratio_16
        if isinstance(self.ratio_16, types.Real):
            ratio_16 = self.ratio_16
        elif isinstance(self.ratio_16, float) or isinstance(self.ratio_16, int):
            ratio_16 = types.Real(self.ratio_16)
        elif isinstance(self.ratio_16, str):
            ratio_16 = types.Real.from_mcnp(self.ratio_16)

        time_16 = self.time_16
        if isinstance(self.time_16, types.Real):
            time_16 = self.time_16
        elif isinstance(self.time_16, float) or isinstance(self.time_16, int):
            time_16 = types.Real(self.time_16)
        elif isinstance(self.time_16, str):
            time_16 = types.Real.from_mcnp(self.time_16)

        ratio_17 = self.ratio_17
        if isinstance(self.ratio_17, types.Real):
            ratio_17 = self.ratio_17
        elif isinstance(self.ratio_17, float) or isinstance(self.ratio_17, int):
            ratio_17 = types.Real(self.ratio_17)
        elif isinstance(self.ratio_17, str):
            ratio_17 = types.Real.from_mcnp(self.ratio_17)

        time_17 = self.time_17
        if isinstance(self.time_17, types.Real):
            time_17 = self.time_17
        elif isinstance(self.time_17, float) or isinstance(self.time_17, int):
            time_17 = types.Real(self.time_17)
        elif isinstance(self.time_17, str):
            time_17 = types.Real.from_mcnp(self.time_17)

        ratio_18 = self.ratio_18
        if isinstance(self.ratio_18, types.Real):
            ratio_18 = self.ratio_18
        elif isinstance(self.ratio_18, float) or isinstance(self.ratio_18, int):
            ratio_18 = types.Real(self.ratio_18)
        elif isinstance(self.ratio_18, str):
            ratio_18 = types.Real.from_mcnp(self.ratio_18)

        time_18 = self.time_18
        if isinstance(self.time_18, types.Real):
            time_18 = self.time_18
        elif isinstance(self.time_18, float) or isinstance(self.time_18, int):
            time_18 = types.Real(self.time_18)
        elif isinstance(self.time_18, str):
            time_18 = types.Real.from_mcnp(self.time_18)

        ratio_19 = self.ratio_19
        if isinstance(self.ratio_19, types.Real):
            ratio_19 = self.ratio_19
        elif isinstance(self.ratio_19, float) or isinstance(self.ratio_19, int):
            ratio_19 = types.Real(self.ratio_19)
        elif isinstance(self.ratio_19, str):
            ratio_19 = types.Real.from_mcnp(self.ratio_19)

        time_19 = self.time_19
        if isinstance(self.time_19, types.Real):
            time_19 = self.time_19
        elif isinstance(self.time_19, float) or isinstance(self.time_19, int):
            time_19 = types.Real(self.time_19)
        elif isinstance(self.time_19, str):
            time_19 = types.Real.from_mcnp(self.time_19)

        ratio_20 = self.ratio_20
        if isinstance(self.ratio_20, types.Real):
            ratio_20 = self.ratio_20
        elif isinstance(self.ratio_20, float) or isinstance(self.ratio_20, int):
            ratio_20 = types.Real(self.ratio_20)
        elif isinstance(self.ratio_20, str):
            ratio_20 = types.Real.from_mcnp(self.ratio_20)

        time_20 = self.time_20
        if isinstance(self.time_20, types.Real):
            time_20 = self.time_20
        elif isinstance(self.time_20, float) or isinstance(self.time_20, int):
            time_20 = types.Real(self.time_20)
        elif isinstance(self.time_20, str):
            time_20 = types.Real.from_mcnp(self.time_20)

        return Tsplt(
            designator=designator,
            ratio_1=ratio_1,
            time_1=time_1,
            ratio_2=ratio_2,
            time_2=time_2,
            ratio_3=ratio_3,
            time_3=time_3,
            ratio_4=ratio_4,
            time_4=time_4,
            ratio_5=ratio_5,
            time_5=time_5,
            ratio_6=ratio_6,
            time_6=time_6,
            ratio_7=ratio_7,
            time_7=time_7,
            ratio_8=ratio_8,
            time_8=time_8,
            ratio_9=ratio_9,
            time_9=time_9,
            ratio_10=ratio_10,
            time_10=time_10,
            ratio_11=ratio_11,
            time_11=time_11,
            ratio_12=ratio_12,
            time_12=time_12,
            ratio_13=ratio_13,
            time_13=time_13,
            ratio_14=ratio_14,
            time_14=time_14,
            ratio_15=ratio_15,
            time_15=time_15,
            ratio_16=ratio_16,
            time_16=time_16,
            ratio_17=ratio_17,
            time_17=time_17,
            ratio_18=ratio_18,
            time_18=time_18,
            ratio_19=ratio_19,
            time_19=time_19,
            ratio_20=ratio_20,
            time_20=time_20,
        )

    @staticmethod
    def unbuild(ast: Tsplt):
        """
        Unbuilds ``Tsplt`` into ``TspltBuilder``

        Returns:
            ``TspltBuilder`` for ``Tsplt``.
        """

        return TspltBuilder(
            designator=copy.deepcopy(ast.designator),
            ratio_1=copy.deepcopy(ast.ratio_1),
            time_1=copy.deepcopy(ast.time_1),
            ratio_2=copy.deepcopy(ast.ratio_2),
            time_2=copy.deepcopy(ast.time_2),
            ratio_3=copy.deepcopy(ast.ratio_3),
            time_3=copy.deepcopy(ast.time_3),
            ratio_4=copy.deepcopy(ast.ratio_4),
            time_4=copy.deepcopy(ast.time_4),
            ratio_5=copy.deepcopy(ast.ratio_5),
            time_5=copy.deepcopy(ast.time_5),
            ratio_6=copy.deepcopy(ast.ratio_6),
            time_6=copy.deepcopy(ast.time_6),
            ratio_7=copy.deepcopy(ast.ratio_7),
            time_7=copy.deepcopy(ast.time_7),
            ratio_8=copy.deepcopy(ast.ratio_8),
            time_8=copy.deepcopy(ast.time_8),
            ratio_9=copy.deepcopy(ast.ratio_9),
            time_9=copy.deepcopy(ast.time_9),
            ratio_10=copy.deepcopy(ast.ratio_10),
            time_10=copy.deepcopy(ast.time_10),
            ratio_11=copy.deepcopy(ast.ratio_11),
            time_11=copy.deepcopy(ast.time_11),
            ratio_12=copy.deepcopy(ast.ratio_12),
            time_12=copy.deepcopy(ast.time_12),
            ratio_13=copy.deepcopy(ast.ratio_13),
            time_13=copy.deepcopy(ast.time_13),
            ratio_14=copy.deepcopy(ast.ratio_14),
            time_14=copy.deepcopy(ast.time_14),
            ratio_15=copy.deepcopy(ast.ratio_15),
            time_15=copy.deepcopy(ast.time_15),
            ratio_16=copy.deepcopy(ast.ratio_16),
            time_16=copy.deepcopy(ast.time_16),
            ratio_17=copy.deepcopy(ast.ratio_17),
            time_17=copy.deepcopy(ast.time_17),
            ratio_18=copy.deepcopy(ast.ratio_18),
            time_18=copy.deepcopy(ast.time_18),
            ratio_19=copy.deepcopy(ast.ratio_19),
            time_19=copy.deepcopy(ast.time_19),
            ratio_20=copy.deepcopy(ast.ratio_20),
            time_20=copy.deepcopy(ast.time_20),
        )
