import re

from . import _field
from . import _card
from .. import types


class Tsplt(_field.Fields, _card.Card):
    """
    Represents INP `tsplt` cards.
    """

    _KEYWORD = 'tsplt'

    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    ratio_1 = _field.Field(types.Real, 'Splitting/roulette ratio #1')
    time_1 = _field.Field(types.Real, 'Splitting/roulette time #1')
    ratio_2 = _field.Field(types.Real, 'Splitting/roulette ratio #2')
    time_2 = _field.Field(types.Real, 'Splitting/roulette time #2')
    ratio_3 = _field.Field(types.Real, 'Splitting/roulette ratio #3')
    time_3 = _field.Field(types.Real, 'Splitting/roulette time #3')
    ratio_4 = _field.Field(types.Real, 'Splitting/roulette ratio #4')
    time_4 = _field.Field(types.Real, 'Splitting/roulette time #4')
    ratio_5 = _field.Field(types.Real, 'Splitting/roulette ratio #5')
    time_5 = _field.Field(types.Real, 'Splitting/roulette time #5')
    ratio_6 = _field.Field(types.Real, 'Splitting/roulette ratio #6')
    time_6 = _field.Field(types.Real, 'Splitting/roulette time #6')
    ratio_7 = _field.Field(types.Real, 'Splitting/roulette ratio #7')
    time_7 = _field.Field(types.Real, 'Splitting/roulette time #7')
    ratio_8 = _field.Field(types.Real, 'Splitting/roulette ratio #8')
    time_8 = _field.Field(types.Real, 'Splitting/roulette time #8')
    ratio_9 = _field.Field(types.Real, 'Splitting/roulette ratio #9')
    time_9 = _field.Field(types.Real, 'Splitting/roulette time #9')
    ratio_10 = _field.Field(types.Real, 'Splitting/roulette ratio #10')
    time_10 = _field.Field(types.Real, 'Splitting/roulette time #10')
    ratio_11 = _field.Field(types.Real, 'Splitting/roulette ratio #11')
    time_11 = _field.Field(types.Real, 'Splitting/roulette time #11')
    ratio_12 = _field.Field(types.Real, 'Splitting/roulette ratio #12')
    time_12 = _field.Field(types.Real, 'Splitting/roulette time #12')
    ratio_13 = _field.Field(types.Real, 'Splitting/roulette ratio #13')
    time_13 = _field.Field(types.Real, 'Splitting/roulette time #13')
    ratio_14 = _field.Field(types.Real, 'Splitting/roulette ratio #14')
    time_14 = _field.Field(types.Real, 'Splitting/roulette time #14')
    ratio_15 = _field.Field(types.Real, 'Splitting/roulette ratio #15')
    time_15 = _field.Field(types.Real, 'Splitting/roulette time #15')
    ratio_16 = _field.Field(types.Real, 'Splitting/roulette ratio #16')
    time_16 = _field.Field(types.Real, 'Splitting/roulette time #16')
    ratio_17 = _field.Field(types.Real, 'Splitting/roulette ratio #17')
    time_17 = _field.Field(types.Real, 'Splitting/roulette time #17')
    ratio_18 = _field.Field(types.Real, 'Splitting/roulette ratio #18')
    time_18 = _field.Field(types.Real, 'Splitting/roulette time #18')
    ratio_19 = _field.Field(types.Real, 'Splitting/roulette ratio #19')
    time_19 = _field.Field(types.Real, 'Splitting/roulette time #19')
    ratio_20 = _field.Field(types.Real, 'Splitting/roulette ratio #20')
    time_20 = _field.Field(types.Real, 'Splitting/roulette time #20')

    _REGEX = re.compile(
        rf'\Atsplt:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
