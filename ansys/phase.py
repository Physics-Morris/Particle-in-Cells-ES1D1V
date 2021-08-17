import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from pylab import cm
import matplotlib.gridspec as gridspec

mpl.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['font.size'] = 17
plt.rcParams['figure.figsize'] = [5.6, 4]
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['lines.markersize'] = 6
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.linewidth'] = 3

colors = cm.get_cmap('Dark2', 9)

#  ax1 = fig.add_subplot(2, 3, 1)
#  ax2 = fig.add_subplot(2, 3, 2)
#  ax3 = fig.add_subplot(2, 3, 4)
#  ax4 = fig.add_subplot(2, 3, 5)
#  ax5 = fig.add_subplot(2, 3, 6)

x = np.loadtxt('../data/0612/r.dat')
v = np.loadtxt('../data/0612/v.dat')
# rho = np.loadtxt('../data/0612/rho.dat')
# phi = np.loadtxt('../data/0612/phi.dat')
# E = np.loadtxt('../data/0612/E.dat')
# t, KE = np.loadtxt('../data/0612/KE.dat', unpack=True)
# t, PE = np.loadtxt('../data/0612/PE.dat', unpack=True)

xx = np.arange(0, 2*np.pi/0.612, .7)

for i in range(0, x.shape[0]):
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(x[i][:], v[i][:], '.', markersize=.5, color=colors(0))

    # ax1.set_title('Phase space')
    # ax1.set_xlabel(r'$x \ [\lambda_d]$')
    # ax1.set_ylabel(r'$v \ [\lambda_d \times \omega_p]$')

    ax1.set_ylim(-2.5, 2.5)

    plt.tight_layout()
    plt.axis('off')
    num = '{0:04}'.format(i)
    filename = '../figures/video/' + str(num) + '.png'
    plt.savefig(filename, dpi=300)
    ax1.clear()
    plt.close()
#  plt.show()
