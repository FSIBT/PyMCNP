"""
Material cards
"""

from collections import defaultdict
import pkg_resources
import re

from molmass import Formula
import numpy as np
import pandas as pd


def isotopic_abundance(element):
    """
    Parameters
    ----------
    element : string
        chemical symbol e.g 'H'.

    Returns
    -------
    result : dictionary
        stable isotopes and their respective natural abundance.

    """
    nist_file = pkg_resources.resource_filename('pymcnp', 'data/Isotopes-NIST-2.txt')
    with open(nist_file) as f:
        lines = f.readlines()

    result = defaultdict()
    for i, line in enumerate(lines):
        tmp = line.split()
        if element in tmp:
            Z = re.findall(r'\d+', lines[i - 1])[0]
            symbol = element
            isotope = re.findall(r'\d+', lines[i + 1])[0]
            # account for isotopically pure elements
            try:
                tmp2 = lines[i + 3].split()
                comp = [float(tmp2[-1])]
            except ValueError:
                comp = re.findall(r'\d.+(?=\()', lines[i + 3])
            if len(comp) != 0:
                result[Z + symbol + '-' + isotope] = float(comp[0])
    return result


def make_material(element, percent, cutoff=0.005, return_string=True):
    """
    Parameters
    ----------
    element : string
        chemical symbol e.g. 'H'.
    percent : float
        percent composition <= 1.
    cutoff : float, optional
        percent cutoff for negligible abundances. The default is 0.005 (0.5%).

    Returns
    -------
    res : list
        MNCP format for material card.

    """
    elem_dict = isotopic_abundance(element)
    elem_dict = {key: val for key, val in elem_dict.items() if val > cutoff}
    lst = list(elem_dict.keys())
    if lst == []:
        raise Exception(
            'ERROR: no isotope found. Double check the symbol or try reducing the cutoff value'
        )
    Z = re.findall(r'\d+', lst[0])[0]
    rel_p = np.array(list(elem_dict.values())) * percent
    A = []
    for el in lst:
        a = re.findall(r'\d+', el)[1]
        if len(a) == 2:
            a = '0' + a
        elif len(a) == 1:
            a = '00' + a
        A.append(a)

    res = []
    res_lst = []
    for isot, perc in zip(A, rel_p):
        val = str(round(perc, 10))
        res.append(f'{Z}{isot}      -{val}      $ {element}-{isot}')
        res_lst.append([int(f'{Z}{isot}'), float(val)])
    if return_string:
        return res
    else:
        return [item for sublist in res_lst for item in sublist]


def make_material_from_formula(formula, frac=1, weight_frac=True):
    # TODO: implement atomic fraction
    form = Formula(formula)
    comp = form.composition().dataframe()
    mat = []
    total = 0
    for c in comp.index:
        # mat.append(make_material(c[0], frac * c[3], return_string=True))
        fr = comp.loc[c].Fraction
        mat.append(make_material(c, frac * fr, return_string=True))
        total += fr
    mat_flat = [item for sublist in mat for item in sublist]
    print(f'Weight fractions for {formula} = {total}')
    return mat_flat


def make_average_composition(elm_dict):
    # elm_dict = {"X":(rho, frac)}
    tot = 0
    rho_avg = 0
    materials = []
    for key in elm_dict.keys():
        tot += elm_dict[key][1]
        rho_avg += elm_dict[key][1] * elm_dict[key][0]
        mt1 = make_material_from_formula(key, frac=elm_dict[key][1])
        materials.append(mt1)
    mat = [item for sublist in materials for item in sublist]

    frac_isot = 0
    isot_lst = []
    comment = []
    for i, m in enumerate(mat):
        split = m.split()
        comment.append(split[-2] + ' ' + split[-1])
        isot_lst.append([int(split[0]), float(split[1])])
        frac_isot += float(split[1])

    # add up duplicates
    isot_np = np.array(isot_lst)
    dfx = pd.DataFrame(data=isot_np, columns=['zaid', 'frac'], index=comment)
    dfx_sort = dfx.sort_values(by='zaid')
    df = dfx_sort.groupby('zaid').sum()
    str_id = dfx_sort.index.unique()

    res = []
    for z, ids in zip(df.index, str_id):
        zaid = str(int(z))
        val = round(float(-1 * df.loc[z]), 10)
        res.append(f'{zaid}      -{val}      {ids}')

    print('Total fraction: ', tot)
    print('Total fraction after isotope splitting: ', frac_isot * -1)

    return rho_avg, res
