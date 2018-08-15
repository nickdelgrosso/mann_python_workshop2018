import os
from os import path
from glob import glob
import numpy as np
import matplotlib.pyplot as plt

savedir = 'Results'
os.mkdir(savedir)

# List all files in a directory: os.listdir()
filenames = glob('Data/*.txt')

for filename in filenames:
    basename = path.splitext(path.basename(filename))[0]

    data = np.loadtxt(filename)

    plt.figure()
    plt.hist(data)
    plt.title(basename)
    plt.savefig(savedir + '/histogram_{}.pdf'.format(basename))
