import random
import pathlib

import pymcnp


MAX_NPS = 1000


def main(path, command):
    path = pathlib.Path(path)

    for file_or_dir in path.rglob('*'):
        if not file_or_dir.is_dir():
            continue

        inp_path = file_or_dir / 'inp.i'
        inp = pymcnp.read.read_input(inp_path)
        nps = inp.data_micellaneous['nps'].npp

        if nps > MAX_NPS:
            pymcnp.update.update_nps(inp, MAX_NPS)
        inp.update_seed(int(random.random() * 9223372036854775807) // 2 * 2 + 1)

        inp.to_mcnp_file(inp_path)
