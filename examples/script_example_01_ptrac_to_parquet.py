"""
Write every gamma entering the NaI detector (cell 3) of a WRITE=ALL PTRAC file to parquet:
position, direction, energy, weight, time and the originating isotope (parent_zaid).

    python script_example_01_ptrac_to_parquet.py [ptrac_path] [out.parquet]
"""

import pathlib
import sys

import pandas
import pymcnp
from pymcnp.ptrac import EventType, Particle

DETECTOR_CELL = 3


def convert(ptrac: pathlib.Path, out: pathlib.Path) -> int:
    """Writes the detector entries of one PTRAC file to parquet; returns the row count."""
    rows = [
        {**e.to_dict(), 'parent_zaid': track.parent_zaid}
        for track in pymcnp.Ptrac.tracks(ptrac)
        if track.particle == Particle.PHOTON
        for e in track.events
        if e.type is EventType.SURFACE and e.cell_entered == DETECTOR_CELL
    ]
    frame = pandas.DataFrame(rows)
    frame.to_parquet(out)
    return len(frame)


if __name__ == '__main__':
    n = convert(
        pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'script_example_01_output/0/0.ptrac'),
        pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else 'out.parquet'),
    )
    print(f'{n} photons')
