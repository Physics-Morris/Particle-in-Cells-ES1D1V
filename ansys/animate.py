import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from pylab import cm
import matplotlib.gridspec as gridspec

mpl.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['font.size'] = 17
plt.rcParams['figure.figsize'] = [15, 15]
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
rho = np.loadtxt('../data/0612/rho.dat')
phi = np.loadtxt('../data/0612/phi.dat')
E = np.loadtxt('../data/0612/E.dat')
t, KE = np.loadtxt('../data/0612/KE.dat', unpack=True)
t, PE = np.loadtxt('../data/0612/PE.dat', unpack=True)

xx = np.arange(0, 2*np.pi/0.612, .7)

for i in range(0, x.shape[0]):
    fig = plt.figure()
    ax1 = fig.add_subplot(3, 2, 1)
    ax2 = fig.add_subplot(3, 2, 2)
    ax3 = fig.add_subplot(3, 2, 3)
    ax4 = fig.add_subplot(3, 2, 4)
    ax5 = fig.add_subplot(3, 2, 5)
    ax6 = fig.add_subplot(3, 2, 6)
    ax1.plot(x[i][:], v[i][:], '.', markersize=.5, color=colors(0))
    ax2.hist(v[i], bins=500, histtype='bar', color=colors(1))
    ax3.plot(xx, rho[i][:], color=colors(2))
    ax4.plot(xx, phi[i][:], color=colors(3))
    ax5.plot(xx, E[i][:], color=colors(4))
    ax6.plot(t[:i], KE[:i], color=colors(5), label='K')
    ax6.plot(t[:i], PE[:i], color=colors(6), label='U')
    ax6.plot(t[:i], PE[:i]+KE[:i], color=colors(7), label='$E_{total}$')

    ax1.set_title('Phase space')
    ax1.set_xlabel(r'$x \ [\lambda_d]$')
    ax1.set_ylabel(r'$v \ [\lambda_d \times \omega_p]$')
    ax2.set_title('Velocity ditribution')
    ax2.set_xlabel(r'$v \ [\lambda_d \times \omega_p]$')
    ax2.set_ylabel(r'$N$')
    ax3.set_title('Nomalized density')
    ax3.set_xlabel(r'$x \ [\lambda_d]$')
    ax3.set_ylabel(r'$\rho$')
    ax4.set_title('Potential')
    ax4.set_xlabel(r'$x \ [\lambda_d]$')
    ax4.set_ylabel(r'$\phi$')
    ax5.set_title('Electric field')
    ax5.set_xlabel(r'$x \ [\lambda_d]$')
    ax5.set_ylabel(r'$E$')
    ax6.set_title('Energy')
    ax6.set_xlabel(r'$time \ [\omega_p^{-1}]$')
    ax6.set_ylabel(r'$Energy$')
    ax6.legend()

    ax1.set_ylim(-2.5, 2.5)
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(0, 3000)
    ax3.set_ylim(-.8, .8)
    ax4.set_ylim(-1.4, 1.4)
    ax5.set_ylim(-.5, .5)
    ax6.set_ylim(-.5, 6)

    plt.tight_layout()
    num = '{0:04}'.format(i)
    filename = '../figures/video/' + str(num) + '.png'
    plt.savefig(filename)
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    ax5.clear()
    ax6.clear()
    plt.close()
#  plt.show()
