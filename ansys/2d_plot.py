import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from pylab import cm

mpl.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['font.size'] = 16
plt.rcParams['figure.figsize'] = [5.6, 4]
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.markersize'] = 6
plt.rcParams['legend.fontsize'] = 13
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.linewidth'] = 1

colors = cm.get_cmap('Set1', 9)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.xaxis.set_tick_params(which='major', size=5, width=1,
                         direction='in', top='on')
ax.xaxis.set_tick_params(which='minor', size=3, width=1,
                         direction='in', top='on')
ax.yaxis.set_tick_params(which='major', size=5, width=1,
                         direction='in', right='on')
ax.yaxis.set_tick_params(which='minor', size=3, width=1,
                         direction='in', right='on')

ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(20))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(.05))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(.01))

n, x = np.loadtxt('a.dat', unpack=True)
ax.plot(n, x, '*', color=colors(0))
ax.plot(n, x, '-', color=colors(1))
ax.set_xlabel('$n$', labelpad=10)
ax.set_ylabel(r'$I_{Simpson}$', labelpad=10)
ax.set_title(r'$I=\int_0^{\infty} \dfrac{1}{1+x^4}$')
ax.set_ylim(1, 1.13)

plt.tight_layout()
plt.savefig('../figure/1a.pdf')
plt.show()
