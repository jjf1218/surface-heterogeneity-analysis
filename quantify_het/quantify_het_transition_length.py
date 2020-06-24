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
ice = cnst.ice
water = cnst.water

# clear all plots
plt.close('all')

##### load maps and calculate transition to compare #####

# load the array text file from the surface folder
# current options: checkerboard, strips
#                 beaufo_2000_aug31, esiber_2000_jul06
#                 cafram_2000_aug07
pattern = 'beaufo_2000_aug31'
#lp = os.path.join(root, 'surfaces',pattern,'arrays'); s_cutoff = -17
#lp = os.path.join(root,'surfaces',pattern,'arrays','perp'); s_cutoff = -22
lp = os.path.join(root, 'surfaces',pattern,'arrays'); s_cutoff = -4
#checkerboard=-17, strips=-22


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
spx = os.path.join(root,'results','transition_scale_txts',f'{pattern}_transcales_x.txt')
spy = os.path.join(root,'results','transition_scale_txts',f'{pattern}_transcales_y.txt')

import json

with open(spx, 'w') as file:
     file.write(json.dumps(transtats_x)) # use `json.loads` to do the reverse
file.close()

test = json.load(open(spx))











#%%
### finish plotting and save ###


# PDF using a Gaussian kernel of both water and ice transitions in x and y
arr_total = pd.Series(tsx_list[arr][ice] + tsx_list[arr][water]
                    + tsy_list[arr][ice] + tsy_list[arr][water])
arr_total.plot.density(label=f"{pattern}",legend='best')
plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_{pattern}_all_pdf.png'))
plt.close()

# PDF using a Gaussian kernel of only ice transitions in x and y
arr_total = pd.Series(tsx_list[arr][ice] + tsy_list[arr][ice])
arr_total.plot.density(label=f"{patterns[arr]}",legend='best')
plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_{pattern}_ice_pdf.png'))
plt.close()

# PDF using a Gaussian kernel of only water transitions in x and y
arr_total = pd.Series(tsx_list[arr][water] + tsy_list[arr][water])
arr_total.plot.density(label=f"{patterns[arr]}",legend='best')
plt.savefig(os.path.join(root,'results','transition_pdfs','comparison_{pattern}_water_pdf.png'))
plt.close()

for i in range(len(tsx_list)):
    arr_total = tsx_list[i][ice]+tsx_list[i][water] + tsy_list[i][ice] + tsy_list[i][water]
    # histrogram using raw data
    # fixed bin size
    bins = np.arange(0, 100, 5) # fixed bin size
    plt.hist(arr_total, bins=bins, alpha=0.5)
    plt.title('Histogram for Transition Lengths (fixed bin size)')
    plt.xlabel('Length (bin size = 5)')
    plt.ylabel('Count')
    plt.savefig(os.path.join(root,'results','transition_pdfs',f'{patterns[i]}_hist.png'))
    plt.close()




















