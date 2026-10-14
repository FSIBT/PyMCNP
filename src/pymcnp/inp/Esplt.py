import re

from . import _field
from . import _card
from .. import types


class Esplt(_field.Fields, _card.Card):
    """
    Represents INP `esplt` cards.
    """

    _KEYWORD = 'esplt'

    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    ratio_1 = _field.Field(types.Real, 'Splitting/roulette ratio #1')
    energy_1 = _field.Field(types.Real, 'Splitting/roulette energy #1')
    ratio_2 = _field.Field(types.Real, 'Splitting/roulette ratio #2')
    energy_2 = _field.Field(types.Real, 'Splitting/roulette energy #2')
    ratio_3 = _field.Field(types.Real, 'Splitting/roulette ratio #3')
    energy_3 = _field.Field(types.Real, 'Splitting/roulette energy #3')
    ratio_4 = _field.Field(types.Real, 'Splitting/roulette ratio #4')
    energy_4 = _field.Field(types.Real, 'Splitting/roulette energy #4')
    ratio_5 = _field.Field(types.Real, 'Splitting/roulette ratio #5')
    energy_5 = _field.Field(types.Real, 'Splitting/roulette energy #5')
    ratio_6 = _field.Field(types.Real, 'Splitting/roulette ratio #6')
    energy_6 = _field.Field(types.Real, 'Splitting/roulette energy #6')
    ratio_7 = _field.Field(types.Real, 'Splitting/roulette ratio #7')
    energy_7 = _field.Field(types.Real, 'Splitting/roulette energy #7')
    ratio_8 = _field.Field(types.Real, 'Splitting/roulette ratio #8')
    energy_8 = _field.Field(types.Real, 'Splitting/roulette energy #8')
    ratio_9 = _field.Field(types.Real, 'Splitting/roulette ratio #9')
    energy_9 = _field.Field(types.Real, 'Splitting/roulette energy #9')
    ratio_10 = _field.Field(types.Real, 'Splitting/roulette ratio #10')
    energy_10 = _field.Field(types.Real, 'Splitting/roulette energy #10')
    ratio_11 = _field.Field(types.Real, 'Splitting/roulette ratio #11')
    energy_11 = _field.Field(types.Real, 'Splitting/roulette energy #11')
    ratio_12 = _field.Field(types.Real, 'Splitting/roulette ratio #12')
    energy_12 = _field.Field(types.Real, 'Splitting/roulette energy #12')
    ratio_13 = _field.Field(types.Real, 'Splitting/roulette ratio #13')
    energy_13 = _field.Field(types.Real, 'Splitting/roulette energy #13')
    ratio_14 = _field.Field(types.Real, 'Splitting/roulette ratio #14')
    energy_14 = _field.Field(types.Real, 'Splitting/roulette energy #14')
    ratio_15 = _field.Field(types.Real, 'Splitting/roulette ratio #15')
    energy_15 = _field.Field(types.Real, 'Splitting/roulette energy #15')
    ratio_16 = _field.Field(types.Real, 'Splitting/roulette ratio #16')
    energy_16 = _field.Field(types.Real, 'Splitting/roulette energy #16')
    ratio_17 = _field.Field(types.Real, 'Splitting/roulette ratio #17')
    energy_17 = _field.Field(types.Real, 'Splitting/roulette energy #17')
    ratio_18 = _field.Field(types.Real, 'Splitting/roulette ratio #18')
    energy_18 = _field.Field(types.Real, 'Splitting/roulette energy #18')
    ratio_19 = _field.Field(types.Real, 'Splitting/roulette ratio #19')
    energy_19 = _field.Field(types.Real, 'Splitting/roulette energy #19')
    ratio_20 = _field.Field(types.Real, 'Splitting/roulette ratio #20')
    energy_20 = _field.Field(types.Real, 'Splitting/roulette energy #20')

    _REGEX = re.compile(
        rf'\Aesplt:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
