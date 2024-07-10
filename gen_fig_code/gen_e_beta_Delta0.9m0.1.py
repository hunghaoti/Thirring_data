import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


Delta_2, m2 = 0.9, 0.1

dt = 0.01
param = 'Delta' + str(Delta_2) + 'm' + str(m2)
data_path = '../data_submit/Fig3/' + param
save_fig_name = '../figs/energyVsBeta_ma' + str(m2) +'_Delta' + str(Delta_2) + '_2'

# plot beta-e curve
data = pd.read_csv(data_path + '/beta_e.csv')
plt.plot(data.beta, data.e, color = 'blue', label = 'thermal equilibrium', zorder = 0)
plt.ylim([-0.47, 0.0])
plt.xlim([0, 10])

# shoe selective cases
data = pd.read_csv(data_path + '/beta_e_cases.csv')
plt.scatter(data.beta, data.e, s = 80, color = 'green', \
        marker = '*', label = 'initial energies')
xs2 = []
ys2 = []
for i in range(0, len(data.is_dqpt)):
    if data.is_dqpt[i] == 1:
        xs2.append(data.beta[i])
        ys2.append(data.e[i])
plt.scatter(xs2, ys2, s= 90, marker = 'o', facecolors='none', \
        edgecolors='olivedrab', label = 'DQPT')
plt.text(data.beta[0] + 0.2, data.e[0], \
        '$\Delta_1=' + str(data.Delta_1[0]) + ', m_1a=' + str(data.m1[0]) +'$')
plt.text(data.beta[1] + 0.2, data.e[1], \
        '$\Delta_1=' + str(data.Delta_1[1]) + ', m_1a=' + str(data.m1[1]) +'$')
plt.text(data.beta[2] + 0.4, data.e[2]-0.015, \
        '$\Delta_1=' + str(data.Delta_1[2]) + ', m_1a=' + str(data.m1[2]) +'$')
plt.text(data.beta[3] + 0.5, data.e[3], \
        '$\Delta_1=' + str(data.Delta_1[3]) + ', m_1a=' + str(data.m1[3]) +'$')
plt.text(data.beta[4] + 0.2, data.e[4], \
        '$\Delta_1=' + str(data.Delta_1[4]) + ', m_1a=' + "{:g}".format(data.m1[4]) +'$')

# Plot critical value
data = pd.read_csv(data_path + '/e_crit.csv')
plt.axhline(y=data.e_c[0], color='gray', linestyle='--', zorder = 0, \
        label = '$E_c/N=' + "{:.4f}".format(data.e_c[0]) + '$')

plt.xlabel('$\\beta$', fontsize = 12)
plt.ylabel('$E/N$', fontsize = 12)
plt.title('$m_2a=' + str(m2) + ', \Delta_2=' + str(Delta_2) + '$', fontsize = 14)
plt.legend(loc = 'upper right')


plt.savefig(save_fig_name + '.pdf')
#plt.savefig(save_fig_name + '.png')
#plt.show()
plt.close()

