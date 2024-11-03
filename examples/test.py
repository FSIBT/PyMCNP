# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:03:58 2024

@author: mayll
"""

import pymcnp
import numpy as np
import pandas as pd

file = 'data/input_files/F1F8.o'
out = pymcnp.outp.ReadOutput(file)
all_lines = out.all_lines


erg_idx = []
tme_idx = []
tly_idx = []
par_idx = []
blank_idx = []
total_idx = []
tally_type = []
particle = []
tally_info = []


print('Reading output file...')
for i, line in enumerate(all_lines):
    tmp = line.split()
    if len(tmp) == 0:
        blank_idx.append(i)
    if 'energy' in tmp and len(tmp) == 1:
        erg_idx.append(i)
    if 'time' in tmp and len(tmp) == 1:
        tme_idx.append(i)
    if 'total' in tmp and len(tmp) == 3 and (len(erg_idx) > 0 or len(tme_idx) > 0):
        total_idx.append(i)
    if 'tally' in tmp and 'type' in tmp:
        tly_idx.append(i)
        tally_type.append(line)
    if 'particle(s):' in tmp:
        par_idx.append(i)
        particle.append(tmp)

lnp = sorted(total_idx + erg_idx + tme_idx)
lnp = np.array(lnp).reshape(-1, 2)
lnp[:, 0] = lnp[:, 0] + 1  # remove keyword header

blank = np.array(blank_idx)

tly_info_idx = []
lines_before_tly = 10  # look for empty lines before tally
for x in lnp:  # this won't work for short tallies
    tly_info_idx.append(blank[(blank < x[0]) & (blank > x[0] - lines_before_tly)].min())
tly_info_idx = np.array(tly_info_idx) + 1


tally1 = all_lines[lnp[0][0] : lnp[0][1]]
tally1_info = all_lines[tly_info_idx[0] : lnp[0][0] - 1]

tally2 = all_lines[lnp[1][0] : lnp[1][1]]
tally2_info = all_lines[tly_info_idx[1] : lnp[1][0] - 1]


def parse_info(lst):
    nps, tally_type, tally_name, description, particle = 0, 0, 0, 0, 0
    other = []
    for line in lst:
        tmp = line.split()
        if len(tmp) == 0:
            continue
        if '1tally' in tmp and 'nps' in tmp and len(tmp) >= 5:
            tally_name = f'F{tmp[1]}'
            nps = int(tmp[-1])
        elif 'tally' in tmp and 'type' in tmp:
            tally_type = f'F{tmp[2]}'
            description = ' '.join(tmp[3:])
        elif 'particle(s):' in tmp and len(tmp) > 1:
            particle = ' '.join(tmp[1:])
        else:
            other.append(' '.join(tmp))
    other_info = ' |***| '.join(other)
    dic = {
        'nps': nps,
        'tally_type': tally_type,
        'tally_name': tally_name,
        'description': description,
        'particle': particle,
        'other': other_info,
    }
    return dic


# initialize dataframe
cols = [
    'tally_name',
    'tally_type',
    'particle',
    'line_start',
    'line_end',
    'description',
    'nps',
    'other',
]


df = pd.DataFrame(columns=cols)

for info, data in zip(tly_info_idx, lnp):
    info_start = info
    info_end = data[0] - 1
    data_start = data[0]
    data_end = data[1]
    info_lst = all_lines[info_start:info_end]
    info_dict = parse_info(info_lst)
    info_dict['line_start'] = data_start
    info_dict['line_end'] = data_end
    df.loc[len(df)] = info_dict


s = df['line_start'][0]
e = df['line_end'][0]
corpus = all_lines[s:e]
corpus_np = np.array([x.split() for x in corpus], dtype=float)
df1 = pd.DataFrame(columns=['energy', 'cts', 'error'], data=corpus_np)
