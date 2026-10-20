import pymcnp
from .... import classes


class Test_Particle(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.Particle
    EXAMPLES_VALID = [
        '@,#',
        '_',
        '#',
        'n',
        'P,n',
        'P,e,!',
    ]
    EXAMPLES_INVALID = [
        ':',
    ]

    def test_particle_list_does_not_swallow_a_following_keyword(self) -> None:
        particle, remainder = pymcnp.inp.literal.Particle.from_mcnp('P WRITE=ALL')

        assert particle == 'P'
        assert remainder == ' WRITE=ALL'

    def test_particle_followed_by_equals_still_parses(self) -> None:
        particle, remainder = pymcnp.inp.literal.Particle.from_mcnp('n=1')

        assert particle == 'n'
        assert remainder == '=1'
