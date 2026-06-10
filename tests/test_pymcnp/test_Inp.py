import pathlib

import pymcnp
from .. import classes


class Test_Inp(classes.Test_Nonterminal):
    element = pymcnp.Inp
    EXAMPLES_VALID = [
        (pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_11.inp').read_text(),
    ]
    EXAMPLES_INVALID = [
        'Vol Test\n1 0 2\n\n2 SO 1\n\nVOL 3.1 3.1\n',
        'Area Test\n1 0 2\n\n2 SO 1\n\nAREA 3.1 3.1\n',
        'hello',
    ]

    def test_nps_valid(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\n')
        inp.nps
        inp.nps = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nNPS 10\n'
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nNPS 200\n')
        inp.nps
        inp.nps = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nNPS 10\n'

    def test_seed_invalid(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\n')
        inp.seed
        inp.seed = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND SEED 10\n'
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND\n')
        inp.seed
        inp.seed = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND SEED 10\n'
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND GEN 1\n')
        inp.seed
        inp.seed = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND GEN 1 SEED 10\n'
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND GEN 1 SEED 200\n')
        inp.seed
        inp.seed = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND GEN 1 SEED 10\n'

    def test_vertical_format_valid(self) -> None:
        a, _ = pymcnp.Inp.from_file(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_42.inp')
        b, _ = self.element.from_mcnp(a.to_mcnp())
        assert a.to_mcnp() == b.to_mcnp()
