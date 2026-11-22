"""
Write every gamma entering the NaI detector (cell 3) of a WRITE=ALL PTRAC file to parquet:
position, direction, energy, weight, time and the originating isotope (parent_zaid).

    python script_example_01_ptrac_to_parquet.py [ptrac_path] [out.parquet]
"""

import pathlib
import sys

import pymcnp


DETECTOR_CELL = '3'


def convert(path: pathlib.Path, out: pathlib.Path) -> int:
    """Writes the detector entries of one PTRAC file to parquet; returns the row count."""

    ptrac, _ = pymcnp.Ptrac.from_file('examples/example_02.ptrac')
    frame = ptrac.to_dataframe()
    frame = frame.loc[frame['NCL(PBL%I%ICL)'] == DETECTOR_CELL]
    frame.to_parquet(out)

    return len(frame)


if __name__ == '__main__':
    n = convert(
        pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'script_example_01_output/0/0.ptrac'),
        pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else 'out.parquet'),
    )
    print(f'{n} photons')
