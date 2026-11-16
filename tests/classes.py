import os
import pathlib
import collections

import pymcnp


class Test_FromMcnp:
    element: pymcnp.abc.Nonterminal

    EXAMPLES_FROM_MCNP_VALID: collections.abc.Sequence[str] = []
    EXAMPLES_FROM_MCNP_INVALID: collections.abc.Sequence[str] = []

    def test_from_mcnp_valid(self) -> None:
        """
        Tests `EXAMPLES_FROM_MCNP_VALID` on `from_mcnp` and `to_mcnp`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)

            a, source = self.element.from_mcnp(example)
            b, source = self.element.from_mcnp(a.to_mcnp())
            assert a.to_mcnp() == b.to_mcnp()
            assert example == a.to_mcnp()

    def test_from_mcnp_invalid(self) -> None:
        """
        Tests `EXAMPLES_FROM_MCNP_INVALID` on `from_mcnp`.
        """

        for example in self.EXAMPLES_FROM_MCNP_INVALID:
            print(example)

            try:
                _, source = self.element.from_mcnp(example)
                assert source
            except pymcnp.abc.Error:
                assert True


class Test_FromFile(Test_FromMcnp):
    element: pymcnp.abc.Nonterminal

    EXAMPLES_FROM_FILE_VALID: collections.abc.Sequence[str] = []
    EXAMPLES_FROM_FILE_INVALID: collections.abc.Sequence[str] = []

    def test_from_file_valid(self) -> None:
        """
        Tests `EXAMPLES_FROM_FILE_VALID` on `from_file`.
        """

        for example in self.EXAMPLES_FROM_FILE_VALID:
            print(example)

            a, _ = self.element.from_file(example)
            b, _ = self.element.from_mcnp(example.read_text())
            assert a == b

    def test_from_file_invalid(self) -> None:
        """
        Tests `EXAMPLES_FROM_FILE_INVALID` on `from_file`.
        """

        for example in self.EXAMPLES_FROM_FILE_INVALID:
            print(example)

            try:
                _, source = self.element.from_file(example)
                assert source
            except pymcnp.abc.Error:
                assert True

    def test_to_file(self) -> None:
        """
        Tests `EXAMPLES_FROM_FILE_VALID` on `to_file`.
        """

        for example in self.EXAMPLES_FROM_FILE_VALID:
            print(example)

            a, _ = self.element.from_file(example)
            a.to_file(pathlib.Path(os.devnull))


class Test_ToDataframe:
    element: pymcnp.abc.Nonterminal

    EXAMPLES_TO_DATAFRAME: list[pathlib.Path | str] = []

    def test_to_dataframe(self) -> None:
        """
        Tests `to_dataframe` on EXAMPLES_TO_DATAFRAME`.
        """

        for example in self.EXAMPLES_TO_DATAFRAME:
            print(example)

            if issubclass(self.element, pymcnp.abc.File):
                element, _ = self.element.from_file(example)
            else:
                element, _ = self.element.from_mcnp(example)

            _ = element.to_dataframe()


class FileWithMcnpIter(pymcnp.abc.file.WithMcnpIter, pymcnp.abc.File): ...


W = typing.TypeVar('W', bound=FileWithMcnpIter)


class Test_FromFileIter(Test_FromFile[W]):
    element: type[W]

    def test_from_file_iter_valid(self) -> None:
        """
        Tests `EXAMPLES_FROM_FILE_VALID` on `from_mcnp` and `to_file_iter`.
        """

        for example in self.EXAMPLES_FROM_FILE_VALID:
            print(example)

            generator = self.element.from_file_iter(example, returning=False)
            for _ in generator:
                pass


class SymbolWithMcnpIter(pymcnp.abc.symbol.WithMcnpIter, pymcnp.abc.Symbol): ...


X = typing.TypeVar('X', bound=SymbolWithMcnpIter)


class Test_FromMcnpIter(Test_FromMcnp[X]):
    element: type[X]

    def test_from_mcnp_iter_valid(self) -> None:
        """
        Tests `EXAMPLES_FROM_MCNP_VALID` on `from_mcnp` and `to_mcnp_iter`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            print(example)

            generator = self.element.from_mcnp_iter(example, returning=False)
            for _ in generator:
                pass
