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

ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.25))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.05))
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(.1))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(.02))

##############################################################3
X = []
Y = []
for a in np.arange(0, 1.3, .0001):
    #  coef = [1, 0, -.5*a**2-2, 0, a**4/16-a**2/2]
    coef = [1, 0, -2*a**2-1, 0, a**4-a**2]
    sol = np.roots(coef)
    X.append(a)
    Y.append(sol[2].imag)

print('maximum at', X[np.argmax(Y)])
ax.set_xlabel(r'$\beta \ (kv_0/\omega_p)$')
ax.set_ylabel(r'$x \ (\omega / \omega_p)$')
#########################################################
flist=['0316', '0387', '0459', '0612', '0765', '0918', '1071', '1224']
tminlist=[0, 0, 0, 3, 1, 0, 0, 0, 0]
tmaxlist=[26, 23, 17, 17, 20, 23.5, 20, 50, 50]
klist=[0.3163, 0.3878, 0.4593, 0.6124, 0.7655, 0.918, 1.0717, 1.224]
growth_rate=[]

for j in range(0, 8): 
    ##############################################################3
    E = np.loadtxt('../data/'+str(flist[j])+'/E.dat')
    #  sumE = []
    #  for i in range(499):
       #  sumE.append(sum(E[i][:]))
    #  ax.plot(sumE)
    ##############################################################3
    #  fft space domain
    tmin = tminlist[j]
    tmax = tmaxlist[j]
    dt = 0.1
    NG = E.shape[1]
    kspace = np.empty([int(tmax/dt)-int(tmin/dt), NG-1])
    for i in range(int(tmax/dt)-int(tmin/dt)):
        kspace[i, :] = np.log(abs(fft(E[i][:-1])))

    kk = klist[j]
    L = 2. * np.pi / kk
    dx = L / NG
    k = np.arange(0., np.pi/dx, np.pi/dx/(NG//2))
    #  for i in range(0, 50, 1):
        #  ax.plot(k, kspace[i, 0:(int(NG//2))])

    t = np.arange(tmin, tmax, dt)
    growth = []
    B = []
    for i in range(0, int(NG//2)):
        m, b = np.polyfit(t, kspace[:, i], 1)
        growth.append(m)
        B.append(b)
        #  ax.plot(t, kspace[:, i])
        #  ax.plot(t, m*t+b, label=i)
    growth_rate.append(growth[1])
    #  ax.plot(t, kspace[:, 1])
    #  ax.plot(t, growth[1]*t+B[1], label=i)
ax.plot(klist, growth_rate, '*', color=colors(1), markersize=10, label='Simulation')
ax.plot(X, Y, '-', color=colors(0), label='Theory')

ax.set_title(r'$Growth \ rate$')
ax.legend()

plt.tight_layout()
plt.savefig('figures/growth_rate.eps')
plt.savefig('figures/growth_rate.png', dpi=1200)
plt.show()
