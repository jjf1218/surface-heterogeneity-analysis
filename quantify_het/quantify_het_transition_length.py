"""
A code to quantify surface heterogeneity
using length between transitions
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy import stats
import json

# reset matplotlib to defalt settings
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)

# import constants and funcs by going up one, importing, then going back down
os.chdir(os.path.join("D:",os.sep,"surface-heterogeneity-analysis"))
from constants import cnst
import funcs as fn
os.chdir(os.path.join("create_surfaces"))

# define constants - these are changed in class cnst in constants.py
label = cnst.label
root = cnst.root
reso = cnst.reso
conv = cnst.conv
iceT = cnst.iceT
waterT = cnst.waterT
iceR = cnst.waterR
waterR =cnst.waterR


# clear all plots
plt.close('all')

##### load maps and calculate transition to compare #####

# load the array text file from the surface folder
# current options: checkerboard, strips, SIPS200, SIPS10k
project = 'SIPS200'
lp = os.path.join(root, 'surfaces','SIPS200_templates','no_ponds')
trans_stats = os.path.join(root,'results','transition_scale_txts',project)
s_cutoff = -3


################# all options should be able to be set above #################

# set strings used to save variables from parameters set above
# set filename and titlestring for saving
fname = f'{pattern}'
print(f"  Filename to be used: {fname}")

# load the array
arr = np.loadtxt(os.path.join(lp,'T_s_remote_ice.txt'))
print(f"\n  Importing from {os.path.join(lp,'T_s_remote_ice.txt')}")

# change resolution of array - if needed
if int(reso) != np.shape(arr)[0]:
    print(f"\n    Converting array from {np.shape(arr)} to reso={reso}")
    arr = fn.conv_np_array_reso(arr, int(reso))

# get transition statistics in x and y
transtats_x = fn.calculate_transition_statistics(arr)
transtats_y = fn.calculate_transition_statistics(arr.T)

# savepath for saving this data
sp_x = os.path.join(root,'results','transition_scale_txts',f'{pattern}_transcales_x.txt')
sp_y = os.path.join(root,'results','transition_scale_txts',f'{pattern}_transcales_y.txt')

# save teh files
with open(sp_x, 'w') as file:
     file.write(json.dumps(transtats_x)) # use `json.loads` to do the reverse
file.close()

with open(sp_y, 'w') as file:
     file.write(json.dumps(transtats_y)) # use `json.loads` to do the reverse
file.close()



























