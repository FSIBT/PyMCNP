import pathlib

import pymcnp
from .. import consts
from .. import classes


class Test_Inp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Inp
        EXAMPLES_VALID = [
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SO, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
            {
                'title': consts.ast.types.STRING,
                'cells': [consts.ast.inp.CELL, consts.ast.inp.COMMENT, consts.ast.inp.LIKE],
                'surfaces': [consts.ast.inp.SO, consts.ast.inp.COMMENT],
                'data': [consts.ast.inp.VOL, consts.ast.inp.COMMENT],
                'message': consts.ast.types.STRING,
                'other': consts.ast.types.STRING,
            },
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SO, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': None,
                'other': consts.string.types.STRING,
            },
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SO, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'title': None,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SO, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
            {
                'title': consts.string.types.STRING,
                'cells': None,
                'surfaces': [consts.string.inp.SO, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': None,
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SO, consts.string.inp.COMMENT],
                'data': None,
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
            {
                'title': consts.string.types.STRING,
                'cells': ['1 0 1'],
                'surfaces': [consts.string.inp.SO, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
        ]

    class Test_Properties:
        EXAMPLES = [
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SO, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
        ]

        def test_nps(self):
            for example in self.EXAMPLES:
                inp = pymcnp.Inp(**example)
                _ = inp.nps

                inp.nps = '1e3'
                inp.nps = 10
                inp.nps = pymcnp.types.Integer(1234938)
                _ = inp.nps

        def test_seed(self):
            for example in self.EXAMPLES:
                inp = pymcnp.Inp(**example)
                _ = inp.seed

                save = inp.data

                inp.seed = '11'
                inp.seed = 11
                inp.seed = pymcnp.types.Integer(11)
                _ = inp.seed

                inp.data = save
                inp.data = [*inp.data, pymcnp.inp.Rand()]

                inp.seed = '11'
                inp.seed = 11
                inp.seed = pymcnp.types.Integer(11)
                _ = inp.seed

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.Inp
        EXAMPLES_VALID = [consts.string.INP]
        EXAMPLES_INVALID = ['hello']

    class Test_File(classes.Test_File):
        element = pymcnp.Inp
        EXAMPLES_VALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp').glob('valid*.inp'),
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp').glob('example*.inp'),
        ]
        EXAMPLES_INVALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp').glob('invalid*.inp'),
        ]


class Test_Inp_Issue_7:
    SOURCE = """MCNP Test Model for MOAA
C cells
1 1 20
         -1000  $ dollar comment
        imp:n,p=1 U=350 trcl=5
99 0
      1010
     imp:n,p=0

C surfaces
1000 SO 1
1010 SO 3

C data
C UO2 5 atpt enriched
m1        92235.80c           5 &
92238.80c          95
C Iron
m2        26054.80c        5.85
          plib= 80p
          26056           91.75
          26057        2.12 $ trailing comment
          26058.80c        0.28
C water
m3        1001.80c           2
           8016.80c           1
           plib=84p
MT3 lwtr.23t h-zr.20t h/zr.28t
mode n p
"""

    def test_library_keyword_between_substances_parses(self):
        written = pymcnp.Inp.from_mcnp(self.SOURCE).to_mcnp()

        assert 'm2 026054.80c 5.85 026056 91.75 026057 2.12 026058.80c 0.28 plib 80p' in ' '.join(written.replace('&', '').split())
        assert 'plib 84p' in written

    def test_written_issue_input_is_stable(self):
        written = pymcnp.Inp.from_mcnp(self.SOURCE).to_mcnp()

        assert pymcnp.Inp.from_mcnp(written).to_mcnp() == written
