import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from pylab import cm
from scipy.fft import fft

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

#  ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.25))
#  ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.05))
#  ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(.1))
#  ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(.02))

##############################################################3
X = []
Y = []
for a in np.arange(0, 1.3, .0001):
    #  coef = [1, 0, -.5*a**2-2, 0, a**4/16-a**2/2]
    coef = [1, 0, -2*a**2-1, 0, a**4-a**2]
    sol = np.roots(coef)
    X.append(a)
    Y.append(sol[2].imag)

print('maximum at', X[np.argmax(Y)], ':', Y[np.argmax(Y)])
#########################################################
E = np.loadtxt('../data/0612/E.dat')
#  sumE = []
#  for i in range(499):
   #  sumE.append(sum(E[i][:]))
#  ax.plot(sumE)
##############################################################3
#  fft space domain
tmin = 0
tmax = 50
dt = 0.1
NG = E.shape[1]
kspace = np.empty([int(tmax/dt)-int(tmin/dt), NG-1])
for i in range(int(tmax/dt)-int(tmin/dt)):
    kspace[i, :] = np.log(abs(fft(E[i][:-1])))

kk = 0.6124
L = 2. * np.pi / kk
dx = L / NG
k = np.arange(0., np.pi/dx, np.pi/dx/(NG//2))

t = np.arange(tmin, tmax, dt)
growth = []
B = []
for i in range(0, int(NG//2)):
    m, b = np.polyfit(t, kspace[:, i], 1)
    growth.append(m)
    B.append(b)
ax.plot(t, np.exp(kspace[:, 1]), label='Simulation (mode 1)')
tt = np.arange(0, 16, 0.1)
ax.plot(tt, np.exp(Y[np.argmax(Y)]*tt-4.2), color=colors(0), label='Theory (max. growth rate)')

ax.set_xlabel(r'$time \ [\omega_p]$')
ax.set_ylabel(r'$E_x$')
ax.set_title(r'$Linear \ growth \ rate$')
ax.legend()
ax.set_yscale('log')

plt.tight_layout()
plt.savefig('figures/mode1.eps')
plt.savefig('figures/mode1.png', dpi=1200)
plt.show()
