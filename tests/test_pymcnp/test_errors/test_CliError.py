import pymcnp


class Test_CliError:
    def test__str__(self):
        str(pymcnp.errors.CliError(pymcnp.errors.CliCode.RUNTIME_PATH, 'Hi'))
        str(pymcnp.errors.CliError(pymcnp.errors.CliCode.RUNTIME_DOER, 'Hi'))
