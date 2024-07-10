import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline, make_interp_spline
import pandas as pd
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

Delta_2 = 0.9
m2 = 0.1
data = pd.read_csv('../data_submit/dqpt_data.csv')
# here need to check range
data=data[data.Delta_2==Delta_2]
data=data[data.m2==m2]
data=data[data.m1<0.5]
data=data[data.m1>=0]
data=data[data.Delta_1>-1]
data=data[data.Delta_1<=0]

data_y=data[data.dqpt==1]
data_n=data[data.dqpt==0]
plt.figure(figsize=(8.75*0.8,5.99*0.8))
ax = plt.subplot(111)
plt.grid()
#plt.scatter(data_n['g0'], data_n['m0'], marker = '^', label = 'no DQPT')


#draw color phase
x_l = [0,0.1,0.2,0.25,0.3,0.42]
x_u = [0,0.1,0.2,0.25,0.3,0.42]
y_l = [-1,-1,-1,-1,-1,-1]
y_u = [-0.74,-0.76,-0.80,-0.827,-0.853,-0.94]
x_new = np.linspace(0, 0.42, 500)
yl_BSpline = make_interp_spline(x_l, y_l)
yu_BSpline = make_interp_spline(x_u, y_u)
y_l_smooth = yl_BSpline(x_new)
y_u_smooth = yu_BSpline(x_new)
plt.fill_betweenx(x_new, y_l_smooth, y_u_smooth, alpha=0.3, facecolor='blue', label = 'critical')

x_l = [0,0.1,0.2,0.25,0.3,0.42]
x_u = [0,0.04,0.1,0.13,0.2,0.3,0.42]
y_l = [-0.74,-0.76,-0.80,-0.827,-0.853,-0.94]
y_u = [-0.4,-0.6,-0.68,-0.7,-0.76,-0.84,-0.93]
x_new = np.linspace(0, 0.42, 500)
yl_BSpline = make_interp_spline(x_l, y_l)
yu_BSpline = make_interp_spline(x_u, y_u)
y_l_smooth = yl_BSpline(x_new)
y_u_smooth = yu_BSpline(x_new)
plt.fill_betweenx(x_new, y_l_smooth, y_u_smooth, alpha=0.3, edgecolor='gray', facecolor='gray', label='undetermined')

clr = plt.cm.gray(0.2)
x_l = [0,0.04,0.1,0.13,0.2,0.3,0.42]
x_u = [0,0.04,0.1,0.13,0.2,0.3,0.42]
y_u = [-0.4,-0.6,-0.68,-0.7,-0.76,-0.84,-0.93]
y_l = [0.1,0.1,0.1,0.1,0.1,0.1,0.1]
x_new = np.linspace(0, 0.42, 500)
yl_BSpline = make_interp_spline(x_l, y_l)
yu_BSpline = make_interp_spline(x_u, y_u)
y_l_smooth = yl_BSpline(x_new)
y_u_smooth = yu_BSpline(x_new)
plt.fill_betweenx(x_new, y_l_smooth, y_u_smooth, alpha=0.3, facecolor='orange', label = 'gapped')

#DQPT points
plt.scatter(data_y['Delta_1'], data_y['m1'], color = 'black', marker = 'o',\
        label = 'DQPT', clip_on = False, zorder = 10)
plt.ylim([0,0.42])
plt.xlim([-0.96,0.02])
plt.xlabel('$\Delta_1(g)$', fontsize = 12)
plt.ylabel('$m_1 a$', fontsize = 12)
plt.legend(loc='best', fontsize = 10)
title_str = '$\Delta_2 = $' + str(Delta_2) + ', $m_2 = $' + str(m2)
#plt.title(title_str, fontsize = 16)
plt.savefig('../figs/DQPT_scan_Delta2_' + str(Delta_2) + '_m2_' + str(m2) + '_local.pdf')
#plt.savefig('../figs/DQPT_scan_g1_' + str(g1) + '_m1_' + str(m1) + '_local.png')
#plt.show()


