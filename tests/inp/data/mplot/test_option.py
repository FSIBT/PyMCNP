import pymcnp
from .... import _utils


class Test_Term:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Term
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.TermBuilder
        EXAMPLES_VALID = [{'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]


class Test_File:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.File
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.FileBuilder
        EXAMPLES_VALID = [
            {'aa': None},
            {'aa': 'all'},
            {'aa': 'all'},
            {'aa': pymcnp.utils.types.String('all')},
        ]
        EXAMPLES_INVALID = []


class Test_Coplot:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Coplot
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.CoplotBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Freq:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Freq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.FreqBuilder
        EXAMPLES_VALID = [{'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]


class Test_Return:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Return
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ReturnBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Plot:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Plot
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.PlotBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Pause:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Pause
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.PauseBuilder
        EXAMPLES_VALID = [{'n': None}, {'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = []


class Test_End:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.End
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.EndBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Options:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Options
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.OptionsBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Help:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Help
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.HelpBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Status:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Status
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.StatusBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Printal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Printal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.PrintalBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Iptal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Iptal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.IptalBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Printpts:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Printpts
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.PrintptsBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Runtpe:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Runtpe
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.RuntpeBuilder
        EXAMPLES_VALID = [
            {'filename': 'a', 'n': None},
            {'filename': 'a', 'n': '1'},
            {'filename': 'a', 'n': 1},
            {'filename': pymcnp.utils.types.String('a'), 'n': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [{'filename': None, 'n': '1'}]


class Test_Dump:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Dump
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.DumpBuilder
        EXAMPLES_VALID = [{'n': None}, {'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = []


class Test_Wmctal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Wmctal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.WmctalBuilder
        EXAMPLES_VALID = [
            {'filename': 'a'},
            {'filename': pymcnp.utils.types.String('a')},
        ]
        EXAMPLES_INVALID = [{'filename': None}]


class Test_Rmctal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Rmctal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.RmctalBuilder
        EXAMPLES_VALID = [
            {'filename': 'a'},
            {'filename': 'a'},
            {'filename': pymcnp.utils.types.String('a')},
        ]
        EXAMPLES_INVALID = [{'filename': None}]


class Test_Tally:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Tally
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.TallyBuilder
        EXAMPLES_VALID = [{'n': None}, {'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = []


class Test_Pert:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Pert
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.PertBuilder
        EXAMPLES_VALID = [{'n': None}, {'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = []


class Test_Lethargy:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Lethargy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.LethargyBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Nonorm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Nonorm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.NonormBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Factor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Factor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.FactorBuilder
        EXAMPLES_VALID = [
            {'a': 'x', 'f': '1.0', 's': '1.0'},
            {'a': 'x', 'f': '1.0', 's': None},
            {'a': 'x', 'f': 1.0, 's': 1.0},
            {'a': pymcnp.utils.types.String('x'), 'f': _utils.REAL, 's': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'a': None, 'f': '1.0', 's': '1.0'},
            {'a': 'x', 'f': None, 's': '1.0'},
        ]


class Test_Reset:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Reset
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ResetBuilder
        EXAMPLES_VALID = [
            {'aa': None},
            {'aa': 'all'},
            {'aa': 'all'},
            {'aa': pymcnp.utils.types.String('all')},
        ]
        EXAMPLES_INVALID = []


class Test_Title:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Title
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.TitleBuilder
        EXAMPLES_VALID = [
            {'n': '1', 'aa': 'a'},
            {'n': 1, 'aa': 'a'},
            {'n': _utils.INTEGER, 'aa': pymcnp.utils.types.String('a')},
        ]
        EXAMPLES_INVALID = [{'n': None, 'aa': 'a'}, {'n': '1', 'aa': None}]


class Test_Below:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Below
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.BelowBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Subtitle:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Subtitle
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.SubtitleBuilder
        EXAMPLES_VALID = [
            {'x': '1', 'y': '1', 'aa': 'a'},
            {'x': 1, 'y': 1, 'aa': 'a'},
            {'x': _utils.INTEGER, 'y': _utils.INTEGER, 'aa': pymcnp.utils.types.String('a')},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': '1', 'aa': 'a'},
            {'x': '1', 'y': None, 'aa': 'a'},
            {'x': '1', 'y': '1', 'aa': None},
        ]


class Test_Xtitle:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xtitle
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.XtitleBuilder
        EXAMPLES_VALID = [{'aa': 'a'}, {'aa': 'a'}, {'aa': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'aa': None}]


class Test_Ytitle:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Ytitle
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.YtitleBuilder
        EXAMPLES_VALID = [{'aa': 'a'}, {'aa': 'a'}, {'aa': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'aa': None}]


class Test_Ztitle:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Ztitle
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ZtitleBuilder
        EXAMPLES_VALID = [{'aa': 'a'}, {'aa': 'a'}, {'aa': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'aa': None}]


class Test_Label:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Label
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.LabelBuilder
        EXAMPLES_VALID = [{'aa': 'a'}, {'aa': 'a'}, {'aa': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'aa': None}]


class Test_Free:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Free
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.FreeBuilder
        EXAMPLES_VALID = [
            {'x': 'f', 'y': 'f', 'option': None},
            {'x': 'f', 'y': 'f', 'option': None},
            {
                'x': pymcnp.utils.types.String('f'),
                'y': pymcnp.utils.types.String('f'),
                'option': None,
            },
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': 'f', 'option': None},
            {'x': 'f', 'y': None, 'option': None},
        ]


class Test_Fixed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Fixed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.FixedBuilder
        EXAMPLES_VALID = [
            {'q': 'f', 'n': '1'},
            {'q': 'f', 'n': 1},
            {'q': pymcnp.utils.types.String('f'), 'n': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [{'q': None, 'n': '1'}, {'q': 'f', 'n': None}]


class Test_Set:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Set
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.SetBuilder
        EXAMPLES_VALID = [
            {'f': '1', 'd': '1', 'u': '1', 's': '1', 'm': '1', 'c': '1', 'e': '1', 't': '1'},
            {'f': 1, 'd': 1, 'u': 1, 's': 1, 'm': 1, 'c': 1, 'e': 1, 't': 1},
            {
                'f': _utils.INTEGER,
                'd': _utils.INTEGER,
                'u': _utils.INTEGER,
                's': _utils.INTEGER,
                'm': _utils.INTEGER,
                'c': _utils.INTEGER,
                'e': _utils.INTEGER,
                't': _utils.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {'f': None, 'd': '1', 'u': '1', 's': '1', 'm': '1', 'c': '1', 'e': '1', 't': '1'},
            {'f': '1', 'd': None, 'u': '1', 's': '1', 'm': '1', 'c': '1', 'e': '1', 't': '1'},
            {'f': '1', 'd': '1', 'u': None, 's': '1', 'm': '1', 'c': '1', 'e': '1', 't': '1'},
            {'f': '1', 'd': '1', 'u': '1', 's': None, 'm': '1', 'c': '1', 'e': '1', 't': '1'},
            {'f': '1', 'd': '1', 'u': '1', 's': '1', 'm': None, 'c': '1', 'e': '1', 't': '1'},
            {'f': '1', 'd': '1', 'u': '1', 's': '1', 'm': '1', 'c': None, 'e': '1', 't': '1'},
            {'f': '1', 'd': '1', 'u': '1', 's': '1', 'm': '1', 'c': '1', 'e': None, 't': '1'},
            {'f': '1', 'd': '1', 'u': '1', 's': '1', 'm': '1', 'c': '1', 'e': '1', 't': None},
        ]


class Test_Tfc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Tfc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.TfcBuilder
        EXAMPLES_VALID = [{'x': 'a'}, {'x': 'a'}, {'x': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'x': None}]


class Test_Kcode:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Kcode
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.KcodeBuilder
        EXAMPLES_VALID = [{'i': '1'}, {'i': 1}, {'i': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'i': None}]


class Test_Xs_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xs_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.XsBuilder_0
        EXAMPLES_VALID = [{'m': '1'}, {'m': 1}, {'m': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'m': None}]


class Test_Xs_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xs_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.XsBuilder_1
        EXAMPLES_VALID = [{'m': '001001'}, {'m': _utils.ZAID}]
        EXAMPLES_INVALID = [{'m': None}]


class Test_Xs_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xs_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.XsBuilder_2
        EXAMPLES_VALID = [{'m': '?'}, {'m': pymcnp.utils.types.String('?')}]
        EXAMPLES_INVALID = [{'m': None}]


class Test_Mt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Mt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.MtBuilder
        EXAMPLES_VALID = [{'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]


class Test_Par:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Par
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ParBuilder
        EXAMPLES_VALID = [{'particle': 'n'}, {'particle': 'n'}, {'particle': _utils.DESIGNATOR}]
        EXAMPLES_INVALID = [{'particle': None}]


class Test_Linlin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Linlin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.LinlinBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Linlog:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Linlog
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.LinlogBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Loglin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Loglin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.LoglinBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Loglog:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Loglog
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.LoglogBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Xlims:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xlims
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.XlimsBuilder
        EXAMPLES_VALID = [
            {'min': '1.0', 'max': '2.0', 'nsteps': '1.0'},
            {'min': '1.0', 'max': '2.0', 'nsteps': None},
            {'min': 1.0, 'max': 2.0, 'nsteps': 1.0},
            {'min': _utils.REAL, 'max': pymcnp.utils.types.Real(2.0), 'nsteps': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'min': None, 'max': '2.0', 'nsteps': '1.0'},
            {'min': '1.0', 'max': None, 'nsteps': '1.0'},
        ]


class Test_Ylims:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Ylims
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.YlimsBuilder
        EXAMPLES_VALID = [
            {'min': '1.0', 'max': '2.0', 'nsteps': '1.0'},
            {'min': '1.0', 'max': '2.0', 'nsteps': None},
            {'min': 1.0, 'max': 2.0, 'nsteps': 1.0},
            {'min': _utils.REAL, 'max': pymcnp.utils.types.Real(2.0), 'nsteps': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'min': None, 'max': '2.0', 'nsteps': '1.0'},
            {'min': '1.0', 'max': None, 'nsteps': '1.0'},
        ]


class Test_Scales:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Scales
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ScalesBuilder
        EXAMPLES_VALID = [{'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]


class Test_Hist:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Hist
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.HistBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Plinear:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Plinear
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.PlinearBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Spline:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Spline
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.SplineBuilder
        EXAMPLES_VALID = [{'x': None}, {'x': '1.0'}, {'x': 1.0}, {'x': _utils.REAL}]
        EXAMPLES_INVALID = []


class Test_Bar:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Bar
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.BarBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Noerrbar:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Noerrbar
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.NoerrbarBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Thick:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Thick
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ThickBuilder
        EXAMPLES_VALID = [{'x': '1.0'}, {'x': 1.0}, {'x': _utils.REAL}]
        EXAMPLES_INVALID = [{'x': None}]


class Test_Thin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Thin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ThinBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Legend:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Legend
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.LegendBuilder
        EXAMPLES_VALID = [
            {'x': '1.0', 'y': '1.0'},
            {'x': None, 'y': '1.0'},
            {'x': '1.0', 'y': None},
            {'x': 1.0, 'y': 1.0},
            {'x': _utils.REAL, 'y': _utils.REAL},
        ]
        EXAMPLES_INVALID = []


class Test_Contour:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Contour
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ContourBuilder
        EXAMPLES_VALID = [
            {'cmin': '1.0', 'cmax': '1.0', 'cstep': '1.0', 'options': None},
            {'cmin': '1.0', 'cmax': '1.0', 'cstep': '1.0', 'options': None},
            {'cmin': 1.0, 'cmax': 1.0, 'cstep': 1.0, 'options': None},
            {'cmin': _utils.REAL, 'cmax': _utils.REAL, 'cstep': _utils.REAL, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'cmin': None, 'cmax': '1.0', 'cstep': '1.0', 'options': None},
            {'cmin': '1.0', 'cmax': None, 'cstep': '1.0', 'options': None},
            {'cmin': '1.0', 'cmax': '1.0', 'cstep': None, 'options': None},
        ]


class Test_Wash:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Wash
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.WashBuilder
        EXAMPLES_VALID = [{'aa': 'on'}, {'aa': 'on'}, {'aa': pymcnp.utils.types.String('on')}]
        EXAMPLES_INVALID = [{'aa': None}]


class Test_Fmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Fmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.FmeshBuilder
        EXAMPLES_VALID = [{'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]


class Test_Fmrelerr:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Fmrelerr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.FmrelerrBuilder
        EXAMPLES_VALID = [{'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]


class Test_Zlev:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Zlev
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ZlevBuilder
        EXAMPLES_VALID = [{'n': ['a']}, {'n': [_utils.STRING]}]
        EXAMPLES_INVALID = [{'n': None}]


class Test_Ebin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Ebin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.EbinBuilder
        EXAMPLES_VALID = [{'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]


class Test_Tbin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Tbin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.TbinBuilder
        EXAMPLES_VALID = [{'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]


class Test_Cop:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Cop
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.CopBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Tal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Tal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.TalBuilder
        EXAMPLES_VALID = [{'n': '1'}, {'n': 1}, {'n': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]
