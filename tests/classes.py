import re
import math
import types
import numbers

import pytest
import typing
import pathlib
import collections

import pandas

import pymcnp

# Numbers of example texts, e.g., ``-0.19652E+01``.
_NUMBER = re.compile(r'[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?')

T = typing.TypeVar('T', bound=pymcnp.abc.Symbol)


class Test_FromMcnp(typing.Generic[T]):
    element: type[T]

    EXAMPLES_FROM_MCNP_VALID: collections.abc.Sequence[str] = []
    EXAMPLES_FROM_MCNP_INVALID: collections.abc.Sequence[str] = []
    # Examples that parse only in part, mapped to the text left over.
    EXAMPLES_FROM_MCNP_REMAINDER: collections.abc.Mapping[str, str] = {}

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
        Tests that `from_mcnp` rejects `EXAMPLES_FROM_MCNP_INVALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_INVALID:
            print(example)

            with pytest.raises(pymcnp.abc.Error):
                self.element.from_mcnp(example)

    def test_from_mcnp_remainder(self) -> None:
        """
        Tests that `from_mcnp` leaves the expected text of `EXAMPLES_FROM_MCNP_REMAINDER`.
        """

        for example, remainder in self.EXAMPLES_FROM_MCNP_REMAINDER.items():
            print(example)

            _, source = self.element.from_mcnp(example)
            assert source == remainder


U = typing.TypeVar('U', bound=pymcnp.abc.File)


class Test_FromFile(Test_FromMcnp, typing.Generic[U]):
    element: type[U]

    EXAMPLES_FROM_FILE_VALID: collections.abc.Sequence[pathlib.Path] = []
    EXAMPLES_FROM_FILE_INVALID: collections.abc.Sequence[pathlib.Path] = []
    # Files that parse only in part, mapped to the text left over.
    EXAMPLES_FROM_FILE_REMAINDER: collections.abc.Mapping[pathlib.Path, str] = {}

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
        Tests that `from_file` rejects `EXAMPLES_FROM_FILE_INVALID`.
        """

        for example in self.EXAMPLES_FROM_FILE_INVALID:
            print(example)

            with pytest.raises(pymcnp.abc.Error):
                self.element.from_file(example)

    def test_from_file_remainder(self) -> None:
        """
        Tests that `from_file` leaves the expected text of `EXAMPLES_FROM_FILE_REMAINDER`.
        """

        for example, remainder in self.EXAMPLES_FROM_FILE_REMAINDER.items():
            print(example)

            _, source = self.element.from_file(example)
            assert source == remainder

    def test_to_file(self, tmp_path: pathlib.Path) -> None:
        """
        Tests `EXAMPLES_FROM_FILE_VALID` on `to_file`: the file holds `to_mcnp` and reads back to the same object.
        """

        for index, example in enumerate(self.EXAMPLES_FROM_FILE_VALID):
            print(example)

            a, _ = self.element.from_file(example)
            path = tmp_path / f'{index}-{example.name}'
            a.to_file(path)
            assert path.read_text() == a.to_mcnp()
            b, remainder = self.element.from_file(path)
            assert remainder == ''
            assert b.to_mcnp() == a.to_mcnp()


class SymbolWithDataIter(pymcnp.abc.symbol.WithDataIter, pymcnp.abc.Symbol): ...


V = typing.TypeVar('V', bound=SymbolWithDataIter)


class Test_ToDataframe(typing.Generic[V]):
    element: type[V]

    EXAMPLES_TO_DATAFRAME: list[str] = []
    # Examples of ``EXAMPLES_TO_DATAFRAME`` without data rows, e.g., a tally block with only its total.
    EXAMPLES_TO_DATAFRAME_EMPTY: collections.abc.Sequence[str] = []

    def test_to_dataframe(self) -> None:
        """
        Tests `to_dataframe` on `EXAMPLES_TO_DATAFRAME`: it has rows, every number in it is a number of the example
        text, and the text written back gives the same dataframe.

        The dataframes of the file fixtures are checked by the snapshot (``tests/snapshot.py``), and some values by hand
        in the tests of the classes.
        """

        for example in self.EXAMPLES_TO_DATAFRAME:
            print(example)

            element, _ = self.element.from_mcnp(example)
            frame = element.to_dataframe()
            assert isinstance(frame, pandas.DataFrame)
            if example in self.EXAMPLES_TO_DATAFRAME_EMPTY:
                assert frame.empty
                continue

            assert len(frame) > 0
            found = {float(token) for token in _NUMBER.findall(example)}
            for column in frame.columns:
                for value in frame[column]:
                    if isinstance(value, numbers.Real) and not isinstance(value, bool) and not math.isnan(value):
                        assert float(value) in found, f'{column=} {value=}'

            again, _ = self.element.from_mcnp(element.to_mcnp())
            pandas.testing.assert_frame_equal(again.to_dataframe(), frame)


def _check_yield(item: object) -> None:
    """
    Checks that iterative compilers yield parsed symbols, or inner generators yielding parsed symbols.
    """

    if isinstance(item, types.GeneratorType):
        for inner in item:
            assert isinstance(inner, pymcnp.abc.Symbol), f'{inner=}'
    else:
        assert isinstance(item, pymcnp.abc.Symbol), f'{item=}'


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
            for item in generator:
                _check_yield(item)


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
            for item in generator:
                _check_yield(item)
