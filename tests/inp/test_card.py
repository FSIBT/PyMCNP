import pymcnp
from .. import _utils


class Test_Cell:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.Cell
        EXAMPLES_VALID = [
            '3 0 -1 2 -4 $ definition of cell 3',
            '5 0 #3',
            '5 0 #(-1 2 -4)',
            '5 0 (+1 : -2 : +4)',
            '2 3 -3.7 -1 IMP:N=2 IMP:P=4',
            '10 16 -4.2 1 -2 3 IMP:N=4 IMP:P=8 EXT:N=-0.4',
            '1 0 -17',
            '1 0 1 -2 -3 4 -5 6 fill=1',
            '2 0 -7 1 -3 8 u=1 fill=2 lat=1',
            '3 0 -11 u=-2',
            '4 0 11 u=2',
            '5 0 -1:2:3:-4:5:-6',
        ]


class Test_Comment:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.Comment
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.CommentBuilder
        EXAMPLES_VALID = [{'text': None}, {'text': 'a'}, {'text': 'a'}, {'text': _utils.STRING}]
        EXAMPLES_INVALID = []


class Test_Data:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.Data
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Surface:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.Surface
        EXAMPLES_VALID = [
            '1 PY 3',
            '3 K/Y 0 0 2 0.25 1',
            '11 GQ 1 0.25 0.75 0 -0.866 0 -12 -2 3.464 39',
            '11 7 CX 1',
            '12 X 7 5 3 2 4 3',
            '12 Y 1 2 1 3 3 4',
            '12 Y 3 0 4 1 5 0',
            '12 Z 1 0 2 1 3 4',
            '12 Z 2 1 3 4 5 9.380832',
            '5 rpp -2 0 -2 0 -1 1',
            '1 rpp 0 2 0 2 -1 1',
            '99 py -2',
            '17 4 RCC 0 0 0 0 12 0 5',
            '11 4 PX 5',
            '11 PY 4.1',
            '1 px 0',
            '2 px 50',
            '3 py 10',
            '4 py -10',
            '5 pz 5',
            '6 pz -5',
            '7 px 10',
            '8 py 0',
            '10 py 10',
            '11 s 5 5 0 4',
            '11 s 5 5 0 4',
        ]
        EXAMPLES_INVALID = []
