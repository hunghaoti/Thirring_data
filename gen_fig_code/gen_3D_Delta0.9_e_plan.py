import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

Delta_2, m2 = 0.9, 0.1

param = 'Delta' + str(Delta_2) + 'm' + str(m2)
data_path = '../data_submit/Fig4/'
file_name = data_path + param + '_E.csv'
data_e = pd.read_csv(file_name)
data_dqpt = pd.read_csv('../data_submit/dqpt_data.csv')
data_dqpt=data_dqpt[data_dqpt['Delta_2']==Delta_2]
data_dqpt=data_dqpt[data_dqpt['m2']==m2]
data_dqpt=data_dqpt[data_dqpt['m1']<=1.5]
data_dqpt=data_dqpt[data_dqpt['m1']>=0]
data_dqpt=data_dqpt[data_dqpt['Delta_1']>=-1]
data_dqpt=data_dqpt[data_dqpt['Delta_1']<=1]
data_dqpt=data_dqpt.drop(['times'], axis=1)
data_dqpt=data_dqpt.drop(['Delta_2'], axis=1)
data_dqpt=data_dqpt.drop(['m2'], axis=1)

data_e = pd.merge(left = data_e, right = data_dqpt, how = 'left')

data_e_crit = pd.read_csv('../data_submit/Fig3/' + param + '/e_crit.csv')
e_crit=data_e_crit.e_c[0]
xx, yy = np.meshgrid([-1, 1], [0, 1.5])
zz = yy*0 + e_crit

fig = plt.figure(1, figsize = (8, 5))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(xx, yy, zz, alpha = 0.5, color = 'gray')
Z = data_e.pivot_table(index='Delta_1', columns='m1', values='e').T.values
X_unique = np.sort(data_e.Delta_1.unique())
Y_unique = np.sort(data_e.m1.unique())
X, Y = np.meshgrid(X_unique, Y_unique)


CS = ax.plot_surface(X, Y, Z, cmap=cm.plasma, alpha = 0.5, zorder = 10)#, norm=norm)
data_e = data_e[data_e['dqpt'] == 1]
ax.scatter(data_e.Delta_1, data_e.m1, data_e.e, label = 'DQPT', color = 'k')
m1_eq_m2_dat = data_e.loc[
    (data_e['m1'] == m2) &
    (data_e['dqpt'] == 1)
]
ax.scatter(m1_eq_m2_dat.Delta_1, m1_eq_m2_dat.m1, m1_eq_m2_dat.e, 
        label = '$m_1a='+ str(m2) + '$', marker = 'o', s = 80, facecolors='none', edgecolors='k')
CS2 = ax.contour(X, Y, Z, levels = [e_crit], colors = 'black')

# Make a colorbar for the ContourSet returned by the contourf call.
cbar = fig.colorbar(CS, pad = 0.2)
#cbar.ax.set_ylabel('$E/N$')
#ax.clabel(CS2, fontsize=8, colors='black',label = 'crit')
# Add the contour line levels to the colorbar
cbar.add_lines(CS2)

ax.legend(loc = 'best')
ax.set(xlabel='$\Delta_1$', ylabel='$m_1a$', zlabel='$E/N$')
ax.set_title('$m_2a = ' + str(m2) + ', \Delta_2 = ' + str(Delta_2) + '$', fontsize = 14)



#plt.grid()
#plt.savefig('e_g1_'+str(g1)+'_m1_'+str(m1)+'.png')
plt.show()
