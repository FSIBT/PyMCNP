"""
Example to read a tally with time and energy bins e.g. a pulsed neutron generator
"""

import pathlib

import pymcnp

import matplotlib.pyplot as plt

path = pathlib.Path(__file__).parent / 'files' / 'outp' / 'F1F8.o'
outp = pymcnp.Outp.from_file(path)
df1, df2, df3 = outp.to_dataframe()

print(repr(outp.blocks))
# print(len(df1['21']))

# information about tallies found
# dfi = out.df_info
# df_err, df = out.read_tally(n=0, mode='te')
# 
# df5 = df.loc[1][1:]  # between 0-5 MeV
# df14 = df.loc[2][1:]  # between 5-14 MeV
# plt.figure()
# plt.plot(df5.index, df5, label='0-5 MeV')
# plt.plot(df14.index, df14, label='5-14 MeV')
# plt.xlabel('Time (us)')
# plt.ylabel('counts')
# plt.legend()
# plt.show()
