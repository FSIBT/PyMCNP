"""
Checks that parsing time grows linearly with the size of the input.

Each test times a parse of ``n`` and of ``2n`` repeats of a unit and requires a ratio below 2.6 (2 for
linear, 4 for quadratic).
"""

import gc
import time
import pathlib
import collections.abc

import pytest

import pymcnp

pytestmark = pytest.mark.scaling

FILES: pathlib.Path = pathlib.Path(__file__).parent.parent / 'files'


def _best(parse: collections.abc.Callable[[str], object], source: str) -> float:
    # Freezing the objects that exist before parsing, i.e., the imported library, keeps full garbage
    # collections from walking them: one such collection costs as much as a small parse, so whether it
    # falls into the parse of ``n`` or of ``2n`` would decide the ratio. Objects of the parse are still collected.
    best = float('inf')
    for _ in range(3):
        gc.collect()
        gc.freeze()
        try:
            start = time.perf_counter()
            parse(source)
            best = min(best, time.perf_counter() - start)
        finally:
            gc.unfreeze()
    return best


def ratio(build: collections.abc.Callable[[int], str], parse: collections.abc.Callable[[str], object], n: int) -> float:
    """
    Time of parsing ``build(2 * n)`` over time of parsing ``build(n)``, best of three each.
    """

    return _best(parse, build(2 * n)) / _best(parse, build(n))


def test_ptrac_scales_linearly() -> None:
    lines = (FILES / 'ptrac' / 'valid_27.ptrac').read_text().split('\n')
    header, history = lines[:8], lines[8:737]  # the first history, up to the start of the second

    def build(k: int) -> str:
        return '\n'.join(header + history * k) + '\n'

    assert ratio(build, pymcnp.Ptrac.from_mcnp, 8) < 2.6


def test_meshtal_scales_linearly() -> None:
    lines = (FILES / 'meshtal' / 'valid_38.meshtal').read_text().split('\n')
    start = next(i for i, line in enumerate(lines) if 'Result' in line) + 1
    header, rows = lines[:start], [line for line in lines[start:] if line.strip()][:1000]

    def build(k: int) -> str:
        return '\n'.join(header + rows * k) + '\n'

    assert ratio(build, pymcnp.Meshtal.from_mcnp, 10) < 2.6


def test_inp_scales_linearly() -> None:
    def build(k: int) -> str:
        cells = ''.join(f'{i} 0 -{i} imp:n=1\n' for i in range(1, k + 1))
        surfaces = ''.join(f'{i} so {i}\n' for i in range(1, k + 1))
        return f'scaling\n{cells}\n{surfaces}\nnps 10\n'

    assert ratio(build, pymcnp.Inp.from_mcnp, 400) < 2.6
