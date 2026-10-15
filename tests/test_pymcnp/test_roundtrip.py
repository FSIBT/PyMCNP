import re
import shutil
import pathlib
import subprocess

import pytest

import pymcnp

EXAMPLES = pathlib.Path(__file__).parents[2] / 'examples'
INPS = sorted(EXAMPLES.glob('example_*.inp'))
IDS = [path.stem for path in INPS]


def _fast(source):
    """Cuts the run to 2000 histories with a fixed seed."""

    source = re.sub(r'(?im)^(nps|rand)\b.*\n?', '', source).rstrip('\n')
    return f'{source}\nnps 2000\nrand seed=12345\n'


def _run(directory, name, source):
    directory.mkdir()
    path = directory / f'{name}.inp'
    path.write_text(source)
    subprocess.run(['mcnp6', 'ixr', f'i={path.name}', f'n={name}.'], cwd=directory, capture_output=True, timeout=300, check=False)
    output = directory / f'{name}.o'
    return output.read_text(errors='replace') if output.exists() else ''


@pytest.mark.parametrize('path', INPS, ids=IDS)
class Test_Roundtrip_PyMCNP:
    def test_write_is_idempotent(self, path):
        written = pymcnp.Inp.from_file(path).to_mcnp()

        assert pymcnp.Inp.from_mcnp(written).to_mcnp() == written

    def test_lines_fit_in_80_columns(self, path):
        written = pymcnp.Inp.from_file(path).to_mcnp()

        assert max(len(line) for line in written.splitlines()) <= 80


@pytest.mark.skipif(shutil.which('mcnp6') is None, reason='mcnp6 is not installed')
@pytest.mark.parametrize('path', INPS, ids=IDS)
class Test_Roundtrip_MCNP:
    def test_mcnp_accepts_original_and_rewritten(self, path, tmp_path):
        original = _fast(path.read_text())
        rewritten = _fast(pymcnp.Inp.from_mcnp(original).to_mcnp())

        out_original = _run(tmp_path / 'original', path.stem, original)
        out_rewritten = _run(tmp_path / 'rewritten', path.stem, rewritten)

        assert out_original, 'MCNP did not run the original input'
        assert 'fatal error' not in out_original
        assert out_rewritten, 'MCNP did not run the rewritten input'
        assert 'fatal error' not in out_rewritten
