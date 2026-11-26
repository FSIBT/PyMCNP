import re
import typing

import pytest

import pymcnp
from pymcnp import abc
from pymcnp.abc.Symbol import _parse, _parse_at


def test_terminal_at():
    value, end = abc.Terminal[r'\d+']._from_mcnp_at('ab12cd', 2)

    assert value == '12'
    assert type(value) is abc.Terminal[r'\d+']
    assert end == 4


def test_terminal_at_failure_reports_source_from_position():
    with pytest.raises(abc.Error) as error:
        abc.Terminal[r'\d+']._from_mcnp_at('ab' + 'x' * 300, 2)

    assert str(error.value) == "Expected Terminal[r'(\\d+)']\n source[:200]='" + 'x' * 200 + "'"


def test_terminal_error_text_unchanged():
    with pytest.raises(abc.Error) as error:
        abc.Terminal[r'\d+'].from_mcnp('x' * 300)

    assert str(error.value) == "Expected Terminal[r'(\\d+)']\n source[:200]='" + 'x' * 200 + "'"


def test_nonterminal_trailing_space_given_back():
    card, remainder = pymcnp.inp.card.data.Nps.from_mcnp('nps 10   \nrest')

    assert card.to_mcnp() == 'nps 10'
    assert remainder == '   \nrest'
    assert card.spaces == {'keyword': ' '}

    card, remainder = pymcnp.inp.card.data.Nps.from_mcnp('nps 10 20   \nrest')

    assert card.to_mcnp() == 'nps 10 20'
    assert remainder == '   \nrest'


def test_nonterminal_at():
    card, end = pymcnp.inp.card.data.Nps._from_mcnp_at('xx nps 10 20   \nrest', 3)

    assert card.to_mcnp() == 'nps 10 20'
    assert end == len('xx nps 10 20')


def test_nonterminal_error_text_at_position():
    with pytest.raises(abc.Error) as error:
        pymcnp.inp.card.data.Nps._from_mcnp_at('xx nps x', 3)

    assert str(error.value) == "Expected ``Nps.npp``.\nExpected Terminal[r'([-+]?(?:(?:\\d+(?:[eE][-+]?\\d+)?)|(?:[eE][-+]?\\d+)))']\n source[:200]='x'"


def test_multiform_nonterminal_error_text_at_position():
    with pytest.raises(abc.Error) as error:
        pymcnp.inp.card.Data._from_mcnp_at('xx nps x', 3)

    assert str(error.value).startswith("Expected ``Data``.\nExpected ``Disable.keyword``.\nExpected Terminal[r'(DISABLE)']\n source[:200]='nps x'")


def test_array_space_given_back():
    array, remainder = abc.Array[abc.Terminal[r'\d+'], None].from_mcnp('1 2 3 x')

    assert list(array) == ['1', '2', '3']
    assert array.spaces == [' ', ' ']
    assert remainder == ' x'


def test_array_at():
    array, end = abc.Array[abc.Terminal[r'\d+'], None]._from_mcnp_at('x 1 2 3 x', 2)

    assert list(array) == ['1', '2', '3']
    assert end == len('x 1 2 3')


def test_longest_match_tie_first_kind():
    first = abc.Terminal[r'[a-z]+']
    second = abc.Terminal[r'[a-c]+']

    value, end = _parse_at((first, second), '  abc  ', 2)
    assert type(value) is first
    assert end == 5

    value, end = _parse_at((second, first), '  abc  ', 2)
    assert type(value) is second
    assert end == 5


def test_longest_match_largest_end():
    short = abc.Terminal[r'a']
    long = abc.Terminal[r'a+']

    value, end = _parse_at((short, long), 'xaaa', 1)
    assert type(value) is long
    assert end == 4


def test_parse_at_raises_first_error():
    with pytest.raises(abc.Error) as error:
        _parse_at((abc.Terminal[r'a'], abc.Terminal[r'b']), 'xc', 1)

    assert str(error.value) == "Expected Terminal[r'(a)']\n source[:200]='c'"


def test_parse_wrapper_returns_remainder():
    value, remainder = _parse((abc.Terminal[r'a'], abc.Terminal[r'a+']), 'aab')

    assert value == 'aa'
    assert remainder == 'b'


class _Override(abc.Nonterminal):
    """
    Nonterminal that overrides only ``from_mcnp``.
    """

    word: typing.Annotated[abc.Terminal, r'[a-z]+']

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        return super().from_mcnp(source.replace('!', 'x', 1))


class _Mixin:
    """
    Mixin that overrides ``from_mcnp``, like ``abc.symbol.WithMcnpIter``.
    """

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Any, str]:
        return super().from_mcnp(source.replace('!', 'x', 1))  # ty: ignore[unresolved-attribute]


class _Mixed(_Mixin, abc.Nonterminal):
    """
    Nonterminal that inherits an override of ``from_mcnp`` from a mixin.
    """

    word: typing.Annotated[abc.Terminal, r'[a-z]+']


class _Holder(abc.Nonterminal):
    """
    Nonterminal with a field whose kind overrides only ``from_mcnp``.
    """

    _space = (abc.Terminal[r' +'],)

    number: typing.Annotated[abc.Terminal, r'\d+']
    word: _Override


def test_from_mcnp_override_reached_as_field_kind():
    holder, remainder = _Holder.from_mcnp('12 a!c rest')

    assert holder.word.word == 'axc'
    assert remainder == ' rest'


def test_from_mcnp_override_calls_parent_parser():
    value, remainder = _Override.from_mcnp('a!c rest')

    assert value.word == 'axc'
    assert remainder == ' rest'

    value, end = _Override._from_mcnp_at('12 a!c rest', 3)

    assert value.word == 'axc'
    assert end == 6


def test_from_mcnp_override_inherited_from_mixin():
    value, remainder = _Mixed.from_mcnp('a!c rest')

    assert type(value) is _Mixed
    assert value.word == 'axc'
    assert remainder == ' rest'

    value, end = _Mixed._from_mcnp_at('12 a!c rest', 3)

    assert value.word == 'axc'
    assert end == 6


def test_symbol_without_parser_raises():
    class Bare(abc.Symbol):
        def to_mcnp(self) -> str:
            return ''

    # Bare is a complete symbol that only lacks a parser.
    assert Bare().to_mcnp() == ''

    with pytest.raises(NotImplementedError):
        Bare.from_mcnp('a')

    with pytest.raises(NotImplementedError):
        Bare._from_mcnp_at('a', 0)


def test_inp_override_still_preprocesses():
    inp, _ = pymcnp.Inp.from_mcnp('title\n1 0 -1\n\n1 so 1\n\nnps 1 2r\n')

    assert inp.data[0].to_mcnp() == 'nps 1 1 1'


# Step 2 audit: every Terminal pattern that depends on the surrounding source (``\Z`` and lookaheads
# reaching it); none use ``^``, ``\A``, ``\b`` or lookbehinds. Matching at a position must agree with
# matching the slice.
AUDITED = [
    (r' *(?:\$.*)?(?:\n|\Z)', 'ab  $ c', 2),
    (r' *(?:\$.*)?(?:\n|\Z)', 'ab  \nc', 2),
    (r'.+(?=\n|\Z)', 'ab cd', 1),
    (r'.+?(?=\n|\Z)', 'ab cd\nx', 1),
    (r'[\s\S]*?(?=\n1|\Z)', 'ab c\n1x', 1),
    (r'[\s\S]*?(?=\n[^ ]{1,5}|\Z)', 'ab c', 1),
    (
        r'(?!\n \*{119}\n\n dump no\.(?:(?!\n1\w|\n \*{119})[\s\S])*\n mcnp     version [^\n]*\n?\Z)[\s\S][^\n]*(?:\n(?!1\w| \*{119})[^\n]*)*',
        'xx\n ' + '*' * 119 + '\n\n dump no. 1\n mcnp     version 6\n',
        2,
    ),
    (r'[^\s$](?:[^$\n]*[^\s$])?(?:\n {1,5}[^\s$](?:[^$\n]*[^\s$])?)*', 'x ab\n  cd $ e', 2),
]


@pytest.mark.parametrize('pattern, source, pos', AUDITED)
def test_audited_pattern_position_matches_slice(pattern, source, pos):
    kind = abc.Terminal[pattern]
    expected = re.compile(f'({pattern})', re.IGNORECASE).match(source[pos:])

    try:
        value, end = kind._from_mcnp_at(source, pos)
    except abc.Error:
        assert expected is None
    else:
        assert expected is not None
        assert value == expected[0]
        assert end == pos + expected.end()
