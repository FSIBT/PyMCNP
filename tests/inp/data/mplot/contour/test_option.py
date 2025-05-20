import pymcnp
from ..... import _utils


class Test_Pct:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Pct
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.contour.PctBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Lin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Lin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.contour.LinBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Log:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Log
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.contour.LogBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_All:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.All
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.contour.AllBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Noall:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Noall
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.contour.NoallBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Line:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Line
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.contour.LineBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Noline:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Noline
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.contour.NolineBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Color:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Color
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.contour.ColorBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Nocolor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Nocolor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.contour.NocolorBuilder
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []
