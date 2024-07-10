import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


def Interpolate(tab, x):
    xs = tab['e']
    ys = tab['beta']
    y = 1000
    if x <= min(xs):
        y = max(ys)
        return y
    elif (x >= max(xs)):
        y = min(ys)
        return y
    else:
        for i in range(0, len(xs)-1):
            if x <= xs[i] and x > xs[i+1]:
                y = (x-xs[i]) / (xs[i+1]-xs[i]) * (ys[i+1]-ys[i]) + ys[i]
                return y
    return y


Delta_2 = -0.9
m2 = 0.1
param = 'Delta' + str(Delta_2) + 'm' + str(m2)
data_path = '../data_submit/'
e_crit_file_name = data_path + 'Fig3/' + param + '/e_crit.csv'
e_crit = pd.read_csv(e_crit_file_name).e_c[0]

E_b_table_str = data_path + 'Fig3/' + param + '/beta_e.csv'
E_b_dat = pd.read_csv(E_b_table_str)
b_crit = Interpolate(E_b_dat, e_crit)
    
dat = pd.read_csv(data_path + 'dqpt_data.csv')

dat = dat.loc[
    (dat['Delta_2'] == Delta_2) &
    (dat['m2'] == m2) &
    (dat['dqpt'] == 1)
]

e0s = []
e1s = []
e2s = []
e3s = []
ens = []
b0s = []
b1s = []
b2s = []
b3s = []
bns = []
t0s = []
t1s = []
t2s = []
t3s = []
tns = []
for i, row in dat.iterrows():
    e, t_list = row['e_vumps'], eval(row['times'])
    e = e - 0.25 * Delta_2
    b = Interpolate(E_b_dat, e)
    tidx = 0
    for t in t_list:
        if tidx == 0:
            e0s.append(e)
            b0s.append(b)
            t0s.append(t)
        elif tidx == 1:
            e1s.append(e)
            b1s.append(b)
            t1s.append(t)
        elif tidx == 2:
            e2s.append(e)
            b2s.append(b)
            t2s.append(t)
        elif tidx == 3:
            e3s.append(e)
            b3s.append(b)
            t3s.append(t)
        else:
            ens.append(e)
            bns.append(b)
            tns.append(t)
        tidx = tidx + 1


plt.axvline(x = b_crit, color = 'gray', linestyle = '-.', alpha = 0.7 ,\
        label = '$\\beta_c\\approx' + "{:.2f}".format(b_crit) + '$' )
if Delta_2 == -0.9:
    speci_Delta1 = 0.1
    speci_m1 = 0.7
    e = dat.loc[
        (dat['Delta_1'] == speci_Delta1) &
        (dat['m1'] == speci_m1)
    ]['e_vumps'].values[0]
    b = Interpolate(E_b_dat, e - 0.25 * Delta_2)
    plt.axvline(x = b, color = 'black', linestyle = 'dashed',\
            label = '$\\beta=' + "{:.3f}".format(b) + '$')
    plt.text(0.13, 7,\
        '$(m_1a, \Delta_1)=(' + str(speci_m1) + ', ' + str(speci_Delta1) + ')\\rightarrow$')
plt.legend(bbox_to_anchor=(0.25, 0.60))
plt.scatter(b0s, t0s, s=5, c='b', label='$t_0$')
plt.scatter(b1s, t1s, s=5, c='orange', label='$t_1$')
plt.scatter(b2s, t2s, s=5, c='g', label='$t_2$')
plt.scatter(b3s, t3s, s=5, c='r', label='$t_3$')
plt.scatter(bns, tns, s=5, c='gray', label='$t_{n>3}$')


plt.title('$m_2a=$' + str(m2) + ', $\Delta_2=$' + str(Delta_2), fontsize = 14)
plt.xlabel('$\\beta$', fontsize = 12)
plt.ylabel('$t$', fontsize = 12)
save_path = '../figs/'
#plt.savefig(save_path + 'g' + str(g1) + '_ts_sep_branch.png')
plt.savefig(save_path + 'Delta' + str(Delta_2) + '_ts_sep_branch.pdf')
#plt.show()

