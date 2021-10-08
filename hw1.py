import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy
from scipy import stats

d = stats.norm.rvs(loc = 3.0, scale = .01, size = 100000)

plt.tick_params(labelsize = 24)

fig, axs = plt.subplots(1, 2, figsize=(20,7))
x = np.linspace(2.95, 3.05, 1000)

axs[1].set_yscale('log')

for ax in axs:
    ax.hist(d, 50, density = True)
    ax.set_xlim([2.95,3.05])
    ax.set_xlabel("$\sigma$")
    ax.plot(x, stats.norm.pdf(x, loc = 3, scale = 0.01), linewidth = 8, alpha = 0.7)

plt.show()