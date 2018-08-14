import pandas as pd
import matplotlib.pyplot as plt
import sys

filename, imagename = sys.argv[1:]


# Load Data
df = pd.read_csv(filename)
df.head()

# Plot Data
df['Time'].hist()
plt.title('Nature Results')
plt.savefig(imagename)
