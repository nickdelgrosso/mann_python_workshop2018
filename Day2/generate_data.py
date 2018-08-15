import os
import numpy as np

# Make a directory: os.mkdir()
# Change working directory (cd): os.chdir()
# Get current working directory: os.getcwd()

os.mkdir('Data')

print(os.getcwd())

for idx in range(1000):
    data = np.random.randn(100)
    np.savetxt('Data/data{}.txt'.format(idx), data)
