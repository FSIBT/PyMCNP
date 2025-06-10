import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Esplt(_option.DataOption):
    """
    Represents INP esplt elements.

    Attributes:
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
    """

    _KEYWORD = 'esplt'

    _ATTRS = {
        'designator': types.Designator,
        'ratio_1': types.Real,
        'energy_1': types.Real,
        'ratio_2': types.Real,
        'energy_2': types.Real,
        'ratio_3': types.Real,
        'energy_3': types.Real,
        'ratio_4': types.Real,
        'energy_4': types.Real,
        'ratio_5': types.Real,
        'energy_5': types.Real,
        'ratio_6': types.Real,
        'energy_6': types.Real,
        'ratio_7': types.Real,
        'energy_7': types.Real,
        'ratio_8': types.Real,
        'energy_8': types.Real,
        'ratio_9': types.Real,
        'energy_9': types.Real,
        'ratio_10': types.Real,
        'energy_10': types.Real,
        'ratio_11': types.Real,
        'energy_11': types.Real,
        'ratio_12': types.Real,
        'energy_12': types.Real,
        'ratio_13': types.Real,
        'energy_13': types.Real,
        'ratio_14': types.Real,
        'energy_14': types.Real,
        'ratio_15': types.Real,
        'energy_15': types.Real,
        'ratio_16': types.Real,
        'energy_16': types.Real,
        'ratio_17': types.Real,
        'energy_17': types.Real,
        'ratio_18': types.Real,
        'energy_18': types.Real,
        'ratio_19': types.Real,
        'energy_19': types.Real,
        'ratio_20': types.Real,
        'energy_20': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aesplt:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        designator: types.Designator,
        ratio_1: types.Real = None,
        energy_1: types.Real = None,
        ratio_2: types.Real = None,
        energy_2: types.Real = None,
        ratio_3: types.Real = None,
        energy_3: types.Real = None,
        ratio_4: types.Real = None,
        energy_4: types.Real = None,
        ratio_5: types.Real = None,
        energy_5: types.Real = None,
        ratio_6: types.Real = None,
        energy_6: types.Real = None,
        ratio_7: types.Real = None,
        energy_7: types.Real = None,
        ratio_8: types.Real = None,
        energy_8: types.Real = None,
        ratio_9: types.Real = None,
        energy_9: types.Real = None,
        ratio_10: types.Real = None,
        energy_10: types.Real = None,
        ratio_11: types.Real = None,
        energy_11: types.Real = None,
        ratio_12: types.Real = None,
        energy_12: types.Real = None,
        ratio_13: types.Real = None,
        energy_13: types.Real = None,
        ratio_14: types.Real = None,
        energy_14: types.Real = None,
        ratio_15: types.Real = None,
        energy_15: types.Real = None,
        ratio_16: types.Real = None,
        energy_16: types.Real = None,
        ratio_17: types.Real = None,
        energy_17: types.Real = None,
        ratio_18: types.Real = None,
        energy_18: types.Real = None,
        ratio_19: types.Real = None,
        energy_19: types.Real = None,
        ratio_20: types.Real = None,
        energy_20: types.Real = None,
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
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)

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
        self.ratio_1: typing.Final[types.Real] = ratio_1
        self.energy_1: typing.Final[types.Real] = energy_1
        self.ratio_2: typing.Final[types.Real] = ratio_2
        self.energy_2: typing.Final[types.Real] = energy_2
        self.ratio_3: typing.Final[types.Real] = ratio_3
        self.energy_3: typing.Final[types.Real] = energy_3
        self.ratio_4: typing.Final[types.Real] = ratio_4
        self.energy_4: typing.Final[types.Real] = energy_4
        self.ratio_5: typing.Final[types.Real] = ratio_5
        self.energy_5: typing.Final[types.Real] = energy_5
        self.ratio_6: typing.Final[types.Real] = ratio_6
        self.energy_6: typing.Final[types.Real] = energy_6
        self.ratio_7: typing.Final[types.Real] = ratio_7
        self.energy_7: typing.Final[types.Real] = energy_7
        self.ratio_8: typing.Final[types.Real] = ratio_8
        self.energy_8: typing.Final[types.Real] = energy_8
        self.ratio_9: typing.Final[types.Real] = ratio_9
        self.energy_9: typing.Final[types.Real] = energy_9
        self.ratio_10: typing.Final[types.Real] = ratio_10
        self.energy_10: typing.Final[types.Real] = energy_10
        self.ratio_11: typing.Final[types.Real] = ratio_11
        self.energy_11: typing.Final[types.Real] = energy_11
        self.ratio_12: typing.Final[types.Real] = ratio_12
        self.energy_12: typing.Final[types.Real] = energy_12
        self.ratio_13: typing.Final[types.Real] = ratio_13
        self.energy_13: typing.Final[types.Real] = energy_13
        self.ratio_14: typing.Final[types.Real] = ratio_14
        self.energy_14: typing.Final[types.Real] = energy_14
        self.ratio_15: typing.Final[types.Real] = ratio_15
        self.energy_15: typing.Final[types.Real] = energy_15
        self.ratio_16: typing.Final[types.Real] = ratio_16
        self.energy_16: typing.Final[types.Real] = energy_16
        self.ratio_17: typing.Final[types.Real] = ratio_17
        self.energy_17: typing.Final[types.Real] = energy_17
        self.ratio_18: typing.Final[types.Real] = ratio_18
        self.energy_18: typing.Final[types.Real] = energy_18
        self.ratio_19: typing.Final[types.Real] = ratio_19
        self.energy_19: typing.Final[types.Real] = energy_19
        self.ratio_20: typing.Final[types.Real] = ratio_20
        self.energy_20: typing.Final[types.Real] = energy_20


@dataclasses.dataclass
class EspltBuilder(_option.DataOptionBuilder):
    """
    Builds ``Esplt``.

    Attributes:
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
    """

    designator: str | types.Designator
    ratio_1: str | float | types.Real = None
    energy_1: str | float | types.Real = None
    ratio_2: str | float | types.Real = None
    energy_2: str | float | types.Real = None
    ratio_3: str | float | types.Real = None
    energy_3: str | float | types.Real = None
    ratio_4: str | float | types.Real = None
    energy_4: str | float | types.Real = None
    ratio_5: str | float | types.Real = None
    energy_5: str | float | types.Real = None
    ratio_6: str | float | types.Real = None
    energy_6: str | float | types.Real = None
    ratio_7: str | float | types.Real = None
    energy_7: str | float | types.Real = None
    ratio_8: str | float | types.Real = None
    energy_8: str | float | types.Real = None
    ratio_9: str | float | types.Real = None
    energy_9: str | float | types.Real = None
    ratio_10: str | float | types.Real = None
    energy_10: str | float | types.Real = None
    ratio_11: str | float | types.Real = None
    energy_11: str | float | types.Real = None
    ratio_12: str | float | types.Real = None
    energy_12: str | float | types.Real = None
    ratio_13: str | float | types.Real = None
    energy_13: str | float | types.Real = None
    ratio_14: str | float | types.Real = None
    energy_14: str | float | types.Real = None
    ratio_15: str | float | types.Real = None
    energy_15: str | float | types.Real = None
    ratio_16: str | float | types.Real = None
    energy_16: str | float | types.Real = None
    ratio_17: str | float | types.Real = None
    energy_17: str | float | types.Real = None
    ratio_18: str | float | types.Real = None
    energy_18: str | float | types.Real = None
    ratio_19: str | float | types.Real = None
    energy_19: str | float | types.Real = None
    ratio_20: str | float | types.Real = None
    energy_20: str | float | types.Real = None

    def build(self):
        """
        Builds ``EspltBuilder`` into ``Esplt``.

        Returns:
            ``Esplt`` for ``EspltBuilder``.
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

        energy_1 = self.energy_1
        if isinstance(self.energy_1, types.Real):
            energy_1 = self.energy_1
        elif isinstance(self.energy_1, float) or isinstance(self.energy_1, int):
            energy_1 = types.Real(self.energy_1)
        elif isinstance(self.energy_1, str):
            energy_1 = types.Real.from_mcnp(self.energy_1)

        ratio_2 = self.ratio_2
        if isinstance(self.ratio_2, types.Real):
            ratio_2 = self.ratio_2
        elif isinstance(self.ratio_2, float) or isinstance(self.ratio_2, int):
            ratio_2 = types.Real(self.ratio_2)
        elif isinstance(self.ratio_2, str):
            ratio_2 = types.Real.from_mcnp(self.ratio_2)

        energy_2 = self.energy_2
        if isinstance(self.energy_2, types.Real):
            energy_2 = self.energy_2
        elif isinstance(self.energy_2, float) or isinstance(self.energy_2, int):
            energy_2 = types.Real(self.energy_2)
        elif isinstance(self.energy_2, str):
            energy_2 = types.Real.from_mcnp(self.energy_2)

        ratio_3 = self.ratio_3
        if isinstance(self.ratio_3, types.Real):
            ratio_3 = self.ratio_3
        elif isinstance(self.ratio_3, float) or isinstance(self.ratio_3, int):
            ratio_3 = types.Real(self.ratio_3)
        elif isinstance(self.ratio_3, str):
            ratio_3 = types.Real.from_mcnp(self.ratio_3)

        energy_3 = self.energy_3
        if isinstance(self.energy_3, types.Real):
            energy_3 = self.energy_3
        elif isinstance(self.energy_3, float) or isinstance(self.energy_3, int):
            energy_3 = types.Real(self.energy_3)
        elif isinstance(self.energy_3, str):
            energy_3 = types.Real.from_mcnp(self.energy_3)

        ratio_4 = self.ratio_4
        if isinstance(self.ratio_4, types.Real):
            ratio_4 = self.ratio_4
        elif isinstance(self.ratio_4, float) or isinstance(self.ratio_4, int):
            ratio_4 = types.Real(self.ratio_4)
        elif isinstance(self.ratio_4, str):
            ratio_4 = types.Real.from_mcnp(self.ratio_4)

        energy_4 = self.energy_4
        if isinstance(self.energy_4, types.Real):
            energy_4 = self.energy_4
        elif isinstance(self.energy_4, float) or isinstance(self.energy_4, int):
            energy_4 = types.Real(self.energy_4)
        elif isinstance(self.energy_4, str):
            energy_4 = types.Real.from_mcnp(self.energy_4)

        ratio_5 = self.ratio_5
        if isinstance(self.ratio_5, types.Real):
            ratio_5 = self.ratio_5
        elif isinstance(self.ratio_5, float) or isinstance(self.ratio_5, int):
            ratio_5 = types.Real(self.ratio_5)
        elif isinstance(self.ratio_5, str):
            ratio_5 = types.Real.from_mcnp(self.ratio_5)

        energy_5 = self.energy_5
        if isinstance(self.energy_5, types.Real):
            energy_5 = self.energy_5
        elif isinstance(self.energy_5, float) or isinstance(self.energy_5, int):
            energy_5 = types.Real(self.energy_5)
        elif isinstance(self.energy_5, str):
            energy_5 = types.Real.from_mcnp(self.energy_5)

        ratio_6 = self.ratio_6
        if isinstance(self.ratio_6, types.Real):
            ratio_6 = self.ratio_6
        elif isinstance(self.ratio_6, float) or isinstance(self.ratio_6, int):
            ratio_6 = types.Real(self.ratio_6)
        elif isinstance(self.ratio_6, str):
            ratio_6 = types.Real.from_mcnp(self.ratio_6)

        energy_6 = self.energy_6
        if isinstance(self.energy_6, types.Real):
            energy_6 = self.energy_6
        elif isinstance(self.energy_6, float) or isinstance(self.energy_6, int):
            energy_6 = types.Real(self.energy_6)
        elif isinstance(self.energy_6, str):
            energy_6 = types.Real.from_mcnp(self.energy_6)

        ratio_7 = self.ratio_7
        if isinstance(self.ratio_7, types.Real):
            ratio_7 = self.ratio_7
        elif isinstance(self.ratio_7, float) or isinstance(self.ratio_7, int):
            ratio_7 = types.Real(self.ratio_7)
        elif isinstance(self.ratio_7, str):
            ratio_7 = types.Real.from_mcnp(self.ratio_7)

        energy_7 = self.energy_7
        if isinstance(self.energy_7, types.Real):
            energy_7 = self.energy_7
        elif isinstance(self.energy_7, float) or isinstance(self.energy_7, int):
            energy_7 = types.Real(self.energy_7)
        elif isinstance(self.energy_7, str):
            energy_7 = types.Real.from_mcnp(self.energy_7)

        ratio_8 = self.ratio_8
        if isinstance(self.ratio_8, types.Real):
            ratio_8 = self.ratio_8
        elif isinstance(self.ratio_8, float) or isinstance(self.ratio_8, int):
            ratio_8 = types.Real(self.ratio_8)
        elif isinstance(self.ratio_8, str):
            ratio_8 = types.Real.from_mcnp(self.ratio_8)

        energy_8 = self.energy_8
        if isinstance(self.energy_8, types.Real):
            energy_8 = self.energy_8
        elif isinstance(self.energy_8, float) or isinstance(self.energy_8, int):
            energy_8 = types.Real(self.energy_8)
        elif isinstance(self.energy_8, str):
            energy_8 = types.Real.from_mcnp(self.energy_8)

        ratio_9 = self.ratio_9
        if isinstance(self.ratio_9, types.Real):
            ratio_9 = self.ratio_9
        elif isinstance(self.ratio_9, float) or isinstance(self.ratio_9, int):
            ratio_9 = types.Real(self.ratio_9)
        elif isinstance(self.ratio_9, str):
            ratio_9 = types.Real.from_mcnp(self.ratio_9)

        energy_9 = self.energy_9
        if isinstance(self.energy_9, types.Real):
            energy_9 = self.energy_9
        elif isinstance(self.energy_9, float) or isinstance(self.energy_9, int):
            energy_9 = types.Real(self.energy_9)
        elif isinstance(self.energy_9, str):
            energy_9 = types.Real.from_mcnp(self.energy_9)

        ratio_10 = self.ratio_10
        if isinstance(self.ratio_10, types.Real):
            ratio_10 = self.ratio_10
        elif isinstance(self.ratio_10, float) or isinstance(self.ratio_10, int):
            ratio_10 = types.Real(self.ratio_10)
        elif isinstance(self.ratio_10, str):
            ratio_10 = types.Real.from_mcnp(self.ratio_10)

        energy_10 = self.energy_10
        if isinstance(self.energy_10, types.Real):
            energy_10 = self.energy_10
        elif isinstance(self.energy_10, float) or isinstance(self.energy_10, int):
            energy_10 = types.Real(self.energy_10)
        elif isinstance(self.energy_10, str):
            energy_10 = types.Real.from_mcnp(self.energy_10)

        ratio_11 = self.ratio_11
        if isinstance(self.ratio_11, types.Real):
            ratio_11 = self.ratio_11
        elif isinstance(self.ratio_11, float) or isinstance(self.ratio_11, int):
            ratio_11 = types.Real(self.ratio_11)
        elif isinstance(self.ratio_11, str):
            ratio_11 = types.Real.from_mcnp(self.ratio_11)

        energy_11 = self.energy_11
        if isinstance(self.energy_11, types.Real):
            energy_11 = self.energy_11
        elif isinstance(self.energy_11, float) or isinstance(self.energy_11, int):
            energy_11 = types.Real(self.energy_11)
        elif isinstance(self.energy_11, str):
            energy_11 = types.Real.from_mcnp(self.energy_11)

        ratio_12 = self.ratio_12
        if isinstance(self.ratio_12, types.Real):
            ratio_12 = self.ratio_12
        elif isinstance(self.ratio_12, float) or isinstance(self.ratio_12, int):
            ratio_12 = types.Real(self.ratio_12)
        elif isinstance(self.ratio_12, str):
            ratio_12 = types.Real.from_mcnp(self.ratio_12)

        energy_12 = self.energy_12
        if isinstance(self.energy_12, types.Real):
            energy_12 = self.energy_12
        elif isinstance(self.energy_12, float) or isinstance(self.energy_12, int):
            energy_12 = types.Real(self.energy_12)
        elif isinstance(self.energy_12, str):
            energy_12 = types.Real.from_mcnp(self.energy_12)

        ratio_13 = self.ratio_13
        if isinstance(self.ratio_13, types.Real):
            ratio_13 = self.ratio_13
        elif isinstance(self.ratio_13, float) or isinstance(self.ratio_13, int):
            ratio_13 = types.Real(self.ratio_13)
        elif isinstance(self.ratio_13, str):
            ratio_13 = types.Real.from_mcnp(self.ratio_13)

        energy_13 = self.energy_13
        if isinstance(self.energy_13, types.Real):
            energy_13 = self.energy_13
        elif isinstance(self.energy_13, float) or isinstance(self.energy_13, int):
            energy_13 = types.Real(self.energy_13)
        elif isinstance(self.energy_13, str):
            energy_13 = types.Real.from_mcnp(self.energy_13)

        ratio_14 = self.ratio_14
        if isinstance(self.ratio_14, types.Real):
            ratio_14 = self.ratio_14
        elif isinstance(self.ratio_14, float) or isinstance(self.ratio_14, int):
            ratio_14 = types.Real(self.ratio_14)
        elif isinstance(self.ratio_14, str):
            ratio_14 = types.Real.from_mcnp(self.ratio_14)

        energy_14 = self.energy_14
        if isinstance(self.energy_14, types.Real):
            energy_14 = self.energy_14
        elif isinstance(self.energy_14, float) or isinstance(self.energy_14, int):
            energy_14 = types.Real(self.energy_14)
        elif isinstance(self.energy_14, str):
            energy_14 = types.Real.from_mcnp(self.energy_14)

        ratio_15 = self.ratio_15
        if isinstance(self.ratio_15, types.Real):
            ratio_15 = self.ratio_15
        elif isinstance(self.ratio_15, float) or isinstance(self.ratio_15, int):
            ratio_15 = types.Real(self.ratio_15)
        elif isinstance(self.ratio_15, str):
            ratio_15 = types.Real.from_mcnp(self.ratio_15)

        energy_15 = self.energy_15
        if isinstance(self.energy_15, types.Real):
            energy_15 = self.energy_15
        elif isinstance(self.energy_15, float) or isinstance(self.energy_15, int):
            energy_15 = types.Real(self.energy_15)
        elif isinstance(self.energy_15, str):
            energy_15 = types.Real.from_mcnp(self.energy_15)

        ratio_16 = self.ratio_16
        if isinstance(self.ratio_16, types.Real):
            ratio_16 = self.ratio_16
        elif isinstance(self.ratio_16, float) or isinstance(self.ratio_16, int):
            ratio_16 = types.Real(self.ratio_16)
        elif isinstance(self.ratio_16, str):
            ratio_16 = types.Real.from_mcnp(self.ratio_16)

        energy_16 = self.energy_16
        if isinstance(self.energy_16, types.Real):
            energy_16 = self.energy_16
        elif isinstance(self.energy_16, float) or isinstance(self.energy_16, int):
            energy_16 = types.Real(self.energy_16)
        elif isinstance(self.energy_16, str):
            energy_16 = types.Real.from_mcnp(self.energy_16)

        ratio_17 = self.ratio_17
        if isinstance(self.ratio_17, types.Real):
            ratio_17 = self.ratio_17
        elif isinstance(self.ratio_17, float) or isinstance(self.ratio_17, int):
            ratio_17 = types.Real(self.ratio_17)
        elif isinstance(self.ratio_17, str):
            ratio_17 = types.Real.from_mcnp(self.ratio_17)

        energy_17 = self.energy_17
        if isinstance(self.energy_17, types.Real):
            energy_17 = self.energy_17
        elif isinstance(self.energy_17, float) or isinstance(self.energy_17, int):
            energy_17 = types.Real(self.energy_17)
        elif isinstance(self.energy_17, str):
            energy_17 = types.Real.from_mcnp(self.energy_17)

        ratio_18 = self.ratio_18
        if isinstance(self.ratio_18, types.Real):
            ratio_18 = self.ratio_18
        elif isinstance(self.ratio_18, float) or isinstance(self.ratio_18, int):
            ratio_18 = types.Real(self.ratio_18)
        elif isinstance(self.ratio_18, str):
            ratio_18 = types.Real.from_mcnp(self.ratio_18)

        energy_18 = self.energy_18
        if isinstance(self.energy_18, types.Real):
            energy_18 = self.energy_18
        elif isinstance(self.energy_18, float) or isinstance(self.energy_18, int):
            energy_18 = types.Real(self.energy_18)
        elif isinstance(self.energy_18, str):
            energy_18 = types.Real.from_mcnp(self.energy_18)

        ratio_19 = self.ratio_19
        if isinstance(self.ratio_19, types.Real):
            ratio_19 = self.ratio_19
        elif isinstance(self.ratio_19, float) or isinstance(self.ratio_19, int):
            ratio_19 = types.Real(self.ratio_19)
        elif isinstance(self.ratio_19, str):
            ratio_19 = types.Real.from_mcnp(self.ratio_19)

        energy_19 = self.energy_19
        if isinstance(self.energy_19, types.Real):
            energy_19 = self.energy_19
        elif isinstance(self.energy_19, float) or isinstance(self.energy_19, int):
            energy_19 = types.Real(self.energy_19)
        elif isinstance(self.energy_19, str):
            energy_19 = types.Real.from_mcnp(self.energy_19)

        ratio_20 = self.ratio_20
        if isinstance(self.ratio_20, types.Real):
            ratio_20 = self.ratio_20
        elif isinstance(self.ratio_20, float) or isinstance(self.ratio_20, int):
            ratio_20 = types.Real(self.ratio_20)
        elif isinstance(self.ratio_20, str):
            ratio_20 = types.Real.from_mcnp(self.ratio_20)

        energy_20 = self.energy_20
        if isinstance(self.energy_20, types.Real):
            energy_20 = self.energy_20
        elif isinstance(self.energy_20, float) or isinstance(self.energy_20, int):
            energy_20 = types.Real(self.energy_20)
        elif isinstance(self.energy_20, str):
            energy_20 = types.Real.from_mcnp(self.energy_20)

        return Esplt(
            designator=designator,
            ratio_1=ratio_1,
            energy_1=energy_1,
            ratio_2=ratio_2,
            energy_2=energy_2,
            ratio_3=ratio_3,
            energy_3=energy_3,
            ratio_4=ratio_4,
            energy_4=energy_4,
            ratio_5=ratio_5,
            energy_5=energy_5,
            ratio_6=ratio_6,
            energy_6=energy_6,
            ratio_7=ratio_7,
            energy_7=energy_7,
            ratio_8=ratio_8,
            energy_8=energy_8,
            ratio_9=ratio_9,
            energy_9=energy_9,
            ratio_10=ratio_10,
            energy_10=energy_10,
            ratio_11=ratio_11,
            energy_11=energy_11,
            ratio_12=ratio_12,
            energy_12=energy_12,
            ratio_13=ratio_13,
            energy_13=energy_13,
            ratio_14=ratio_14,
            energy_14=energy_14,
            ratio_15=ratio_15,
            energy_15=energy_15,
            ratio_16=ratio_16,
            energy_16=energy_16,
            ratio_17=ratio_17,
            energy_17=energy_17,
            ratio_18=ratio_18,
            energy_18=energy_18,
            ratio_19=ratio_19,
            energy_19=energy_19,
            ratio_20=ratio_20,
            energy_20=energy_20,
        )

    @staticmethod
    def unbuild(ast: Esplt):
        """
        Unbuilds ``Esplt`` into ``EspltBuilder``

        Returns:
            ``EspltBuilder`` for ``Esplt``.
        """

        return EspltBuilder(
            designator=copy.deepcopy(ast.designator),
            ratio_1=copy.deepcopy(ast.ratio_1),
            energy_1=copy.deepcopy(ast.energy_1),
            ratio_2=copy.deepcopy(ast.ratio_2),
            energy_2=copy.deepcopy(ast.energy_2),
            ratio_3=copy.deepcopy(ast.ratio_3),
            energy_3=copy.deepcopy(ast.energy_3),
            ratio_4=copy.deepcopy(ast.ratio_4),
            energy_4=copy.deepcopy(ast.energy_4),
            ratio_5=copy.deepcopy(ast.ratio_5),
            energy_5=copy.deepcopy(ast.energy_5),
            ratio_6=copy.deepcopy(ast.ratio_6),
            energy_6=copy.deepcopy(ast.energy_6),
            ratio_7=copy.deepcopy(ast.ratio_7),
            energy_7=copy.deepcopy(ast.energy_7),
            ratio_8=copy.deepcopy(ast.ratio_8),
            energy_8=copy.deepcopy(ast.energy_8),
            ratio_9=copy.deepcopy(ast.ratio_9),
            energy_9=copy.deepcopy(ast.energy_9),
            ratio_10=copy.deepcopy(ast.ratio_10),
            energy_10=copy.deepcopy(ast.energy_10),
            ratio_11=copy.deepcopy(ast.ratio_11),
            energy_11=copy.deepcopy(ast.energy_11),
            ratio_12=copy.deepcopy(ast.ratio_12),
            energy_12=copy.deepcopy(ast.energy_12),
            ratio_13=copy.deepcopy(ast.ratio_13),
            energy_13=copy.deepcopy(ast.energy_13),
            ratio_14=copy.deepcopy(ast.ratio_14),
            energy_14=copy.deepcopy(ast.energy_14),
            ratio_15=copy.deepcopy(ast.ratio_15),
            energy_15=copy.deepcopy(ast.energy_15),
            ratio_16=copy.deepcopy(ast.ratio_16),
            energy_16=copy.deepcopy(ast.energy_16),
            ratio_17=copy.deepcopy(ast.ratio_17),
            energy_17=copy.deepcopy(ast.energy_17),
            ratio_18=copy.deepcopy(ast.ratio_18),
            energy_18=copy.deepcopy(ast.energy_18),
            ratio_19=copy.deepcopy(ast.ratio_19),
            energy_19=copy.deepcopy(ast.energy_19),
            ratio_20=copy.deepcopy(ast.ratio_20),
            energy_20=copy.deepcopy(ast.energy_20),
        )
