import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from pylab import cm
import matplotlib.gridspec as gridspec
import itertools

marker = itertools.cycle((',', '+', '.', 'o', '*'))

mpl.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['font.size'] = 15
plt.rcParams['figure.figsize'] = [15, 5]
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 17
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.markersize'] = 6
plt.rcParams['legend.fontsize'] = 15
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.linewidth'] = 2

colors = cm.get_cmap('Set1', 9)

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(1, 2, 2)

ax.xaxis.set_tick_params(which='major', size=10, width=2,
                         direction='in', top='on')
ax.xaxis.set_tick_params(which='minor', size=7, width=2,
                         direction='in', top='on')
ax.yaxis.set_tick_params(which='major', size=10, width=2,
                         direction='in', right='on')
ax.yaxis.set_tick_params(which='minor', size=7, width=2,
                         direction='in', right='on')
ax1.xaxis.set_tick_params(which='major', size=10, width=2,
                         direction='in', top='on')
ax1.xaxis.set_tick_params(which='minor', size=7, width=2,
                         direction='in', top='on')
ax1.yaxis.set_tick_params(which='major', size=10, width=2,
                         direction='in', right='on')
ax1.yaxis.set_tick_params(which='minor', size=7, width=2,
                         direction='in', right='on')

fn = ['0', '1', '2', '3', '4', '5']
dt = ['0.01', '0.1', '0.2', '0.3', '0.4', '0.5']
for i in range(5):
    filename = '../data/conv/'+str(fn[i])+'/KE.dat'
    t, K = np.loadtxt(filename, unpack=True)
    filename = '../data/conv/'+str(fn[i])+'/PE.dat'
    t, U = np.loadtxt(filename, unpack=True)
    filename = '../data/conv/'+str(fn[i])+'/P.dat'
    t, P = np.loadtxt(filename, unpack=True)

    E = K + U
    ax.plot(t, abs((E-E[0])/E[0]), color=colors(i), label=r'$dt=$'+dt[i])
    #  ax.plot(t, K, color=colors(0), label='K')
    #  ax.plot(t, U, color=colors(1), label='U')
    #  ax.plot(t, E, color=colors(i), label='E')
    #  ax1.plot(t, (P-P[0])/P[0]*100, color=colors(i), label=r'$dt=$'+dt[i])
    ax1.plot(t, P, color=colors(i), label=r'$dt=$'+dt[i])


ax.set_yscale('log')
#  ax1.set_yscale('log')
ax.set_title(r'$Energy$', fontsize=20)
ax.set_xlabel(r'$time \ [1/\omega_p]$', fontsize=20)
ax.set_ylabel(r'$\varepsilon$', fontsize=20)
ax1.set_title(r'$Momentum$', fontsize=20)
ax1.set_xlabel(r'$time \ [1/\omega_p]$', fontsize=20)
ax1.set_ylabel(r'$P \ [m_e\lambda_D/\omega_p]$', fontsize=20)
ax.legend()
ax1.legend()

plt.tight_layout()
plt.savefig('figures/conv.eps')
plt.savefig('figures/conv.png', dpi=1200)
plt.show()
