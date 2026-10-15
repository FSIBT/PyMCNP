import pathlib


import pymcnp
from .. import consts
from .. import classes


class Test_Visualize:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Visualize
        EXAMPLES_VALID = [
            {'inpt': consts.ast.INP},
        ]
        EXAMPLES_INVALID = [{'inpt': None}]

    class Test_Methods:
        element = pymcnp.Visualize
        EXAMPLES = [{'inpt': consts.ast.INP}]

        def test_to_show_surfaces(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_show_surfaces()

        def test_to_show_cells(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_show_cells()

        def test_to_show_surface(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_show_surface('1')

        def test_to_show_cell(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_show_cell('1')

        def test_to_pdf_surfaces(self):
            path = pathlib.Path('hello.pdf')

            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_pdf_surfaces(path)

        def test_to_pdf_cells(self):
            path = pathlib.Path('hello.pdf')

            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_pdf_cells(path)

        def test_to_pdf_surface(self):
            path = pathlib.Path('hello.pdf')

            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_pdf_surface('1', path)

        def test_to_pdf_cell(self):
            path = pathlib.Path('hello.pdf')

            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_pdf_cell('1', path)


class Test_Visualize_Skip:
    INP = 'c title\n1 0 -1 imp:n=1\n2 0 1 -2 imp:n=1\n3 0 2 imp:n=0\n\n1 so 1\n2 so 2\n\nnps 1\n'

    @staticmethod
    def _count(plot):
        return len([actor for actor in plot.renderer.actors.values() if type(actor).__name__ in ('Actor', 'Volume')])

    def test_surfaces_skip_removes_the_surface(self):
        visualize = pymcnp.Visualize(pymcnp.Inp.from_mcnp(self.INP))

        assert self._count(visualize.to_show_surfaces(skip=(2,))) == self._count(visualize.to_show_surfaces()) - 1

    def test_cells_skip_removes_the_cell(self):
        visualize = pymcnp.Visualize(pymcnp.Inp.from_mcnp(self.INP))

        assert self._count(visualize.to_show_cells(skip=(2,))) < self._count(visualize.to_show_cells())
