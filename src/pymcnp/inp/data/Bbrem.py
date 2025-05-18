import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Bbrem(DataOption):
    """
    Represents INP bbrem elements.

    Attributes:
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
            InpError: SEMANTICS_OPTION.
        """

        if bias_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_1)
        if bias_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_2)
        if bias_3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_3)
        if bias_4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_4)
        if bias_5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_5)
        if bias_6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_6)
        if bias_7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_7)
        if bias_8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_8)
        if bias_9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_9)
        if bias_10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_10)
        if bias_11 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_11)
        if bias_12 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_12)
        if bias_13 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_13)
        if bias_14 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_14)
        if bias_15 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_15)
        if bias_16 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_16)
        if bias_17 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_17)
        if bias_18 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_18)
        if bias_19 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_19)
        if bias_20 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_20)
        if bias_21 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_21)
        if bias_22 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_22)
        if bias_23 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_23)
        if bias_24 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_24)
        if bias_25 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_25)
        if bias_26 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_26)
        if bias_27 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_27)
        if bias_28 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_28)
        if bias_29 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_29)
        if bias_30 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_30)
        if bias_31 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_31)
        if bias_32 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_32)
        if bias_33 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_33)
        if bias_34 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_34)
        if bias_35 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_35)
        if bias_36 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_36)
        if bias_37 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_37)
        if bias_38 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_38)
        if bias_39 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_39)
        if bias_40 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_40)
        if bias_41 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_41)
        if bias_42 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_42)
        if bias_43 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_43)
        if bias_44 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_44)
        if bias_45 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_45)
        if bias_46 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_46)
        if bias_47 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_47)
        if bias_48 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_48)
        if bias_49 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bias_49)
        if materials is None or not (
            filter(lambda entry: not (0 <= entry <= 99_999_999), materials)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, materials)

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


@dataclasses.dataclass
class BbremBuilder:
    """
    Builds ``Bbrem``.

    Attributes:
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
    """

    bias_1: str | float | types.RealOrJump
    bias_2: str | float | types.RealOrJump
    bias_3: str | float | types.RealOrJump
    bias_4: str | float | types.RealOrJump
    bias_5: str | float | types.RealOrJump
    bias_6: str | float | types.RealOrJump
    bias_7: str | float | types.RealOrJump
    bias_8: str | float | types.RealOrJump
    bias_9: str | float | types.RealOrJump
    bias_10: str | float | types.RealOrJump
    bias_11: str | float | types.RealOrJump
    bias_12: str | float | types.RealOrJump
    bias_13: str | float | types.RealOrJump
    bias_14: str | float | types.RealOrJump
    bias_15: str | float | types.RealOrJump
    bias_16: str | float | types.RealOrJump
    bias_17: str | float | types.RealOrJump
    bias_18: str | float | types.RealOrJump
    bias_19: str | float | types.RealOrJump
    bias_20: str | float | types.RealOrJump
    bias_21: str | float | types.RealOrJump
    bias_22: str | float | types.RealOrJump
    bias_23: str | float | types.RealOrJump
    bias_24: str | float | types.RealOrJump
    bias_25: str | float | types.RealOrJump
    bias_26: str | float | types.RealOrJump
    bias_27: str | float | types.RealOrJump
    bias_28: str | float | types.RealOrJump
    bias_29: str | float | types.RealOrJump
    bias_30: str | float | types.RealOrJump
    bias_31: str | float | types.RealOrJump
    bias_32: str | float | types.RealOrJump
    bias_33: str | float | types.RealOrJump
    bias_34: str | float | types.RealOrJump
    bias_35: str | float | types.RealOrJump
    bias_36: str | float | types.RealOrJump
    bias_37: str | float | types.RealOrJump
    bias_38: str | float | types.RealOrJump
    bias_39: str | float | types.RealOrJump
    bias_40: str | float | types.RealOrJump
    bias_41: str | float | types.RealOrJump
    bias_42: str | float | types.RealOrJump
    bias_43: str | float | types.RealOrJump
    bias_44: str | float | types.RealOrJump
    bias_45: str | float | types.RealOrJump
    bias_46: str | float | types.RealOrJump
    bias_47: str | float | types.RealOrJump
    bias_48: str | float | types.RealOrJump
    bias_49: str | float | types.RealOrJump
    materials: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``BbremBuilder`` into ``Bbrem``.

        Returns:
            ``Bbrem`` for ``BbremBuilder``.
        """

        bias_1 = self.bias_1
        if isinstance(self.bias_1, types.Real):
            bias_1 = self.bias_1
        elif isinstance(self.bias_1, float) or isinstance(self.bias_1, int):
            bias_1 = types.RealOrJump(self.bias_1)
        elif isinstance(self.bias_1, str):
            bias_1 = types.RealOrJump.from_mcnp(self.bias_1)

        bias_2 = self.bias_2
        if isinstance(self.bias_2, types.Real):
            bias_2 = self.bias_2
        elif isinstance(self.bias_2, float) or isinstance(self.bias_2, int):
            bias_2 = types.RealOrJump(self.bias_2)
        elif isinstance(self.bias_2, str):
            bias_2 = types.RealOrJump.from_mcnp(self.bias_2)

        bias_3 = self.bias_3
        if isinstance(self.bias_3, types.Real):
            bias_3 = self.bias_3
        elif isinstance(self.bias_3, float) or isinstance(self.bias_3, int):
            bias_3 = types.RealOrJump(self.bias_3)
        elif isinstance(self.bias_3, str):
            bias_3 = types.RealOrJump.from_mcnp(self.bias_3)

        bias_4 = self.bias_4
        if isinstance(self.bias_4, types.Real):
            bias_4 = self.bias_4
        elif isinstance(self.bias_4, float) or isinstance(self.bias_4, int):
            bias_4 = types.RealOrJump(self.bias_4)
        elif isinstance(self.bias_4, str):
            bias_4 = types.RealOrJump.from_mcnp(self.bias_4)

        bias_5 = self.bias_5
        if isinstance(self.bias_5, types.Real):
            bias_5 = self.bias_5
        elif isinstance(self.bias_5, float) or isinstance(self.bias_5, int):
            bias_5 = types.RealOrJump(self.bias_5)
        elif isinstance(self.bias_5, str):
            bias_5 = types.RealOrJump.from_mcnp(self.bias_5)

        bias_6 = self.bias_6
        if isinstance(self.bias_6, types.Real):
            bias_6 = self.bias_6
        elif isinstance(self.bias_6, float) or isinstance(self.bias_6, int):
            bias_6 = types.RealOrJump(self.bias_6)
        elif isinstance(self.bias_6, str):
            bias_6 = types.RealOrJump.from_mcnp(self.bias_6)

        bias_7 = self.bias_7
        if isinstance(self.bias_7, types.Real):
            bias_7 = self.bias_7
        elif isinstance(self.bias_7, float) or isinstance(self.bias_7, int):
            bias_7 = types.RealOrJump(self.bias_7)
        elif isinstance(self.bias_7, str):
            bias_7 = types.RealOrJump.from_mcnp(self.bias_7)

        bias_8 = self.bias_8
        if isinstance(self.bias_8, types.Real):
            bias_8 = self.bias_8
        elif isinstance(self.bias_8, float) or isinstance(self.bias_8, int):
            bias_8 = types.RealOrJump(self.bias_8)
        elif isinstance(self.bias_8, str):
            bias_8 = types.RealOrJump.from_mcnp(self.bias_8)

        bias_9 = self.bias_9
        if isinstance(self.bias_9, types.Real):
            bias_9 = self.bias_9
        elif isinstance(self.bias_9, float) or isinstance(self.bias_9, int):
            bias_9 = types.RealOrJump(self.bias_9)
        elif isinstance(self.bias_9, str):
            bias_9 = types.RealOrJump.from_mcnp(self.bias_9)

        bias_10 = self.bias_10
        if isinstance(self.bias_10, types.Real):
            bias_10 = self.bias_10
        elif isinstance(self.bias_10, float) or isinstance(self.bias_10, int):
            bias_10 = types.RealOrJump(self.bias_10)
        elif isinstance(self.bias_10, str):
            bias_10 = types.RealOrJump.from_mcnp(self.bias_10)

        bias_11 = self.bias_11
        if isinstance(self.bias_11, types.Real):
            bias_11 = self.bias_11
        elif isinstance(self.bias_11, float) or isinstance(self.bias_11, int):
            bias_11 = types.RealOrJump(self.bias_11)
        elif isinstance(self.bias_11, str):
            bias_11 = types.RealOrJump.from_mcnp(self.bias_11)

        bias_12 = self.bias_12
        if isinstance(self.bias_12, types.Real):
            bias_12 = self.bias_12
        elif isinstance(self.bias_12, float) or isinstance(self.bias_12, int):
            bias_12 = types.RealOrJump(self.bias_12)
        elif isinstance(self.bias_12, str):
            bias_12 = types.RealOrJump.from_mcnp(self.bias_12)

        bias_13 = self.bias_13
        if isinstance(self.bias_13, types.Real):
            bias_13 = self.bias_13
        elif isinstance(self.bias_13, float) or isinstance(self.bias_13, int):
            bias_13 = types.RealOrJump(self.bias_13)
        elif isinstance(self.bias_13, str):
            bias_13 = types.RealOrJump.from_mcnp(self.bias_13)

        bias_14 = self.bias_14
        if isinstance(self.bias_14, types.Real):
            bias_14 = self.bias_14
        elif isinstance(self.bias_14, float) or isinstance(self.bias_14, int):
            bias_14 = types.RealOrJump(self.bias_14)
        elif isinstance(self.bias_14, str):
            bias_14 = types.RealOrJump.from_mcnp(self.bias_14)

        bias_15 = self.bias_15
        if isinstance(self.bias_15, types.Real):
            bias_15 = self.bias_15
        elif isinstance(self.bias_15, float) or isinstance(self.bias_15, int):
            bias_15 = types.RealOrJump(self.bias_15)
        elif isinstance(self.bias_15, str):
            bias_15 = types.RealOrJump.from_mcnp(self.bias_15)

        bias_16 = self.bias_16
        if isinstance(self.bias_16, types.Real):
            bias_16 = self.bias_16
        elif isinstance(self.bias_16, float) or isinstance(self.bias_16, int):
            bias_16 = types.RealOrJump(self.bias_16)
        elif isinstance(self.bias_16, str):
            bias_16 = types.RealOrJump.from_mcnp(self.bias_16)

        bias_17 = self.bias_17
        if isinstance(self.bias_17, types.Real):
            bias_17 = self.bias_17
        elif isinstance(self.bias_17, float) or isinstance(self.bias_17, int):
            bias_17 = types.RealOrJump(self.bias_17)
        elif isinstance(self.bias_17, str):
            bias_17 = types.RealOrJump.from_mcnp(self.bias_17)

        bias_18 = self.bias_18
        if isinstance(self.bias_18, types.Real):
            bias_18 = self.bias_18
        elif isinstance(self.bias_18, float) or isinstance(self.bias_18, int):
            bias_18 = types.RealOrJump(self.bias_18)
        elif isinstance(self.bias_18, str):
            bias_18 = types.RealOrJump.from_mcnp(self.bias_18)

        bias_19 = self.bias_19
        if isinstance(self.bias_19, types.Real):
            bias_19 = self.bias_19
        elif isinstance(self.bias_19, float) or isinstance(self.bias_19, int):
            bias_19 = types.RealOrJump(self.bias_19)
        elif isinstance(self.bias_19, str):
            bias_19 = types.RealOrJump.from_mcnp(self.bias_19)

        bias_20 = self.bias_20
        if isinstance(self.bias_20, types.Real):
            bias_20 = self.bias_20
        elif isinstance(self.bias_20, float) or isinstance(self.bias_20, int):
            bias_20 = types.RealOrJump(self.bias_20)
        elif isinstance(self.bias_20, str):
            bias_20 = types.RealOrJump.from_mcnp(self.bias_20)

        bias_21 = self.bias_21
        if isinstance(self.bias_21, types.Real):
            bias_21 = self.bias_21
        elif isinstance(self.bias_21, float) or isinstance(self.bias_21, int):
            bias_21 = types.RealOrJump(self.bias_21)
        elif isinstance(self.bias_21, str):
            bias_21 = types.RealOrJump.from_mcnp(self.bias_21)

        bias_22 = self.bias_22
        if isinstance(self.bias_22, types.Real):
            bias_22 = self.bias_22
        elif isinstance(self.bias_22, float) or isinstance(self.bias_22, int):
            bias_22 = types.RealOrJump(self.bias_22)
        elif isinstance(self.bias_22, str):
            bias_22 = types.RealOrJump.from_mcnp(self.bias_22)

        bias_23 = self.bias_23
        if isinstance(self.bias_23, types.Real):
            bias_23 = self.bias_23
        elif isinstance(self.bias_23, float) or isinstance(self.bias_23, int):
            bias_23 = types.RealOrJump(self.bias_23)
        elif isinstance(self.bias_23, str):
            bias_23 = types.RealOrJump.from_mcnp(self.bias_23)

        bias_24 = self.bias_24
        if isinstance(self.bias_24, types.Real):
            bias_24 = self.bias_24
        elif isinstance(self.bias_24, float) or isinstance(self.bias_24, int):
            bias_24 = types.RealOrJump(self.bias_24)
        elif isinstance(self.bias_24, str):
            bias_24 = types.RealOrJump.from_mcnp(self.bias_24)

        bias_25 = self.bias_25
        if isinstance(self.bias_25, types.Real):
            bias_25 = self.bias_25
        elif isinstance(self.bias_25, float) or isinstance(self.bias_25, int):
            bias_25 = types.RealOrJump(self.bias_25)
        elif isinstance(self.bias_25, str):
            bias_25 = types.RealOrJump.from_mcnp(self.bias_25)

        bias_26 = self.bias_26
        if isinstance(self.bias_26, types.Real):
            bias_26 = self.bias_26
        elif isinstance(self.bias_26, float) or isinstance(self.bias_26, int):
            bias_26 = types.RealOrJump(self.bias_26)
        elif isinstance(self.bias_26, str):
            bias_26 = types.RealOrJump.from_mcnp(self.bias_26)

        bias_27 = self.bias_27
        if isinstance(self.bias_27, types.Real):
            bias_27 = self.bias_27
        elif isinstance(self.bias_27, float) or isinstance(self.bias_27, int):
            bias_27 = types.RealOrJump(self.bias_27)
        elif isinstance(self.bias_27, str):
            bias_27 = types.RealOrJump.from_mcnp(self.bias_27)

        bias_28 = self.bias_28
        if isinstance(self.bias_28, types.Real):
            bias_28 = self.bias_28
        elif isinstance(self.bias_28, float) or isinstance(self.bias_28, int):
            bias_28 = types.RealOrJump(self.bias_28)
        elif isinstance(self.bias_28, str):
            bias_28 = types.RealOrJump.from_mcnp(self.bias_28)

        bias_29 = self.bias_29
        if isinstance(self.bias_29, types.Real):
            bias_29 = self.bias_29
        elif isinstance(self.bias_29, float) or isinstance(self.bias_29, int):
            bias_29 = types.RealOrJump(self.bias_29)
        elif isinstance(self.bias_29, str):
            bias_29 = types.RealOrJump.from_mcnp(self.bias_29)

        bias_30 = self.bias_30
        if isinstance(self.bias_30, types.Real):
            bias_30 = self.bias_30
        elif isinstance(self.bias_30, float) or isinstance(self.bias_30, int):
            bias_30 = types.RealOrJump(self.bias_30)
        elif isinstance(self.bias_30, str):
            bias_30 = types.RealOrJump.from_mcnp(self.bias_30)

        bias_31 = self.bias_31
        if isinstance(self.bias_31, types.Real):
            bias_31 = self.bias_31
        elif isinstance(self.bias_31, float) or isinstance(self.bias_31, int):
            bias_31 = types.RealOrJump(self.bias_31)
        elif isinstance(self.bias_31, str):
            bias_31 = types.RealOrJump.from_mcnp(self.bias_31)

        bias_32 = self.bias_32
        if isinstance(self.bias_32, types.Real):
            bias_32 = self.bias_32
        elif isinstance(self.bias_32, float) or isinstance(self.bias_32, int):
            bias_32 = types.RealOrJump(self.bias_32)
        elif isinstance(self.bias_32, str):
            bias_32 = types.RealOrJump.from_mcnp(self.bias_32)

        bias_33 = self.bias_33
        if isinstance(self.bias_33, types.Real):
            bias_33 = self.bias_33
        elif isinstance(self.bias_33, float) or isinstance(self.bias_33, int):
            bias_33 = types.RealOrJump(self.bias_33)
        elif isinstance(self.bias_33, str):
            bias_33 = types.RealOrJump.from_mcnp(self.bias_33)

        bias_34 = self.bias_34
        if isinstance(self.bias_34, types.Real):
            bias_34 = self.bias_34
        elif isinstance(self.bias_34, float) or isinstance(self.bias_34, int):
            bias_34 = types.RealOrJump(self.bias_34)
        elif isinstance(self.bias_34, str):
            bias_34 = types.RealOrJump.from_mcnp(self.bias_34)

        bias_35 = self.bias_35
        if isinstance(self.bias_35, types.Real):
            bias_35 = self.bias_35
        elif isinstance(self.bias_35, float) or isinstance(self.bias_35, int):
            bias_35 = types.RealOrJump(self.bias_35)
        elif isinstance(self.bias_35, str):
            bias_35 = types.RealOrJump.from_mcnp(self.bias_35)

        bias_36 = self.bias_36
        if isinstance(self.bias_36, types.Real):
            bias_36 = self.bias_36
        elif isinstance(self.bias_36, float) or isinstance(self.bias_36, int):
            bias_36 = types.RealOrJump(self.bias_36)
        elif isinstance(self.bias_36, str):
            bias_36 = types.RealOrJump.from_mcnp(self.bias_36)

        bias_37 = self.bias_37
        if isinstance(self.bias_37, types.Real):
            bias_37 = self.bias_37
        elif isinstance(self.bias_37, float) or isinstance(self.bias_37, int):
            bias_37 = types.RealOrJump(self.bias_37)
        elif isinstance(self.bias_37, str):
            bias_37 = types.RealOrJump.from_mcnp(self.bias_37)

        bias_38 = self.bias_38
        if isinstance(self.bias_38, types.Real):
            bias_38 = self.bias_38
        elif isinstance(self.bias_38, float) or isinstance(self.bias_38, int):
            bias_38 = types.RealOrJump(self.bias_38)
        elif isinstance(self.bias_38, str):
            bias_38 = types.RealOrJump.from_mcnp(self.bias_38)

        bias_39 = self.bias_39
        if isinstance(self.bias_39, types.Real):
            bias_39 = self.bias_39
        elif isinstance(self.bias_39, float) or isinstance(self.bias_39, int):
            bias_39 = types.RealOrJump(self.bias_39)
        elif isinstance(self.bias_39, str):
            bias_39 = types.RealOrJump.from_mcnp(self.bias_39)

        bias_40 = self.bias_40
        if isinstance(self.bias_40, types.Real):
            bias_40 = self.bias_40
        elif isinstance(self.bias_40, float) or isinstance(self.bias_40, int):
            bias_40 = types.RealOrJump(self.bias_40)
        elif isinstance(self.bias_40, str):
            bias_40 = types.RealOrJump.from_mcnp(self.bias_40)

        bias_41 = self.bias_41
        if isinstance(self.bias_41, types.Real):
            bias_41 = self.bias_41
        elif isinstance(self.bias_41, float) or isinstance(self.bias_41, int):
            bias_41 = types.RealOrJump(self.bias_41)
        elif isinstance(self.bias_41, str):
            bias_41 = types.RealOrJump.from_mcnp(self.bias_41)

        bias_42 = self.bias_42
        if isinstance(self.bias_42, types.Real):
            bias_42 = self.bias_42
        elif isinstance(self.bias_42, float) or isinstance(self.bias_42, int):
            bias_42 = types.RealOrJump(self.bias_42)
        elif isinstance(self.bias_42, str):
            bias_42 = types.RealOrJump.from_mcnp(self.bias_42)

        bias_43 = self.bias_43
        if isinstance(self.bias_43, types.Real):
            bias_43 = self.bias_43
        elif isinstance(self.bias_43, float) or isinstance(self.bias_43, int):
            bias_43 = types.RealOrJump(self.bias_43)
        elif isinstance(self.bias_43, str):
            bias_43 = types.RealOrJump.from_mcnp(self.bias_43)

        bias_44 = self.bias_44
        if isinstance(self.bias_44, types.Real):
            bias_44 = self.bias_44
        elif isinstance(self.bias_44, float) or isinstance(self.bias_44, int):
            bias_44 = types.RealOrJump(self.bias_44)
        elif isinstance(self.bias_44, str):
            bias_44 = types.RealOrJump.from_mcnp(self.bias_44)

        bias_45 = self.bias_45
        if isinstance(self.bias_45, types.Real):
            bias_45 = self.bias_45
        elif isinstance(self.bias_45, float) or isinstance(self.bias_45, int):
            bias_45 = types.RealOrJump(self.bias_45)
        elif isinstance(self.bias_45, str):
            bias_45 = types.RealOrJump.from_mcnp(self.bias_45)

        bias_46 = self.bias_46
        if isinstance(self.bias_46, types.Real):
            bias_46 = self.bias_46
        elif isinstance(self.bias_46, float) or isinstance(self.bias_46, int):
            bias_46 = types.RealOrJump(self.bias_46)
        elif isinstance(self.bias_46, str):
            bias_46 = types.RealOrJump.from_mcnp(self.bias_46)

        bias_47 = self.bias_47
        if isinstance(self.bias_47, types.Real):
            bias_47 = self.bias_47
        elif isinstance(self.bias_47, float) or isinstance(self.bias_47, int):
            bias_47 = types.RealOrJump(self.bias_47)
        elif isinstance(self.bias_47, str):
            bias_47 = types.RealOrJump.from_mcnp(self.bias_47)

        bias_48 = self.bias_48
        if isinstance(self.bias_48, types.Real):
            bias_48 = self.bias_48
        elif isinstance(self.bias_48, float) or isinstance(self.bias_48, int):
            bias_48 = types.RealOrJump(self.bias_48)
        elif isinstance(self.bias_48, str):
            bias_48 = types.RealOrJump.from_mcnp(self.bias_48)

        bias_49 = self.bias_49
        if isinstance(self.bias_49, types.Real):
            bias_49 = self.bias_49
        elif isinstance(self.bias_49, float) or isinstance(self.bias_49, int):
            bias_49 = types.RealOrJump(self.bias_49)
        elif isinstance(self.bias_49, str):
            bias_49 = types.RealOrJump.from_mcnp(self.bias_49)

        if self.materials:
            materials = []
            for item in self.materials:
                if isinstance(item, types.IntegerOrJump):
                    materials.append(item)
                elif isinstance(item, int):
                    materials.append(types.IntegerOrJump(item))
                elif isinstance(item, str):
                    materials.append(types.IntegerOrJump.from_mcnp(item))
            materials = types.Tuple(materials)
        else:
            materials = None

        return Bbrem(
            bias_1=bias_1,
            bias_2=bias_2,
            bias_3=bias_3,
            bias_4=bias_4,
            bias_5=bias_5,
            bias_6=bias_6,
            bias_7=bias_7,
            bias_8=bias_8,
            bias_9=bias_9,
            bias_10=bias_10,
            bias_11=bias_11,
            bias_12=bias_12,
            bias_13=bias_13,
            bias_14=bias_14,
            bias_15=bias_15,
            bias_16=bias_16,
            bias_17=bias_17,
            bias_18=bias_18,
            bias_19=bias_19,
            bias_20=bias_20,
            bias_21=bias_21,
            bias_22=bias_22,
            bias_23=bias_23,
            bias_24=bias_24,
            bias_25=bias_25,
            bias_26=bias_26,
            bias_27=bias_27,
            bias_28=bias_28,
            bias_29=bias_29,
            bias_30=bias_30,
            bias_31=bias_31,
            bias_32=bias_32,
            bias_33=bias_33,
            bias_34=bias_34,
            bias_35=bias_35,
            bias_36=bias_36,
            bias_37=bias_37,
            bias_38=bias_38,
            bias_39=bias_39,
            bias_40=bias_40,
            bias_41=bias_41,
            bias_42=bias_42,
            bias_43=bias_43,
            bias_44=bias_44,
            bias_45=bias_45,
            bias_46=bias_46,
            bias_47=bias_47,
            bias_48=bias_48,
            bias_49=bias_49,
            materials=materials,
        )
