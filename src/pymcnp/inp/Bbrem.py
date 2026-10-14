import re

from . import _field
from . import _card
from .. import types


class Bbrem(_field.Fields, _card.Card):
    """
    Represents INP bbrem cards.
    """

    _KEYWORD = 'bbrem'

    bias_1 = _field.Field(types.Real, 'Bias factor #1 for bremsstrahlung specturm', required=True)
    bias_2 = _field.Field(types.Real, 'Bias factor #2 for bremsstrahlung specturm', required=True)
    bias_3 = _field.Field(types.Real, 'Bias factor #3 for bremsstrahlung specturm', required=True)
    bias_4 = _field.Field(types.Real, 'Bias factor #4 for bremsstrahlung specturm', required=True)
    bias_5 = _field.Field(types.Real, 'Bias factor #5 for bremsstrahlung specturm', required=True)
    bias_6 = _field.Field(types.Real, 'Bias factor #6 for bremsstrahlung specturm', required=True)
    bias_7 = _field.Field(types.Real, 'Bias factor #7 for bremsstrahlung specturm', required=True)
    bias_8 = _field.Field(types.Real, 'Bias factor #8 for bremsstrahlung specturm', required=True)
    bias_9 = _field.Field(types.Real, 'Bias factor #9 for bremsstrahlung specturm', required=True)
    bias_10 = _field.Field(types.Real, 'Bias factor #10 for bremsstrahlung specturm', required=True)
    bias_11 = _field.Field(types.Real, 'Bias factor #11 for bremsstrahlung specturm', required=True)
    bias_12 = _field.Field(types.Real, 'Bias factor #12 for bremsstrahlung specturm', required=True)
    bias_13 = _field.Field(types.Real, 'Bias factor #13 for bremsstrahlung specturm', required=True)
    bias_14 = _field.Field(types.Real, 'Bias factor #14 for bremsstrahlung specturm', required=True)
    bias_15 = _field.Field(types.Real, 'Bias factor #15 for bremsstrahlung specturm', required=True)
    bias_16 = _field.Field(types.Real, 'Bias factor #16 for bremsstrahlung specturm', required=True)
    bias_17 = _field.Field(types.Real, 'Bias factor #17 for bremsstrahlung specturm', required=True)
    bias_18 = _field.Field(types.Real, 'Bias factor #18 for bremsstrahlung specturm', required=True)
    bias_19 = _field.Field(types.Real, 'Bias factor #19 for bremsstrahlung specturm', required=True)
    bias_20 = _field.Field(types.Real, 'Bias factor #20 for bremsstrahlung specturm', required=True)
    bias_21 = _field.Field(types.Real, 'Bias factor #21 for bremsstrahlung specturm', required=True)
    bias_22 = _field.Field(types.Real, 'Bias factor #22 for bremsstrahlung specturm', required=True)
    bias_23 = _field.Field(types.Real, 'Bias factor #23 for bremsstrahlung specturm', required=True)
    bias_24 = _field.Field(types.Real, 'Bias factor #24 for bremsstrahlung specturm', required=True)
    bias_25 = _field.Field(types.Real, 'Bias factor #25 for bremsstrahlung specturm', required=True)
    bias_26 = _field.Field(types.Real, 'Bias factor #26 for bremsstrahlung specturm', required=True)
    bias_27 = _field.Field(types.Real, 'Bias factor #27 for bremsstrahlung specturm', required=True)
    bias_28 = _field.Field(types.Real, 'Bias factor #28 for bremsstrahlung specturm', required=True)
    bias_29 = _field.Field(types.Real, 'Bias factor #29 for bremsstrahlung specturm', required=True)
    bias_30 = _field.Field(types.Real, 'Bias factor #30 for bremsstrahlung specturm', required=True)
    bias_31 = _field.Field(types.Real, 'Bias factor #31 for bremsstrahlung specturm', required=True)
    bias_32 = _field.Field(types.Real, 'Bias factor #32 for bremsstrahlung specturm', required=True)
    bias_33 = _field.Field(types.Real, 'Bias factor #33 for bremsstrahlung specturm', required=True)
    bias_34 = _field.Field(types.Real, 'Bias factor #34 for bremsstrahlung specturm', required=True)
    bias_35 = _field.Field(types.Real, 'Bias factor #35 for bremsstrahlung specturm', required=True)
    bias_36 = _field.Field(types.Real, 'Bias factor #36 for bremsstrahlung specturm', required=True)
    bias_37 = _field.Field(types.Real, 'Bias factor #37 for bremsstrahlung specturm', required=True)
    bias_38 = _field.Field(types.Real, 'Bias factor #38 for bremsstrahlung specturm', required=True)
    bias_39 = _field.Field(types.Real, 'Bias factor #39 for bremsstrahlung specturm', required=True)
    bias_40 = _field.Field(types.Real, 'Bias factor #40 for bremsstrahlung specturm', required=True)
    bias_41 = _field.Field(types.Real, 'Bias factor #41 for bremsstrahlung specturm', required=True)
    bias_42 = _field.Field(types.Real, 'Bias factor #42 for bremsstrahlung specturm', required=True)
    bias_43 = _field.Field(types.Real, 'Bias factor #43 for bremsstrahlung specturm', required=True)
    bias_44 = _field.Field(types.Real, 'Bias factor #44 for bremsstrahlung specturm', required=True)
    bias_45 = _field.Field(types.Real, 'Bias factor #45 for bremsstrahlung specturm', required=True)
    bias_46 = _field.Field(types.Real, 'Bias factor #46 for bremsstrahlung specturm', required=True)
    bias_47 = _field.Field(types.Real, 'Bias factor #47 for bremsstrahlung specturm', required=True)
    bias_48 = _field.Field(types.Real, 'Bias factor #48 for bremsstrahlung specturm', required=True)
    bias_49 = _field.Field(types.Real, 'Bias factor #49 for bremsstrahlung specturm', required=True)
    materials = _field.Field.tuple(types.Integer, 'Material to bias', required=True, numeric=int)

    _REGEX = re.compile(
        rf'\Abbrem( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z',
        re.IGNORECASE,
    )
