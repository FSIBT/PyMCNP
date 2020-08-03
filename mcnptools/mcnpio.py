# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:56:29 2020

@author: mauricio

Functions to create and read MCNP io files
"""

import numpy as np
import pandas as pd
from scipy.interpolate import griddata as gd
from pathlib import Path
import re
from collections import defaultdict
import time
import pkg_resources
from datetime import datetime


def read_output(file, tally=8, n=1, tally_type="e", particle="n"):
    """ Read standard MCNP output file.
    

    Parameters
    ----------
    file : Path object.
        MCNP output file in plain text format
    tally: integer.
        tally type based on MCNP manual. Default is 8: pule-height tally
    n: integer.
        tally number to output. Default is the first one found.
    tally_type: string.
        either energy 'e', time 't', or both 'et'.
        

    Returns
    -------
    df : pandas dataframe.
        dataframe with columns: energy, cts, err
        or dataframe with columns: time, cts, err
        or dataframe with columns: energy, time_bins...
        time in [us]

    """
    flag = False
    if tally_type == "t":
        key_word = "time"
    elif tally_type == "e":
        key_word = "energy"
    elif tally_type == "et" or tally_type == "te":
        flag = True
        key_word = "energy"
    else:
        print("ERROR: tally type not recognized")

    if particle == "n":
        particle = "neutrons"
    elif particle == "p":
        particle = "photons"
    lidx = []
    endbin = []
    pidx = []
    en = []
    surf = []
    tagix = []
    uncol = []
    print("Reading output file...")
    with open(file, "r") as myfile:
        for i, l in enumerate(myfile):
            tmp = l.split()
            if "tally" in tmp and "type" in tmp and str(tally) in tmp:
                lidx.append(i)
            if "particle(s):" in tmp and particle in tmp:
                pidx.append(i)
            if key_word in tmp:
                en.append(i)
            if ("total") in tmp:
                endbin.append(i)
            if "surface" in tmp:
                surf.append(i)
            if "uncollided" in tmp and "flux" in tmp:
                uncol.append(i)
            if "user" in tmp and "bin" in tmp:
                tagix.append(i)
    first = [x for x in en if x > pidx[0]][0]  # begining of data
    surfaces = [x for x in surf if x > first]  # rest of data
    if len(surfaces) > 0:  # this is usually necessary for F1 tally
        [lidx.append(x) for x in surfaces]
        pidx = lidx
    if len(tagix) > 0:
        pidx = tagix
    if len(uncol) > 0:
        [lidx.append(x) for x in uncol]
        pidx = lidx

    print(f"Found {len(pidx)} tallies")
    print(f"Output tally number {n}")

    if flag:  # this is a time and energy tally
        start = [x for x in en if x > pidx[n - 1]][0] + 1
        totals0 = np.array([x for x in endbin if x > pidx[n - 1]][:-1]) + 4
        diffs = np.diff(totals0)
        # = totals[1] - totals[0]
        ix_delete = np.where(diffs == 2)[0] + 1
        totals = np.delete(totals0, ix_delete)
        idxall = np.append(start, totals)
        ebins = idxall[1] - idxall[0] - 4
        energy = np.genfromtxt(
            file, delimiter=" ", usecols=(0), skip_header=idxall[0], max_rows=ebins
        )
        df = pd.DataFrame(columns=["energy"], data=energy)

        starttime = time.time()
        with open(file, "r") as f:
            allf = f.readlines()

        for i in range(len(idxall)):
            tme0 = allf[idxall[i] - 2]
            tme1 = re.findall("\d.+\d", tme0)
            tme2 = tme1[0].split()
            tme = np.array(tme2, dtype="float")
            data0 = allf[idxall[i] : idxall[i] + ebins]
            data1 = np.array([x.split() for x in data0], dtype="float")
            data2 = data1[:, 1::2]
            # need the following if statement because 'Total' printed at the end
            if len(tme) == 1:
                data2 = data2[:, 0:-1]
                df0 = pd.DataFrame(columns=tme / 100, data=data2)
                df = df.join(df0)
                break
            else:
                df0 = pd.DataFrame(columns=tme / 100, data=data2)
                df = df.join(df0)

        endtime = time.time()
        print(f"For loop took {round(endtime-starttime,2)} seconds")

        return df
    else:
        start = [x for x in en if x > pidx[n - 1]][0]  # begining of data
        end = [x for x in endbin if x > pidx[n - 1]][0]  # end of data
        binsP = end - start  # number of bins
        Edep = np.genfromtxt(
            file,
            delimiter=" ",
            usecols=(0, 3, 4),
            skip_header=start + 1,
            max_rows=binsP - 1,
        )
        df = pd.DataFrame(columns=[key_word, "cts", "err"], data=Edep)
        if key_word == "time":
            df[key_word] = df[key_word] / 100  # output in microseconds
        return df


def read_inp_source(file, s1=["SI1", "SP1"], s2=["SI2", "SP2"], form="column"):
    """
    Parameters
    ----------
    file : str or file Path
        MCNP input file to read.
    s1 : list of strings, optional
        keywords for start of SI1 and SP1. The default is ['SI1','SP1'].
    s2 : list of strings, optional
        keywords for start of SI2 and SP2. The default is ['SI2','SP2'].
    form: string
        keyword for column format (#) or row format (not yet implemented).
        The default is 'column'

    Returns
    -------
    df1 : pandas DataFrame
        SI1 and SP1.
    df2 : pandas Data Frame
        SI2 and SP2.

    """
    # need implementation of row format
    idx1_start = 0
    idx2_start = 0
    print("Reading input file...")
    with open(file, "r") as myfile:
        for i, l in enumerate(myfile):
            tmp = l.split()
            if s1[0] in tmp and s1[1] in tmp:
                idx1_start = i
            if s2[0] in tmp and s2[1] in tmp:
                idx2_start = i
    with open(file, "r") as f:
        all_lines = f.readlines()
    print("Done")
    s1_str = all_lines[idx1_start + 1 : idx2_start]
    s1_str_split = [x.split() for x in s1_str]
    s1np = np.array(s1_str_split, dtype="float")
    s2_str = all_lines[idx2_start + 1 : idx2_start + 3]
    s2_str_split = [x.split() for x in s2_str]
    s2np = np.array(s2_str_split, dtype="float")
    df1 = pd.DataFrame(columns=["SI", "SP"], data=s1np)
    df2 = pd.DataFrame(columns=["SI", "SP"], data=s2np)
    return df1, df2


def make_inp(cells, surfaces, materials, dataC, fileName):  # to be deleted
    """ Create MCNPinput file from scratch.
    

    Parameters
    ----------
    cells : List of strings.
        cell cards
    surfaces: List of strings.
        surface cards
    materials: List of strings.
        material cards
    dataC: List of strings.
        data cards
    fileName: string or Path object
        file to write
        

    Returns
    -------
    creates input file"""

    with open(fileName, "w") as f:
        f.writelines(["%s\n" % c for c in cells])
        f.writelines("\n")
        f.writelines("%s\n" % s for s in surfaces)
        f.writelines("\n")
        f.writelines(["%s\n" % m for m in materials])
        f.writelines(["%s\n" % d for d in dataC])


def make_inp_DE(
    cells, surfaces, materials, dataC, fileName, Ebin, freq
):  # to be deleted
    """Create input file with histogram photon source
    
    Parameters
    ----------
    cells : List of strings.
        cell cards
    surfaces: List of strings.
        surface cards
    materials: List of strings.
        material cards
    dataC: List of strings.
        data cards
    Ebin:
        energy bins
    freq: 
        normalized frequency
        

    Returns
    -------
    creates input file"""

    with open(fileName, "w") as f:
        f.writelines(["%s\n" % c for c in cells])
        f.writelines("\n")
        f.writelines(["%s\n" % s for s in surfaces])
        f.writelines("\n")
        f.writelines(["%s\n" % m for m in materials])
        f.writelines(["%s\n" % d for d in dataC])
        f.writelines("SI1 ")
        f.writelines("%s &\n" % b for b in Ebin[:-1])
        f.writelines("%s\n" % Ebin[-1])
        f.writelines("SP1 0 &\n")
        f.writelines("%s &\n" % f for f in freq[1:-1])
        f.writelines("%s\n" % freq[-1])


def numpy_fillna(data):
    # Get lengths of each row of data
    lens = np.array([len(i) for i in data])

    # Mask of valid places in each row
    mask = np.arange(lens.max()) < lens[:, None]

    # Setup output array and put elements from data into masked positions
    out = np.zeros(mask.shape, dtype=data.dtype)
    out[mask] = np.concatenate(data)
    return out


def read_fmesh(file, mesh_info=False):
    """
    Parameters
    ----------
    file : string
        meshtal file.
    mesh_info : boolean, optional
        if mesh points are desired. The default is False.

    Returns
    -------
    pandas dataframe
        dataframe columns: Energy, X, Y, Result, RelError
        or if mesh_info=True, an additional dataframe is returned
        containing information regarding bins
    """

    idx0 = 0
    e0 = np.array([0])
    t0 = np.array([0])
    totals = []
    with open(file, "r") as myfile:
        for i, l in enumerate(myfile):
            tmp = l.split()
            if ("X direction") in l:
                x0 = np.asarray(tmp[2:], dtype=float)
            if ("Y direction") in l:
                y0 = np.asarray(tmp[2:], dtype=float)
            if ("Z direction") in l:
                z0 = np.asarray(tmp[2:], dtype=float)
            if ("Energy bin boundaries") in l:
                e0 = np.asarray(tmp[3:], dtype=float)
            if ("Time bin boundaries") in l:
                t0 = np.asarray(tmp[3:], dtype=float)
            if "Result" in tmp and "Error" in tmp:
                idx0 = i
            if "Total" in tmp:
                totals.append(i)

    with open(file, "r") as f:
        all_data = f.readlines()

    data0 = all_data[idx0 + 1 :]
    data1 = np.array(
        [np.fromstring(x, dtype=float, sep=" ") for x in data0 if "Total" not in x]
    )
    cols = all_data[idx0].split()
    cols.remove("Rel")
    df = pd.DataFrame(data=data1, columns=cols)
    # info
    if mesh_info:
        data_info = [e0, t0, x0, y0, z0]
        info_np = np.array(data_info)
        a = numpy_fillna(info_np)
        df_info = pd.DataFrame(
            data=a.T, columns=["Ebins", "tbins", "Xbins", "Ybins", "Zbins"]
        )
        return df_info, df
    else:
        return df


def griddata(x, y, z, nbins, xrange=None, yrange=None):
    """
    Parameters
    ----------
    x : numpy array or dataframe
        x-values.
    y : numpy array or dataframe
        y-values.
    z : numpy array or dataframe
        z-values.
    nbins : integer
        number of bins.
    xrange : list, optional
        with minimum and maximum values for x. The default is None.
    yrange : list, optional
        with minimum and maximum values for x. The default is None.

    Returns
    -------
    xx : numpy array
        mesh points.
    result : numpy array
        3D matrix better visualized with imshow.

    """
    if xrange == None:
        lowx = x.min()
        highx = x.max()
    if yrange == None:
        lowy = y.min()
        highy = y.max()
    else:
        lowx = xrange[0]
        highx = xrange[1]
        lowy = yrange[0]
        highy = yrange[1]

    xx = np.linspace(lowx, highx, nbins)
    yy = np.linspace(lowy, highy, nbins)
    xg, yg = np.meshgrid(xx, yy)

    result = gd((x, y), z, (xg, yg))  # , method='cubic')
    return xx, result


def make_pulsed_source(B, P, BP, LW, SP):
    """
    Parameters
    ----------
    B : integer
        burst time in microseconds.
    P : integer
        period in microseconds.
    BP : integer > 0
        burst packets.
    LW : integer
        long wait time in microseconds.
    SP : integer
        sigma packets.

    Returns
    -------
    numpy array
        [SI1,SP1], and [SI2,SP2].
    """
    if BP <= 0:
        print("Burst packets must be greater than 0")
    if SP <= 0:
        print("Sigma packets must be greater than 0")
    res = np.zeros((2 * BP + 2, 2))
    res[1::2, 1] = 1
    for i in range(int(res.shape[0] / 2)):
        res[2 * i][0] = int(i * P)
        res[2 * i - 1][0] = int((i - 1) * P + B)
    res = res[:-1]
    res[-1][0] = res[-3][0] + LW + P
    res[:, 0] = res[:, 0] * 1e2  # to shakes
    # SI2, SP2
    res2 = np.array([[0, res[-1][0] * SP], [0, 1]])
    return res.astype(int), res2.transpose().astype(int)


def write_inp_time(file_to_write, tbins, S1, S2, ncutoff=None):
    """
    Parameters
    ----------
    file_to_write : string or Path object
        file to write.
    tbins : integer
        number of time bins.
    S1 : numpy array
        source information and probability 1.
    S2 : numpy array
        source information and probability 2.
    ncutoff : integer, optional
        neutron cutoff time in seconds. The default is None.

    Raises
    ------
    Exception
        'time information' and 'end file' need to be in the file.

    Returns
    -------
    None.

    """
    with open(file_to_write, "r") as rf:
        idx_end = 0
        for i, l in enumerate(rf):
            tmp = l.split()
            if "time" in tmp and "information" in tmp:
                idx_tme = i
            if "end" in tmp and "file" in tmp:
                idx_end = i
    with open(file_to_write, "r") as f:
        file = f.readlines()

    if idx_tme == 0:
        raise Exception(
            "ERROR: Make sure there is a line with the words: 'time information'"
        )
    if idx_end == 0:
        raise Exception(
            "ERROR: Make sure the last line of the file has the words 'end file' in it"
        )

    source0 = "sdef par=n erg=14 TME=D1<D2 \n"
    source1 = "# SI1 SP1 \n"
    file.insert(idx_tme + 2, source0)
    file.insert(idx_tme + 3, source1)
    x = 1
    for l1 in S1:
        tmp = "{} {} \n".format(l1[0], l1[1])
        file.insert(idx_tme + 3 + x, tmp)
        x += 1
    source2 = "# SI2 SP2 \n"
    file.insert(idx_tme + 3 + x, source2)
    x += 1
    for l2 in S2:
        tmp = "{} {} \n".format(l2[0], l2[1])
        file.insert(idx_tme + 3 + x, tmp)
        x += 1
    str1 = "c \n"
    file.insert(idx_tme + 3 + x, str1)
    tstr = "t0 0 {}i {} \n".format(tbins - 1, S2[1, 0])
    file.insert(idx_tme + 4 + x, tstr)
    if ncutoff != None:
        cut = "cut:n" + " " + str(int(ncutoff * 1e8)) + " " + "j 0 0 \n"
        file.insert(idx_tme + 5 + x, cut)
    with open(file_to_write, "w") as wf:
        wf.writelines(file)


def write_inp_tally(
    file_to_write, cell, erg=[0.1, 10, 1000], tally_type="F4", particle="n", cutoff=None
):
    """
    Parameters
    ----------
    file_to_write : string or Path object
        file to write.
    cell : integer
        cell number.
    erg : list, optional
        [energy min, energy max, energy bins]. The default is [0.1,10,1000].
    tally_type : string, optional
        type of tally with respective numbering. The default is 'F4'.
    particle : string, optional
        photon 'p' or neutron 'n'. The default is 'n'.
    cutoff : energy cutoff in MeV, optional
        DESCRIPTION. The default is None.

    Raises
    ------
    Exception
        'tally information' and 'end file' must be in the file.

    Returns
    -------
    None.

    """
    tly = tally_type + ":" + particle + " " + str(cell) + "\n"
    energy = (
        "E"
        + re.findall("\d+", tally_type)[0]
        + " "
        + str(erg[0])
        + " "
        + str(erg[2] - 1)
        + "I"
        + " "
        + str(erg[1])
        + "\n"
    )
    if cutoff != None:
        cut = "cut" + ":" + particle + " " + "j" + str(cutoff) + " " + "0"
        com1 = " $ lower energy threshold, analog simulation \n"

    with open(file_to_write, "r") as rf:
        idx_end = 0
        for i, l in enumerate(rf):
            tmp = l.split()
            if "tally" in tmp and "information" in tmp:
                idx_tly = i
            if "end" in tmp and "file" in tmp:
                idx_end = i
    with open(file_to_write, "r") as f:
        file = f.readlines()
    if idx_tly == 0:
        raise Exception(
            "ERROR: Make sure there is a line with the words: 'tally information'"
        )
    if idx_end == 0:
        raise Exception(
            "ERROR: Make sure the last line of the file has the words 'end file' in it"
        )

    file.insert(idx_tly + 2, tly)
    file.insert(idx_tly + 3, energy)
    if cutoff != None:
        file.insert(idx_tly + 4, cut)
        file.insert(idx_tly + 5, com1)

    with open(file_to_write, "w") as wf:
        wf.writelines(file)


def write_inp_tallyF5(
    file_to_write, pos, r0, erg=[0.1, 10, 1000], particle="n", cutoff=None
):
    """
    Parameters
    ----------
    file_to_write : string or Path object
        file to write.
    pos : list
        detector locaion [x,y,z].
    r0: integer
        radius of exclusion (positive in cm and negative in mfp)
    erg : list, optional
        [energy min, energy max, energy bins]. The default is [0.1,10,1000].
    particle : string, optional
        photon 'p' or neutron 'n'. The default is 'n'.
    cutoff : energy cutoff in MeV, optional
        DESCRIPTION. The default is None.

    Raises
    ------
    Exception
        'tally information' and 'end file' must be in the file.

    Returns
    -------
    None.

    """
    tally_type = "F5"
    tly = f"{tally_type}:{particle} {pos[0]} {pos[1]} {pos[2]} {r0} \n"
    energy = (
        "E"
        + re.findall("\d+", tally_type)[0]
        + " "
        + str(erg[0])
        + " "
        + str(erg[2] - 1)
        + "I"
        + " "
        + str(erg[1])
        + "\n"
    )
    if cutoff != None:
        cut = "cut" + ":" + particle + " " + "j" + str(cutoff) + " " + "0"
        com1 = " $ lower energy threshold, analog simulation \n"

    with open(file_to_write, "r") as rf:
        idx_end = 0
        for i, l in enumerate(rf):
            tmp = l.split()
            if "tally" in tmp and "information" in tmp:
                idx_tly = i
            if "end" in tmp and "file" in tmp:
                idx_end = i
    with open(file_to_write, "r") as f:
        file = f.readlines()
    if idx_tly == 0:
        raise Exception(
            "ERROR: Make sure there is a line with the words: 'tally information'"
        )
    if idx_end == 0:
        raise Exception(
            "ERROR: Make sure the last line of the file has the words 'end file' in it"
        )

    file.insert(idx_tly + 2, tly)
    file.insert(idx_tly + 3, energy)
    if cutoff != None:
        file.insert(idx_tly + 4, cut)
        file.insert(idx_tly + 5, com1)

    with open(file_to_write, "w") as wf:
        wf.writelines(file)


def write_inp_mode_nps(file_to_write, mode="n", nps=1000):
    """
    Parameters
    ----------
    file_to_write : string or path object
        file to write.
    mode : string, optional
        mcnp mode e.g. 'n', 'n p', etc. The default is "n".
    nps : integer, optional
        number of simulated particles. The default is 1000.

    Raises
    ------
    Exception
        'source defintion' and 'end file' must be in file.

    Returns
    -------
    None.

    """
    with open(file_to_write, "r") as rf:
        idx_end = 0
        for i, l in enumerate(rf):
            tmp = l.split()
            if "source" in tmp and "definition" in tmp:
                idx_src = i
            if "end" in tmp and "file" in tmp:
                idx_end = i
    with open(file_to_write, "r") as f:
        file = f.readlines()

    if idx_src == 0:
        raise Exception(
            "ERROR: Make sure there is a line with the words: 'source definition'"
        )
    if idx_end == 0:
        raise Exception(
            "ERROR: Make sure the last line of the file has the words 'end file' in it"
        )
    mde = "mode" + " " + mode + "\n"
    npart = "nps" + " " + str(int(nps)) + "\n"
    file.insert(idx_src + 2, mde)
    file.insert(idx_src + 3, npart)
    with open(file_to_write, "w") as wf:
        wf.writelines(file)


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
    file = pkg_resources.resource_filename("mcnptools", "data/Isotopes-NIST-2.txt")
    # read all lines and store in memory
    with open(file, "r") as f:
        lines = f.readlines()

    result = defaultdict()
    for i, l in enumerate(lines):
        tmp = l.split()
        if element in tmp:
            Z = re.findall("\d+", lines[i - 1])[0]
            symbol = element
            isotope = re.findall("\d+", lines[i + 1])[0]
            # account for isotopically pure elements
            try:
                tmp2 = lines[i + 3].split()
                comp = [float(tmp2[-1])]
            except ValueError:
                comp = re.findall("\d.+(?=\()", lines[i + 3])
            if len(comp) != 0:
                result[Z + symbol + "-" + isotope] = float(comp[0])
    return result


def make_material(element, percent, cutoff=0.005):
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
            "ERROR: no isotope found. Double check the symbol or try reducing the cutoff value"
        )
    Z = re.findall("\d+", lst[0])[0]
    rel_p = np.array(list(elem_dict.values())) * percent
    A = []
    for el in lst:
        a = re.findall("\d+", el)[1]
        if len(a) == 2:
            a = "0" + a
        elif len(a) == 1:
            a = "00" + a
        A.append(a)

    res = []
    for isot, perc in zip(A, rel_p):
        val = str(round(perc, 10))
        res.append(f"{Z}{isot}      -{val}      $ {element}-{isot}")
    return res


def write_inp_material(file_to_write, mat_list, mat_num):
    """
    Parameters
    ----------
    file_to_write : string or Path object
        file to write.
    mat_list : list
        material list in MCNP format.
    mat_num : integer
        material number for MCNP input.

    Raises
    ------
    Exception
        'material compositions' and 'source definition' must be in the file.

    Returns
    -------
    None.

    """
    with open(file_to_write, "r") as rf:
        for i, l in enumerate(rf):
            tmp = l.split()
            if "material" in tmp and "compositions" in tmp:
                idx_mat = i
            if "source" in tmp and "definition" in tmp:
                idx_src = i
    with open(file_to_write, "r") as f:
        file = f.readlines()

    if idx_mat == 0:
        raise Exception(
            "ERROR: Make sure there is a line with the words: 'material compositions'"
        )
    if idx_src == 0:
        raise Exception(
            "ERROR: Make sure there is a line with the words: 'source definition'"
        )

    mnum1 = "M" + str(mat_num) + 3 * " " + mat_list[0] + "\n"
    file.insert(idx_src - 1, mnum1)
    x = 1
    for mat in mat_list[1:]:
        length = len(f"M{str(mat_num)}")
        line = (length + 3) * " " + mat + "\n"
        file.insert(idx_src - 1 + x, line)
        x += 1
    file.insert(idx_src - 1 + x, "c \n")
    with open(file_to_write, "w") as wf:
        wf.writelines(file)


def write_inp_sdef_F8(
    file_to_write,
    ebins,
    freq,
    SI2,
    pos,
    cell,
    erg="d1",
    par=2,
    rad="d2",
    clear_sdef=True,
):
    """
    Parameters
    ----------
    file_to_write : string or Path object
        file to write.
    ebins : numpy array
        energy bins.
    freq : numpy array
        frequency or probability (cts).
    SI2 : list
        source infrmation 2 e.g. SI2=[0,10].
    pos : list
        position of gamma source e.g. [0,0,0].
    cell : integer
        cell number.
    erg : string, optional
        energy distribution identifier. The default is 'd1'.
    par : integer, optional
        particle type. The default is 2 (gammas).
    rad : string, optional
        radial distribution for source 2. The default is 'd2'.
    clear_sdef : boolean, optional
        clears the source definition. The default is True.

    Returns
    -------
    None.

    """
    with open(file_to_write, "r") as rf:
        for i, l in enumerate(rf):
            tmp = l.split()
            if "source" in tmp and "definition" in tmp:
                idx_src = i

    with open(file_to_write, "r") as f:
        file = f.readlines()

    if clear_sdef:
        file = file[: idx_src + 2]
    sdef = (
        "SDEF pos="
        + f"{pos[0]} {pos[1]} {pos[2]}"
        + f" CEL={cell}"
        + f" ERG={erg}"
        + f" PAR={par}"
        + f" RAD={rad} \n"
    )
    si2 = f"SI2 {SI2[0]} {SI2[1]} \n"
    si1 = f"# SI1   SP1 \n"
    file.append(sdef)
    file.append(si2)
    file.append(si1)
    for e, f in zip(ebins, freq):
        tmp = f"{e}  {f} \n"
        file.append(tmp)
    with open(file_to_write, "w") as wf:
        wf.writelines(file)


def write_inp_tally_F8(
    file_to_write,
    cell,
    geb,
    tally_nb=8,
    energy=[0.1, 10, 1000],
    nps=1000,
    clear_sdef=True,
):
    """
    Parameters
    ----------
    file_to_write : string or Path object
        file to write.
    cell : integer
        cell number.
    geb : list
        GEB parameters e.g. [-0.020,0.044,0.117].
    tally_nb : integer, optional
        tally 8 number e.g. 18. The default is 8.
    energy : list, optional
        energy range [min, max, bins]. The default is [0.1,10,1000].
    nps : integer, optional
        number of particles. The default is 1000.
    clear_sdef : boolean, optional
        clears source definition. The default is True.

    Returns
    -------
    None.

    """
    with open(file_to_write, "r") as rf:
        for i, l in enumerate(rf):
            tmp = l.split()
            if "source" in tmp and "definition" in tmp:
                idx_src = i

    with open(file_to_write, "r") as f:
        file = f.readlines()

    if clear_sdef:
        file = file[: idx_src + 2]

    mode = "mode e p \n"
    tly = f"F{tally_nb}:p {cell} \n"
    erg = f"E{tally_nb}: {energy[0]} {energy[2]-1}I {energy[1]} \n"
    GEB = f"FT{tally_nb} GEB {geb[0]} {geb[1]} {geb[2]} \n"
    n_part = f"nps {int(nps)} \n"
    file.insert(idx_src + 2, mode)
    file.insert(idx_src + 3, tly)
    file.insert(idx_src + 4, erg)
    file.insert(idx_src + 5, GEB)
    file.insert(idx_src + 6, n_part)
    with open(file_to_write, "w") as wf:
        wf.writelines(file)


class display_info:
    # in development
    """
    Display information from output file.
    Supports tallies: F1, F4, F5, F6, F8
    Supports subtallies: F5 - uncollided flux, tally tag, F1 - surfaces
    """

    def __init__(self, filename):
        self.filename = filename

    def get_runtime(self):
        # in development
        outp = open(self.filename, "r").read().split("\n")

        time1 = ""
        time2 = ""
        for line in outp:
            if "mcnp" in line and "version 6" in line and "probid" in line:
                string = line.replace("     ", " ").split(" ")
                time1 = string[10]
                time2 = string[19]
            if "computer" in line and "time" in line:
                cpt = line

        datetime2 = datetime.strptime(time2, "%H:%M:%S")
        datetime1 = datetime.strptime(time1, "%H:%M:%S")
        diff = datetime1 - datetime2
        # real_time = "real time: " + time.strftime("%H:%M:%S", time.gmtime(diff.seconds))
        real_time = f"real time: {round(diff.seconds/60,1)} minutes"
        computer_time = cpt[1:]
        return real_time, computer_time

    def get_tally_info(self):
        lidx, pidx = [], []
        surf, tagix, uncol = [], [], []
        tally_type, particle, surface = [], [], []
        uncollided, user_bin = [], []

        print("Reading output file...")
        with open(self.filename, "r") as myfile:
            for i, l in enumerate(myfile):
                tmp = l.split()
                if "tally" in tmp and "type" in tmp:
                    lidx.append(i)
                    tally_type.append(l)
                if "particle(s):" in tmp:
                    pidx.append(i)
                    particle.append(tmp)
                if "surface" in tmp and len(lidx) > 0 and i >= min(lidx):
                    surf.append(i)
                    surface.append(tmp)
                if "uncollided" in tmp and "flux" in tmp:
                    uncol.append(i)
                    uncollided.append(l)
                if "user" in tmp and "bin" in tmp:
                    tagix.append(i)
                    user_bin.append(l)
        print("Done reading")
        tot_subtly = len(surface) + len(uncollided) + len(user_bin)
        print("--" * 20)
        print(f"Number of tallies: {len(lidx)}")
        print(f"Number of subtallies: {tot_subtly}")
        print("--" * 20)
        ttype = tally_type[0].split()

        # initialize dataframe
        cols = [
            "tally_type",
            "description",
            "particle",
            "surfaces",
            "uncollided_flux",
            "user_bin",
            "line_number",
        ]
        df = pd.DataFrame(columns=cols)

        sur, unc, ub = 0, 0, 0
        if len(surface) > 0:
            sur = surface
            for ls, s in zip(surf, sur):
                dat0 = [
                    "F" + ttype[2],
                    " ".join(ttype[3:]),
                    particle[0][1],
                    s[1],
                    unc,
                    ub,
                    ls,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df = df.append(ser0, ignore_index=True)
        if len(uncollided) > 0:
            uncol_idx = uncol
            unc0 = "collided photon flux"
            unc = uncollided
            for l in lidx:
                dat0 = [
                    "F" + ttype[2],
                    " ".join(ttype[3:]),
                    particle[0][1],
                    sur,
                    unc0,
                    ub,
                    l,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df = df.append(ser0, ignore_index=True)
            for line, ix in zip(unc, uncol_idx):
                dat0 = [
                    "F" + ttype[2],
                    " ".join(ttype[3:]),
                    particle[0][1],
                    sur,
                    line[1:],
                    ub,
                    ix,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df = df.append(ser0, ignore_index=True)
        if len(user_bin) > 0:
            ub = user_bin
            for line, ix in zip(ub, tagix):
                dat0 = [
                    "F" + ttype[2],
                    " ".join(ttype[3:]),
                    particle[0][1],
                    sur,
                    unc,
                    line,
                    ix,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df = df.append(ser0, ignore_index=True)

        if tot_subtly == 0:
            for l in lidx:
                dat0 = [
                    "F" + ttype[2],
                    " ".join(ttype[3:]),
                    particle[0][1],
                    sur,
                    unc,
                    ub,
                    l,
                ]
                ser0 = pd.Series(dat0, index=df.columns)
                df = df.append(ser0, ignore_index=True)

        # drop all zero columns
        df = df.loc[:, (df != 0).any(axis=0)]
        return df

    def get_nps(self):
        print("Reading output file...")
        nps = 0
        with open(self.filename, "r") as myfile:
            for i, l in enumerate(myfile):
                tmp = l.split()
                if "run" in tmp and "terminated" in tmp:
                    nps = tmp[3]
                    break
        print("Done reading")
        print(f"Number of simulated particles: {nps}")
