import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import string
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fig, axes = plt.subplots(nrows=1, ncols=2)
fig.set_figheight(5)
fig.set_figwidth(12)

# fig a
ax = axes.flatten()[0]

Delta_2, m2 = -0.9, 0.1

dt = 0.01
param = 'Delta' + str(Delta_2) + 'm' + str(m2)
data_path = '../data_submit/Fig3/' + param
save_fig_name = '../figs/energyVsBeta_ma'

# plot beta-e curve
data = pd.read_csv(data_path + '/beta_e.csv')
ax.plot(data.beta, data.e, color = 'blue', label = 'thermal equilibrium', zorder = 0)
ax.set_ylim([-0.25, 0.05])
ax.set_xlim([0, 5.2])

# shoe selective cases
data = pd.read_csv(data_path + '/beta_e_cases.csv')
ax.scatter(data.beta, data.e, s = 80, color = 'green', \
        marker = '*', label = 'initial energies')
xs2 = []
ys2 = []
for i in range(0, len(data.is_dqpt)):
    if data.is_dqpt[i] == 1:
        xs2.append(data.beta[i])
        ys2.append(data.e[i])
ax.scatter(xs2, ys2, s= 90, marker = 'o', facecolors='none', \
        edgecolors='olivedrab', label = 'DQPT')
ax.text(data.beta[0] + 0.1, data.e[0] - 0.015, \
        '$\Delta_1=' + str(data.Delta_1[0]) + ', m_1a=' + str(data.m1[0]) +'$')
ax.text(data.beta[1] + 0.1, data.e[1], \
        '$\Delta_1=' + str(data.Delta_1[1]) + ', m_1a=' + str(data.m1[1]) +'$')
ax.text(data.beta[2] + 0.1, data.e[2], \
        '$\Delta_1=' + str(data.Delta_1[2]) + ', m_1a=' + str(data.m1[2]) +'$')

# Plot critical value
data = pd.read_csv(data_path + '/e_crit.csv')
ax.axhline(y=data.e_c[0], color='gray', linestyle='--', zorder = 0, \
        label = '$E_c/N=' + "{:.4f}".format(data.e_c[0]) + '$')

ax.set_xlabel('$\\beta$', fontsize = 12)
ax.set_ylabel('$E/N$', fontsize = 12)
ax.set_title('$m_2a=' + str(m2) + ', \Delta_2=' + str(Delta_2) + '$', fontsize = 14)
ax.legend(loc = 'upper right')


#fig b
ax = axes.flatten()[1]
Delta_2, m2 = 0.9, 0.1

dt = 0.01
param = 'Delta' + str(Delta_2) + 'm' + str(m2)
data_path = '../data_submit/Fig3/' + param

# plot beta-e curve
data = pd.read_csv(data_path + '/beta_e.csv')
ax.plot(data.beta, data.e, color = 'blue', label = 'thermal equilibrium', zorder = 0)
ax.set_ylim([-0.47, 0.0])
ax.set_xlim([0, 10])

# shoe selective cases
data = pd.read_csv(data_path + '/beta_e_cases.csv')
ax.scatter(data.beta, data.e, s = 80, color = 'green', \
        marker = '*', label = 'initial energies')
xs2 = []
ys2 = []
for i in range(0, len(data.is_dqpt)):
    if data.is_dqpt[i] == 1:
        xs2.append(data.beta[i])
        ys2.append(data.e[i])
ax.scatter(xs2, ys2, s= 90, marker = 'o', facecolors='none', \
        edgecolors='olivedrab', label = 'DQPT')
ax.text(data.beta[0] + 0.2, data.e[0], \
        '$\Delta_1=' + str(data.Delta_1[0]) + ', m_1a=' + str(data.m1[0]) +'$')
ax.text(data.beta[1] + 0.2, data.e[1], \
        '$\Delta_1=' + str(data.Delta_1[1]) + ', m_1a=' + str(data.m1[1]) +'$')
ax.text(data.beta[2] + 0.4, data.e[2]-0.015, \
        '$\Delta_1=' + str(data.Delta_1[2]) + ', m_1a=' + str(data.m1[2]) +'$')
ax.text(data.beta[3] + 0.5, data.e[3], \
        '$\Delta_1=' + str(data.Delta_1[3]) + ', m_1a=' + str(data.m1[3]) +'$')
ax.text(data.beta[4] + 0.2, data.e[4], \
        '$\Delta_1=' + str(data.Delta_1[4]) + ', m_1a=' + "{:g}".format(data.m1[4]) +'$')

# Plot critical value
data = pd.read_csv(data_path + '/e_crit.csv')
ax.axhline(y=data.e_c[0], color='gray', linestyle='--', zorder = 0, \
        label = '$E_c/N=' + "{:.4f}".format(data.e_c[0]) + '$')

ax.set_xlabel('$\\beta$', fontsize = 12)
ax.set_ylabel('$E/N$', fontsize = 12)
ax.set_title('$m_2a=' + str(m2) + ', \Delta_2=' + str(Delta_2) + '$', fontsize = 14)
ax.legend(loc = 'upper right')


for n, ax in enumerate(axes.flatten()):
    ax.text(-0.14, 1.1, '(' + string.ascii_lowercase[n] + ')', transform=ax.transAxes,
            size=14)

plt.subplots_adjust(hspace=0.35, wspace=0.27, left=0.08, right = 0.97)
plt.savefig(save_fig_name + '.pdf')
#plt.savefig(save_fig_name + '.png')
#plt.show()
#plt.close()

