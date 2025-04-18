import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Bbrem(DataOption_, keyword='bbrem'):
    """
    Represents INP bbrem elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'bias_1': types.RealOrJump,
        'bias_2': types.RealOrJump,
        'bias_3': types.RealOrJump,
        'bias_4': types.RealOrJump,
        'bias_5': types.RealOrJump,
        'bias_6': types.RealOrJump,
        'bias_7': types.RealOrJump,
        'bias_8': types.RealOrJump,
        'bias_9': types.RealOrJump,
        'bias_10': types.RealOrJump,
        'bias_11': types.RealOrJump,
        'bias_12': types.RealOrJump,
        'bias_13': types.RealOrJump,
        'bias_14': types.RealOrJump,
        'bias_15': types.RealOrJump,
        'bias_16': types.RealOrJump,
        'bias_17': types.RealOrJump,
        'bias_18': types.RealOrJump,
        'bias_19': types.RealOrJump,
        'bias_20': types.RealOrJump,
        'bias_21': types.RealOrJump,
        'bias_22': types.RealOrJump,
        'bias_23': types.RealOrJump,
        'bias_24': types.RealOrJump,
        'bias_25': types.RealOrJump,
        'bias_26': types.RealOrJump,
        'bias_27': types.RealOrJump,
        'bias_28': types.RealOrJump,
        'bias_29': types.RealOrJump,
        'bias_30': types.RealOrJump,
        'bias_31': types.RealOrJump,
        'bias_32': types.RealOrJump,
        'bias_33': types.RealOrJump,
        'bias_34': types.RealOrJump,
        'bias_35': types.RealOrJump,
        'bias_36': types.RealOrJump,
        'bias_37': types.RealOrJump,
        'bias_38': types.RealOrJump,
        'bias_39': types.RealOrJump,
        'bias_40': types.RealOrJump,
        'bias_41': types.RealOrJump,
        'bias_42': types.RealOrJump,
        'bias_43': types.RealOrJump,
        'bias_44': types.RealOrJump,
        'bias_45': types.RealOrJump,
        'bias_46': types.RealOrJump,
        'bias_47': types.RealOrJump,
        'bias_48': types.RealOrJump,
        'bias_49': types.RealOrJump,
        'materials': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(
        rf'\Abbrem( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z'
    )

    def __init__(
        self,
        bias_1: types.RealOrJump,
        bias_2: types.RealOrJump,
        bias_3: types.RealOrJump,
        bias_4: types.RealOrJump,
        bias_5: types.RealOrJump,
        bias_6: types.RealOrJump,
        bias_7: types.RealOrJump,
        bias_8: types.RealOrJump,
        bias_9: types.RealOrJump,
        bias_10: types.RealOrJump,
        bias_11: types.RealOrJump,
        bias_12: types.RealOrJump,
        bias_13: types.RealOrJump,
        bias_14: types.RealOrJump,
        bias_15: types.RealOrJump,
        bias_16: types.RealOrJump,
        bias_17: types.RealOrJump,
        bias_18: types.RealOrJump,
        bias_19: types.RealOrJump,
        bias_20: types.RealOrJump,
        bias_21: types.RealOrJump,
        bias_22: types.RealOrJump,
        bias_23: types.RealOrJump,
        bias_24: types.RealOrJump,
        bias_25: types.RealOrJump,
        bias_26: types.RealOrJump,
        bias_27: types.RealOrJump,
        bias_28: types.RealOrJump,
        bias_29: types.RealOrJump,
        bias_30: types.RealOrJump,
        bias_31: types.RealOrJump,
        bias_32: types.RealOrJump,
        bias_33: types.RealOrJump,
        bias_34: types.RealOrJump,
        bias_35: types.RealOrJump,
        bias_36: types.RealOrJump,
        bias_37: types.RealOrJump,
        bias_38: types.RealOrJump,
        bias_39: types.RealOrJump,
        bias_40: types.RealOrJump,
        bias_41: types.RealOrJump,
        bias_42: types.RealOrJump,
        bias_43: types.RealOrJump,
        bias_44: types.RealOrJump,
        bias_45: types.RealOrJump,
        bias_46: types.RealOrJump,
        bias_47: types.RealOrJump,
        bias_48: types.RealOrJump,
        bias_49: types.RealOrJump,
        materials: types.Tuple[types.IntegerOrJump],
    ):
        """
        Initializes ``Bbrem``.

        Parameters:
            bias_1: Bias factor #1 for bremsstrahlung specturm.
            bias_2: Bias factor #2 for bremsstrahlung specturm.
            bias_3: Bias factor #3 for bremsstrahlung specturm.
            bias_4: Bias factor #4 for bremsstrahlung specturm.
            bias_5: Bias factor #5 for bremsstrahlung specturm.
            bias_6: Bias factor #6 for bremsstrahlung specturm.
            bias_7: Bias factor #7 for bremsstrahlung specturm.
            bias_8: Bias factor #8 for bremsstrahlung specturm.
            bias_9: Bias factor #9 for bremsstrahlung specturm.
            bias_10: Bias factor #10 for bremsstrahlung specturm.
            bias_11: Bias factor #11 for bremsstrahlung specturm.
            bias_12: Bias factor #12 for bremsstrahlung specturm.
            bias_13: Bias factor #13 for bremsstrahlung specturm.
            bias_14: Bias factor #14 for bremsstrahlung specturm.
            bias_15: Bias factor #15 for bremsstrahlung specturm.
            bias_16: Bias factor #16 for bremsstrahlung specturm.
            bias_17: Bias factor #17 for bremsstrahlung specturm.
            bias_18: Bias factor #18 for bremsstrahlung specturm.
            bias_19: Bias factor #19 for bremsstrahlung specturm.
            bias_20: Bias factor #20 for bremsstrahlung specturm.
            bias_21: Bias factor #21 for bremsstrahlung specturm.
            bias_22: Bias factor #22 for bremsstrahlung specturm.
            bias_23: Bias factor #23 for bremsstrahlung specturm.
            bias_24: Bias factor #24 for bremsstrahlung specturm.
            bias_25: Bias factor #25 for bremsstrahlung specturm.
            bias_26: Bias factor #26 for bremsstrahlung specturm.
            bias_27: Bias factor #27 for bremsstrahlung specturm.
            bias_28: Bias factor #28 for bremsstrahlung specturm.
            bias_29: Bias factor #29 for bremsstrahlung specturm.
            bias_30: Bias factor #30 for bremsstrahlung specturm.
            bias_31: Bias factor #31 for bremsstrahlung specturm.
            bias_32: Bias factor #32 for bremsstrahlung specturm.
            bias_33: Bias factor #33 for bremsstrahlung specturm.
            bias_34: Bias factor #34 for bremsstrahlung specturm.
            bias_35: Bias factor #35 for bremsstrahlung specturm.
            bias_36: Bias factor #36 for bremsstrahlung specturm.
            bias_37: Bias factor #37 for bremsstrahlung specturm.
            bias_38: Bias factor #38 for bremsstrahlung specturm.
            bias_39: Bias factor #39 for bremsstrahlung specturm.
            bias_40: Bias factor #40 for bremsstrahlung specturm.
            bias_41: Bias factor #41 for bremsstrahlung specturm.
            bias_42: Bias factor #42 for bremsstrahlung specturm.
            bias_43: Bias factor #43 for bremsstrahlung specturm.
            bias_44: Bias factor #44 for bremsstrahlung specturm.
            bias_45: Bias factor #45 for bremsstrahlung specturm.
            bias_46: Bias factor #46 for bremsstrahlung specturm.
            bias_47: Bias factor #47 for bremsstrahlung specturm.
            bias_48: Bias factor #48 for bremsstrahlung specturm.
            bias_49: Bias factor #49 for bremsstrahlung specturm.
            materials: Material to bias.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if bias_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_1)
        if bias_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_2)
        if bias_3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_3)
        if bias_4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_4)
        if bias_5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_5)
        if bias_6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_6)
        if bias_7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_7)
        if bias_8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_8)
        if bias_9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_9)
        if bias_10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_10)
        if bias_11 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_11)
        if bias_12 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_12)
        if bias_13 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_13)
        if bias_14 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_14)
        if bias_15 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_15)
        if bias_16 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_16)
        if bias_17 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_17)
        if bias_18 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_18)
        if bias_19 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_19)
        if bias_20 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_20)
        if bias_21 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_21)
        if bias_22 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_22)
        if bias_23 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_23)
        if bias_24 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_24)
        if bias_25 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_25)
        if bias_26 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_26)
        if bias_27 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_27)
        if bias_28 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_28)
        if bias_29 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_29)
        if bias_30 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_30)
        if bias_31 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_31)
        if bias_32 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_32)
        if bias_33 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_33)
        if bias_34 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_34)
        if bias_35 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_35)
        if bias_36 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_36)
        if bias_37 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_37)
        if bias_38 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_38)
        if bias_39 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_39)
        if bias_40 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_40)
        if bias_41 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_41)
        if bias_42 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_42)
        if bias_43 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_43)
        if bias_44 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_44)
        if bias_45 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_45)
        if bias_46 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_46)
        if bias_47 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_47)
        if bias_48 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_48)
        if bias_49 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bias_49)
        if materials is None or not (
            filter(lambda entry: not (0 <= entry <= 99_999_999), materials)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, materials)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bias_1,
                bias_2,
                bias_3,
                bias_4,
                bias_5,
                bias_6,
                bias_7,
                bias_8,
                bias_9,
                bias_10,
                bias_11,
                bias_12,
                bias_13,
                bias_14,
                bias_15,
                bias_16,
                bias_17,
                bias_18,
                bias_19,
                bias_20,
                bias_21,
                bias_22,
                bias_23,
                bias_24,
                bias_25,
                bias_26,
                bias_27,
                bias_28,
                bias_29,
                bias_30,
                bias_31,
                bias_32,
                bias_33,
                bias_34,
                bias_35,
                bias_36,
                bias_37,
                bias_38,
                bias_39,
                bias_40,
                bias_41,
                bias_42,
                bias_43,
                bias_44,
                bias_45,
                bias_46,
                bias_47,
                bias_48,
                bias_49,
                materials,
            ]
        )

        self.bias_1: typing.Final[types.RealOrJump] = bias_1
        self.bias_2: typing.Final[types.RealOrJump] = bias_2
        self.bias_3: typing.Final[types.RealOrJump] = bias_3
        self.bias_4: typing.Final[types.RealOrJump] = bias_4
        self.bias_5: typing.Final[types.RealOrJump] = bias_5
        self.bias_6: typing.Final[types.RealOrJump] = bias_6
        self.bias_7: typing.Final[types.RealOrJump] = bias_7
        self.bias_8: typing.Final[types.RealOrJump] = bias_8
        self.bias_9: typing.Final[types.RealOrJump] = bias_9
        self.bias_10: typing.Final[types.RealOrJump] = bias_10
        self.bias_11: typing.Final[types.RealOrJump] = bias_11
        self.bias_12: typing.Final[types.RealOrJump] = bias_12
        self.bias_13: typing.Final[types.RealOrJump] = bias_13
        self.bias_14: typing.Final[types.RealOrJump] = bias_14
        self.bias_15: typing.Final[types.RealOrJump] = bias_15
        self.bias_16: typing.Final[types.RealOrJump] = bias_16
        self.bias_17: typing.Final[types.RealOrJump] = bias_17
        self.bias_18: typing.Final[types.RealOrJump] = bias_18
        self.bias_19: typing.Final[types.RealOrJump] = bias_19
        self.bias_20: typing.Final[types.RealOrJump] = bias_20
        self.bias_21: typing.Final[types.RealOrJump] = bias_21
        self.bias_22: typing.Final[types.RealOrJump] = bias_22
        self.bias_23: typing.Final[types.RealOrJump] = bias_23
        self.bias_24: typing.Final[types.RealOrJump] = bias_24
        self.bias_25: typing.Final[types.RealOrJump] = bias_25
        self.bias_26: typing.Final[types.RealOrJump] = bias_26
        self.bias_27: typing.Final[types.RealOrJump] = bias_27
        self.bias_28: typing.Final[types.RealOrJump] = bias_28
        self.bias_29: typing.Final[types.RealOrJump] = bias_29
        self.bias_30: typing.Final[types.RealOrJump] = bias_30
        self.bias_31: typing.Final[types.RealOrJump] = bias_31
        self.bias_32: typing.Final[types.RealOrJump] = bias_32
        self.bias_33: typing.Final[types.RealOrJump] = bias_33
        self.bias_34: typing.Final[types.RealOrJump] = bias_34
        self.bias_35: typing.Final[types.RealOrJump] = bias_35
        self.bias_36: typing.Final[types.RealOrJump] = bias_36
        self.bias_37: typing.Final[types.RealOrJump] = bias_37
        self.bias_38: typing.Final[types.RealOrJump] = bias_38
        self.bias_39: typing.Final[types.RealOrJump] = bias_39
        self.bias_40: typing.Final[types.RealOrJump] = bias_40
        self.bias_41: typing.Final[types.RealOrJump] = bias_41
        self.bias_42: typing.Final[types.RealOrJump] = bias_42
        self.bias_43: typing.Final[types.RealOrJump] = bias_43
        self.bias_44: typing.Final[types.RealOrJump] = bias_44
        self.bias_45: typing.Final[types.RealOrJump] = bias_45
        self.bias_46: typing.Final[types.RealOrJump] = bias_46
        self.bias_47: typing.Final[types.RealOrJump] = bias_47
        self.bias_48: typing.Final[types.RealOrJump] = bias_48
        self.bias_49: typing.Final[types.RealOrJump] = bias_49
        self.materials: typing.Final[types.Tuple[types.IntegerOrJump]] = materials
