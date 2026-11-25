"""
Prints best-of-3 parse times, for humans and for comparing changes to the parsers.

    uv run python benchmarks/parse.py
"""

import time
import pathlib
import collections.abc

import pymcnp

FILES = pathlib.Path(__file__).parent.parent / 'files'


def best(function: collections.abc.Callable[[], object]) -> float:
    times = []
    for _ in range(3):
        start = time.perf_counter()
        function()
        times.append(time.perf_counter() - start)
    return min(times)


def main() -> None:
    inps = sorted((FILES / 'inp').glob('valid_*.inp'))

    def parse_inps() -> None:
        for path in inps:
            try:
                pymcnp.Inp.from_file(path)
            except pymcnp.abc.Error:
                pass

    ptrac = FILES / 'ptrac' / 'valid_31.ptrac'
    cases = {
        f'Inp.from_file x {len(inps)} valid fixtures': parse_inps,
        'Outp.from_file(valid_38)': lambda: pymcnp.Outp.from_file(FILES / 'outp' / 'valid_38.outp'),
        'Meshtal.from_file(valid_39)': lambda: pymcnp.Meshtal.from_file(FILES / 'meshtal' / 'valid_39.meshtal'),
        'Ptrac.from_file(valid_31)': lambda: pymcnp.Ptrac.from_file(ptrac),
        'Ptrac.from_file(valid_31)[0].to_dataframe()': lambda: pymcnp.Ptrac.from_file(ptrac)[0].to_dataframe(),
        'Ptrac.iter_histories(valid_31)': lambda: list(pymcnp.Ptrac.iter_histories(ptrac)),
    }
    for name, function in cases.items():
        print(f'{best(function):8.3f} s  {name}')


if __name__ == '__main__':
    main()
