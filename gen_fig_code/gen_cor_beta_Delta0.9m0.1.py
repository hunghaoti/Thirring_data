import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


Delta_2, m2 = 0.9, 0.1

dt = 0.01
param = 'Delta' + str(Delta_2) + 'm' + str(m2)
data_path = '../data_submit/'
save_fig_name = '../figs/' + param + '_cor'

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


# find critical b
e_crit_file_name = data_path + 'Fig3/' + param + '/e_crit.csv'
e_crit = pd.read_csv(e_crit_file_name).e_c[0]
E_b_table_str = data_path + 'Fig3/' + param + '/beta_e.csv'
E_b_dat = pd.read_csv(E_b_table_str)
b_crit = Interpolate(E_b_dat, e_crit)

#plot beta-correlator
file_name = data_path + '/Fig5/' + param + '_cor.csv'
dat = pd.read_csv(file_name)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dat.beta, dat.C, color = 'blue', s = 15)
ax.errorbar(dat.beta, dat.C, yerr=dat.C_err, color = 'blue',\
                 linestyle='None',capsize=2)
ax.set_ylim([-0.01, 0.3])
ax.set_xlim([1, 4.5])

axins = inset_axes(ax, width="90%", height="100%",
                   bbox_to_anchor=(0.15, 0.4, 0.57, 0.5),
                   bbox_transform=ax.transAxes, loc=3, borderpad=0)
axins.axvline(x = b_crit, color = 'gray', linestyle = '--', alpha = 0.8 ,\
        label = '$\\beta_c\\approx' + "{:.2f}".format(b_crit) + '$' )
axins.text(1.44,0.0002,'$\\beta_c\\approx'+ "{:.2f}".format(b_crit) + '$')
axins.errorbar(dat.beta, dat.C, yerr=dat.C_err, color = 'blue',\
               linestyle='None',capsize=2)
axins.scatter(dat.beta, dat.C, color = 'blue', s = 15)
axins.set_ylim([-0.00005, 0.00025])
axins.set_xlim([1.1, 2.1])
ax.set_xlabel('$\\beta$', fontsize = 12)
ax.set_ylabel('$C$', fontsize = 12)
ax.set_title('$m_2a=' + str(m2) + ', \Delta_2=' + str(Delta_2) + '$', fontsize = 14)
plt.rcParams.update({'font.size': 12})
ax.text(1.1, 0.28, '$C_{string}(x)=C + Bx^{-\eta}A^{x}$')


plt.savefig(save_fig_name + '.pdf')
#plt.savefig(save_fig_name + '.png')
#plt.show()
plt.close()

