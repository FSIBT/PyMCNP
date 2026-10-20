"""
Run the 20 NPS cases in parallel with MCNP and convert each PTRAC to parquet.

Result in script_example_01_output/N/: N.inp, N.outp, N.ptrac, N.parquet for N = 0..19.

    python script_example_01_run.py
"""

import shutil

import pymcnp

import script_example_01_geometry as geometry
import script_example_01_ptrac_to_parquet as to_parquet

ROOT = geometry.OUTPUT


class Cases(pymcnp.Run):
    def posthook_file(self, result):
        assert result.ptrac, 'MCNP wrote no PTRAC file'
        n = to_parquet.convert(result.ptrac, result.ptrac.with_suffix('.parquet'))
        print(f'{result.ptrac.stem}: {n} photons')


if __name__ == '__main__':
    shutil.rmtree(ROOT, ignore_errors=True)
    inps = list(geometry.base.scan(nps=[int(n) for n in geometry.NPS_VALUES]))
    Cases(inps, command='mcnp6', names='{index}', batch=False).run(ROOT)
