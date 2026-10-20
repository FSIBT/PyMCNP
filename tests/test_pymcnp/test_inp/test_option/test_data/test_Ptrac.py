import pymcnp
from ..... import classes


class Test_Ptrac(classes.Test_Nonterminal):
    element = pymcnp.inp.option.data.Ptrac
    EXAMPLES_VALID = [
        'buffer 1',
        'file asc',
        'flushnps 1',
        'max 1',
        'meph 1',
        'write pos',
        'coinc col',
        'event src',
        # 'filter 3.1,hello,3.1 3.1,hello,3.1 3.1,hello,3.1',
        'type @ @ @',
        'nps 1 1 1',
        'cell 1 1 1',
        'surface 1 1 1',
        'surface 3.1 3.2 3.3',
        'tally 1 1 1',
        'value 3.1',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]

    def test_macrobody_facets_survive_parsing(self) -> None:
        source = 'PTRAC FILE=ASC EVENT=SUR SURFACE=3.1 3.2 3.3 TYPE=P\n'
        card, rest = pymcnp.inp.card.data.Ptrac.from_mcnp(source)

        assert rest == '\n'
        assert card.to_mcnp() == source.rstrip('\n')
