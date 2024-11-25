from . import modify
from . import append
from .. import files


def update_nps(inpt, npp: int):
    """Updates the ``npp`` value on the ``nps`` card.

    ``update_nps`` uses ``modify`` to change the ``nps`` card or add a new ``nps``
    card if it does not already exist.

    Parameters:
        npp: New total number of histories to run.

    Returns:
        The modified Inp object.
    """

    if 'nps' in inpt.data_micellaneous:
        modify.modify(inpt.data_micellaneous['nps'], npp=files.utils.types.McnpInteger(npp))
    else:
        append.append_data(inpt, files.inp.data.Nps.from_mcnp(f'nps {npp}'))


def update_seed(inpt, seed: int = None):
    """
    Updates the ``seed`` key-value pair on the ``rand`` card.

    ``update_seed`` uses ``modify`` to change the ``rand`` card or add a new
    ``rand`` card if it does not already exist.

    Parameters:
        input_: PyMCNP INP object with NPS data card to update.
        seed: New random number generator seed.

    Returns:
        The modified Inp object.
    """

    if seed is None or seed % 2 == 0:
        raise ValueError

    seed = files.utils.types.McnpInteger(seed)

    if 'rand' in inpt.data_micellaneous:
        if 'seed' not in inpt.data_micellaneous['rand'].pairs:
            new_pairs = inpt.data_micellaneous['rand'].pairs | {'seed': seed}
            modify.modify(inpt.data_micellaneous['rand'].pairs['seed'], pairs=new_pairs)
        else:
            modify.modify(inpt.data_micellaneous['rand'].pairs['seed'], seed=seed)
    else:
        append.append_data(inpt, files.inp.DataRand.from_mcnp(f'rand seed={seed}'))
